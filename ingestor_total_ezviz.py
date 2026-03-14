import asyncio
import os
import sys
import time
import logging
import json
import re
import functools
import io
from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path
from dotenv import load_dotenv

import google.genai as genai
from pinecone import Pinecone
from playwright.async_api import async_playwright

# --- Configuración de Alta Disponibilidad v3.6.0 ---
load_dotenv()
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("ingesta_total_v3.log"),
        logging.StreamHandler()
    ]
)

# Variables de Entorno (Requeridas)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "manuales-tech")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE", "ezviz")

STORAGE_BASE = Path("storage/ezviz")
PROGRESO_FILE = Path("progreso_v3.json")
RESUMEN_FILE = Path("resumen_ingesta.txt")

# --- Utilidades de Sistema ---

def sanitizar_modelo_id(nombre: str) -> str:
    """Único punto de sanitización para evitar discrepancias."""
    if not nombre: return "UNKNOWN"
    # Tomamos la primera palabra y limpiamos caracteres extraños
    main_part = nombre.split()[0]
    return re.sub(r'[^a-zA-Z0-9-]', '', main_part).strip().upper()

def registrar_resumen(modelo_id: str, status: str, detalle: str = ""):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(RESUMEN_FILE, "a", encoding="utf-8") as f:
        f.write(f"{ts} | {modelo_id} | {status} | {detalle}\n")

def cargar_progreso(reset=False) -> set:
    if reset and PROGRESO_FILE.exists():
        logging.info("🗑️ Reset de control solicitado.")
        PROGRESO_FILE.unlink()
        return set()
    if PROGRESO_FILE.exists():
        try:
            with open(PROGRESO_FILE, "r") as f:
                return set(json.load(f))
        except: return set()
    return set()

def guardar_progreso(modelo_id: str):
    progreso = list(cargar_progreso())
    if modelo_id not in progreso:
        progreso.append(modelo_id)
        with open(PROGRESO_FILE, "w") as f:
            json.dump(progreso, f, indent=4)

# --- Fase 1: Descarga y Validación Binaria ---

async def descargar_y_validar_pdf(subpagina_url: str, context, modelo_id: str) -> Optional[Path]:
    """
    ARQUITECTURA DE DATOS: Prioriza descarga local y validación del header %PDF.
    """
    folder = STORAGE_BASE / modelo_id
    pdf_path = folder / "Manual.pdf"
    
    # Check pre-existencia y validación binaria
    if pdf_path.exists():
        try:
            with open(pdf_path, 'rb') as f:
                header = f.read(4)
                if header == b'%PDF':
                    logging.info(f"♻️ {modelo_id}: PDF válido detectado localmente.")
                    return pdf_path
                else:
                    logging.warning(f"⚠️ {modelo_id}: Archivo local corrupto. Re-descargando...")
        except Exception: pass

    page = None
    try:
        logging.info(f"🌐 Navegando a subpágina: {subpagina_url}")
        page = await context.new_page()
        await page.goto(subpagina_url, wait_until="networkidle", timeout=60000)
        await page.wait_for_timeout(2000)
        
        # Búsqueda de link Manual + Español
        target_link = await page.evaluate('''() => {
            const anchors = Array.from(document.querySelectorAll('a'));
            const matches = anchors.filter(a => {
                const text = a.innerText.toLowerCase();
                const href = a.href.toLowerCase();
                return (text.includes('manual') || text.includes('user manual') || text.includes('guía')) &&
                       (text.includes('español') || text.includes('spanish') || text.includes('_es.pdf') || href.includes('_es.pdf')) &&
                       href.endsWith('.pdf');
            });
            return matches.length > 0 ? matches[0].href : null;
        }''')
        
        if not target_link:
            target_link = await page.evaluate('() => { const a = document.querySelector(\'a[href*=".pdf"]\'); return a ? a.href : null; }')

        if not target_link:
            logging.error(f"❌ {modelo_id}: No se encontró ningún enlace PDF.")
            return None

        logging.info(f"💾 Descargando: {target_link}")
        response = await page.request.get(target_link)
        if response.status == 200:
            body = await response.body()
            if body.startswith(b'%PDF'):
                folder.mkdir(parents=True, exist_ok=True)
                with open(pdf_path, "wb") as f: f.write(body)
                logging.info(f"✅ {modelo_id}: Descarga exitosa y validada.")
                return pdf_path
            else:
                logging.error(f"❌ {modelo_id}: Descarga no es un PDF válido (Faltan bytes %PDF).")
        return None
    except Exception as e:
        logging.error(f"💥 Error en descarga para {modelo_id}: {e}")
        return None
    finally:
        if page: await page.close()

# --- Fase 2: Procesamiento IA y Gestión de Cuota (429 Awareness) ---

def retry_429_aware(retries=50, wait_on_429=180):
    """Estrategia Anti-Saturación: 180s obligatorios ante 429."""
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            intentos = 0
            while True:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    err_msg = str(e).upper()
                    if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg:
                        intentos += 1
                        logging.warning(f"⚠️ [LIMITE DE CUOTA] {intentos}/{retries}. Esperando {wait_on_429}s...")
                        if intentos > retries: raise e
                        await asyncio.sleep(wait_on_429)
                        continue
                    raise e
        return wrapper
    return decorator

@retry_429_aware()
async def analizar_con_ia_controlada(pdf_path: Path, modelo_id: str, genai_client) -> Optional[Dict[str, Any]]:
    """
    FRAGMENTACIÓN INTELIGENTE: Analiza solo secciones clave para ahorrar tokens.
    """
    try:
        # Pausa preventiva Burst
        await asyncio.sleep(5)
        
        up = genai_client.files.upload(file=str(pdf_path), config={'display_name': f"Manual {modelo_id}"})
        while up.state.name == "PROCESSING":
            await asyncio.sleep(2)
            up = genai_client.files.get(name=up.name)
            
        # Prompt Optimizado (Gasto Controlado)
        prompt = f'''
        Analiza el manual del modelo EZVIZ "{modelo_id}".
        INSTRUCCIÓN: Analiza solo las secciones de instalación, reset y estados de LEDs. 
        Ignora el resto del documento para ahorrar tokens.
        
        Extrae exclusivamente en JSON:
        1. "pasos_instalacion": Montaje físico y conexiones.
        2. "configuracion_inicial": Vinculación App y red.
        3. "procedimiento_reset": Pasos del botón de reset.
        4. "codigos_led": Significado de los colores/parpadeos.
        5. "variaciones": Variaciones comerciales de "{modelo_id}".
        
        RETORNA SOLO JSON PURO.
        '''
        
        res = genai_client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[up, prompt],
            config=genai.types.GenerateContentConfig(response_mime_type="application/json")
        )
        
        # Logging de Tokens (Si está disponible en el SDK)
        try:
            tokens = res.usage_metadata.total_token_count
            logging.info(f"📊 Consumo tokens para {modelo_id}: {tokens}")
        except: pass
        
        genai_client.files.delete(name=up.name)
        return json.loads(res.text)
    except Exception as e:
        logging.error(f"❌ Error IA en {modelo_id}: {e}")
        raise e

# --- Fase 3: Vectorización y Confirmación Atómica ---

async def vectorizar_y_completar(doc_ia: Dict[str, Any], modelo_id: str, url_fuente: str, index, genai_client):
    """
    VECTORIZACIÓN: Sube a Pinecone y confirma el éxito de forma atómica.
    """
    conceptos = [
        ("Instalación", doc_ia.get("pasos_instalacion", "")),
        ("Configuración", doc_ia.get("configuracion_inicial", "")),
        ("Reset", doc_ia.get("procedimiento_reset", "")),
        ("Soporte_LED", doc_ia.get("codigos_led", ""))
    ]
    variaciones = doc_ia.get("variaciones", [modelo_id])
    
    for i, (titulo, contenido) in enumerate(conceptos):
        if not contenido or len(str(contenido)) < 20: continue
        
        texto_chunk = f"Modelo: {modelo_id} | {titulo}\n{contenido}"
        
        @retry_429_aware(retries=5, wait_on_429=60)
        async def get_emb():
            r = genai_client.models.embed_content(
                model="text-embedding-004",
                contents=texto_chunk,
                config={'task_type': 'RETRIEVAL_DOCUMENT', 'title': f"EZVIZ {modelo_id}"}
            )
            return r.embeddings[0].values
            
        vector = await get_emb()
        metadata = {
            "nombre_comercial": modelo_id,
            "seccion": titulo,
            "url_fuente": url_fuente,
            "variaciones": ", ".join(variaciones) if isinstance(variaciones, list) else str(variaciones),
            "texto_original": texto_chunk
        }
        
        index.upsert(vectors=[(f"ezv36_{modelo_id}_{i}", vector, metadata)], namespace=PINECONE_NAMESPACE)

# --- Orquestación Principal (Maratón Lenta y Segura) ---

async def procesar_modelo_controlado(item: Dict[str, str], context, index, genai_client):
    modelo_id = sanitizar_modelo_id(item['nombre'])
    subpagina = item['subpagina']
    
    logging.info(f"\n--- 🏭 PROCESANDO v3.6.0: [{modelo_id}] ---")
    
    # 1. DESCARGA -> VALIDACIÓN BINARIA
    pdf_path = await descargar_y_validar_pdf(subpagina, context, modelo_id)
    if not pdf_path:
        registrar_resumen(modelo_id, "ERROR_DESCARGA")
        return False
        
    # 2. IA -> VECTORIZACIÓN
    try:
        doc_ia = await analizar_con_ia_controlada(pdf_path, modelo_id, genai_client)
        if not doc_ia: return False

        await vectorizar_y_completar(doc_ia, modelo_id, subpagina, index, genai_client)
        
        # Marcado Atómico
        guardar_progreso(modelo_id)
        registrar_resumen(modelo_id, "OK")
        logging.info(f"🏆 [{modelo_id}] COMPLETADO AL 100%.")
        return True
    except Exception as e:
        logging.error(f"💥 Error crítico en flujo para {modelo_id}: {e}")
        registrar_resumen(modelo_id, "FALLO_IA", str(e))
        return False

async def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--reset', action='store_true')
    parser.add_argument('--test-mode', action='store_true')
    args = parser.parse_args()

    # Clientes
    if not GEMINI_API_KEY or not PINECONE_API_KEY:
        print("❌ Error: Credenciales faltantes."); return

    genai_client = genai.Client(api_key=GEMINI_API_KEY)
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index_pc = pc.Index(PINECONE_INDEX_NAME)
    
    progreso = cargar_progreso(reset=args.reset)
    
    # Discovery
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(user_agent="Mozilla/5.0 ...")
        page = await ctx.new_page()
        logging.info("🔎 Escaneando catálogo principal...")
        await page.goto("https://support.ezviz.com/download/user_manual", wait_until="networkidle")
        
        for _ in range(8):
            await page.evaluate("window.scrollBy(0, 1000)")
            await asyncio.sleep(1)

        raw_list = await page.evaluate('''() => {
            const res = [];
            document.querySelectorAll('h3').forEach(h3 => {
                const nombre = h3.innerText.trim();
                const link = h3.closest('div, li, .item')?.querySelector('a[href*="/download/user_manual/"]');
                if (nombre && link) res.push({ nombre, subpagina: link.href });
            });
            return res;
        }''')
        await browser.close()

    # Deduplicación con modelo_id
    vistos = set()
    total_list = []
    for p in raw_list:
        modelo_id = sanitizar_modelo_id(p['nombre'])
        if modelo_id not in vistos:
            total_list.append(p)
            vistos.add(modelo_id)

    if args.test_mode:
        logging.info("🛠️ MODO TEST: Solo 2 modelos.")
        total_list = total_list[:2]

    logging.info(f"📦 Total modelos en cola: {len(total_list)}")

    # Bucle Maratón Controlado
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(user_agent="Mozilla/5.0 ...")
        
        for idx, item in enumerate(total_list):
            modelo_id = sanitizar_modelo_id(item['nombre'])
            if modelo_id in progreso:
                logging.info(f"⏩ {modelo_id} ya procesado. Saltando.")
                continue
                
            exito = await procesar_modelo_controlado(item, ctx, index_pc, genai_client)
            
            # Reporte Progress
            actual = idx + 1
            if actual % 10 == 0 or actual == len(total_list):
                perc = (actual / len(total_list)) * 100
                print(f"\n📊 MARATÓN v3.6.0: [{actual}/{len(total_list)}] - [{perc:.1f}%] Completado\n")
                
            # Ritmo Maratón: 60s base
            if actual < len(total_list):
                delay = 60 if exito else 15
                logging.info(f"⏸️ Pausa de seguridad: {delay}s...")
                await asyncio.sleep(delay)

        await browser.close()

if __name__ == "__main__":
    try: asyncio.run(main())
    except KeyboardInterrupt: print("\n👋 Cancelado.")
