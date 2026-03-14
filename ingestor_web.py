import asyncio
import os
import time
import logging
import json
import urllib.request
import io
import functools
import re
from datetime import datetime
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

import google.genai as genai
from pinecone import Pinecone
from playwright.async_api import async_playwright

# --- Configuración inicial ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Credenciales y Variables de Entorno ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE", "ezviz_knowledge")
PROGRESO_FILE = "progreso_v3.json"
DISCOVERY_FILE = "discovery_total.json"

# --- Utilidades de Sistema (Checkpoints y Normalización) ---

def cargar_progreso() -> set:
    if os.path.exists(PROGRESO_FILE):
        try:
            with open(PROGRESO_FILE, "r") as f:
                return set(json.load(f))
        except:
            return set()
    return set()

def guardar_progreso(modelo: str):
    progreso = cargar_progreso()
    progreso.add(modelo)
    with open(PROGRESO_FILE, "w") as f:
        json.dump(list(progreso), f, indent=4)

def limpiar_nombre_modelo(nombre: str) -> str:
    """
    Normaliza el nombre comercial del producto.
    Ej: 'C6N 4MP Smart Wi-Fi...' -> 'C6N'
    """
    # Tomar la primera palabra o identificador principal (letras y números seguidos)
    # Por lo general el modelo es lo primero: C6N, H1C, BC1, etc.
    partes = nombre.split()
    if not partes: return nombre
    
    modelo = partes[0].strip()
    # Limpieza de caracteres raros al final
    modelo = re.sub(r'[^a-zA-Z0-9-]', '', modelo)
    return modelo

# --- Inicialización de Clientes ---
genai_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None
if PINECONE_API_KEY:
    pc = Pinecone(api_key=PINECONE_API_KEY)
    pinecone_index = pc.Index(PINECONE_INDEX_NAME)
else:
    pinecone_index = None

# --- Decoradores de Robustez ---

def retry_with_backoff(retries=5, backoff_in_seconds=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            x = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if "429" not in str(e) and "RESOURCE_EXHAUSTED" not in str(e) and x >= retries:
                        raise e
                    
                    if x == retries:
                        logging.error(f"Se agotaron los {retries} reintentos para {func.__name__}.")
                        raise e
                    
                    sleep = (backoff_in_seconds * (2 ** x))
                    logging.warning(f"⚠️ Error en {func.__name__}: {e}. Reintentando en {sleep}s (Intento {x+1}/{retries})...")
                    time.sleep(sleep)
                    x += 1
        return wrapper
    return decorator

# --- Funciones Core (Módulo Web de Extracción) ---

async def obtener_catalogo_web_ezviz(test_mode=False) -> List[Dict[str, str]]:
    """
    Navega a la página de manuales de usuario de EZVIZ, extrae los nombres
    comerciales e identifica sus enlaces de descarga.
    """
    # Usamos la página que lista específicamente todos los manuales de usuario
    url_manuales_global = "https://support.ezviz.com/download/user_manual"
    modelos_encontrados = []
    
    logging.info(f"Iniciando raspado web en: {url_manuales_global}...")
    
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = await context.new_page()
            page.set_default_timeout(60000)
            
            await page.goto(url_manuales_global, wait_until="networkidle")
            logging.info("Página de manuales cargada. Limpiando vista...")
            
            # Aceptar cookies
            try:
                cookie_btn = await page.query_selector("button#onetrust-accept-btn-handler")
                if cookie_btn: await cookie_btn.click()
            except: pass
                
            await page.wait_for_timeout(3000)

            # Extraer modelos y links
            # Según la investigación:
            # - Nombres comerciales en <h3>
            # - Enlaces de descarga con clase .yf-download o similar
            
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context(user_agent="Mozilla/5.0 ...")
                page = await context.new_page()
                
                logging.info(f"Iniciando descubrimiento en: {url_manuales_global}")
                await page.goto(url_manuales_global, wait_until="networkidle", timeout=60000)
                
                # Extraer bloques de productos
                productos_raw = await page.evaluate('''() => {
                    const items = Array.from(document.querySelectorAll('.download-item'));
                    return items.map(item => {
                        const h3 = item.querySelector('h3');
                        const link = item.querySelector('a');
                        return {
                            nombre: h3 ? h3.innerText.trim() : 'Unknown',
                            subpagina: link ? link.href : null
                        };
                    }).filter(i => i.subpagina);
                }''')
                
                logging.info(f"Encontrados {len(productos_raw)} productos. Iniciando mapeo detallado...")
                
                mapeo_total = []
                for idx, p_raw in enumerate(productos_raw):
                    nombre_limpio = limpiar_nombre_modelo(p_raw['nombre'])
                    logging.info(f"[{idx+1}/{len(productos_raw)}] Mapeando {nombre_limpio}...")
                    
                    p_data = {
                        "modelo": nombre_limpio,
                        "nombre_completo": p_raw['nombre'],
                        "manual_url": None,
                        "qsg_url": None,
                        "faq_url": f"https://support.ezviz.com/faq?keyword={nombre_limpio}" # Link dinámico FAQ
                    }
                    
                    try:
                        subpage = await context.new_page()
                        await subpage.goto(p_raw['subpagina'], wait_until="networkidle", timeout=30000)
                        
                        links = await subpage.evaluate('''() => {
                            const allLinks = Array.from(document.querySelectorAll('a'));
                            return allLinks.map(a => ({ text: a.innerText.toLowerCase(), href: a.href }));
                        }''')
                        
                        # Buscar Manual (prioridad ES)
                        manual = next((l['href'] for l in links if ('.pdf' in l['href']) and ('user manual' in l['text'] or 'manual de usuario' in l['text'])), None)
                        # Buscar QSG (Quick Start Guide)
                        qsg = next((l['href'] for l in links if ('.pdf' in l['href']) and ('qsg' in l['text'] or 'guía' in l['text'] or 'quick start' in l['text'])), None)
                        
                        # Fallbacks si no se encuentran explícitamente
                        if not manual: manual = f"https://mfs.ezvizlife.com/{nombre_limpio}_UM_ES.pdf"
                        if not qsg: qsg = f"https://mfs.ezvizlife.com/{nombre_limpio}_QSG_ES.pdf"
                        
                        p_data["manual_url"] = manual
                        p_data["qsg_url"] = qsg
                        mapeo_total.append(p_data)
                        
                        await subpage.close()
                    except Exception as e:
                        logging.warning(f"Error mapeando subpágina de {nombre_limpio}: {e}")
                        # Aun con error, guardamos fallbacks
                        p_data["manual_url"] = f"https://mfs.ezvizlife.com/{nombre_limpio}_UM_ES.pdf"
                        p_data["qsg_url"] = f"https://mfs.ezvizlife.com/{nombre_limpio}_QSG_ES.pdf"
                        mapeo_total.append(p_data)

                    if test_mode and len(mapeo_total) >= 3: break
                    
                await browser.close()
                
                with open(DISCOVERY_FILE, "w", encoding="utf-8") as f:
                    json.dump(mapeo_total, f, indent=4, ensure_ascii=False)
                    
                return mapeo_total
                    
    except Exception as e:
        logging.error(f"Fallo durante la extracción del catálogo de EZVIZ: {e}")
        return []

# --- Resto de Funciones Copiadas y Adaptadas del Ingestor Previo ---

def descargar_pdf_a_memoria(url: str) -> Optional[io.BytesIO]:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            pdf_bytes = response.read()
            return io.BytesIO(pdf_bytes)
    except Exception as e:
        logging.error(f"Fallo al descargar PDF desde {url}: {e}")
        return None

@retry_with_backoff(retries=4, backoff_in_seconds=5)
def analizar_documento_con_gemini(pdf_buffer: io.BytesIO, modelo: str) -> Dict[str, Any]:
    logging.info(f"Subiendo documento {modelo} a la API de Gemini (File API)...")
    temp_filename = f"/tmp/manual_{modelo.replace(' ', '_')}.pdf"
    with open(temp_filename, "wb") as f:
         f.write(pdf_buffer.getbuffer())
         
    try:
        # 1. Subir a File API
        uploaded_file = genai_client.files.upload(
            file=temp_filename, 
            config={'display_name': f"Manual {modelo}"}
        )
        
        while uploaded_file.state.name == "PROCESSING":
             time.sleep(2)
             uploaded_file = genai_client.files.get(name=uploaded_file.name)
             
        if uploaded_file.state.name == "FAILED":
             raise Exception("Fallo el procesamiento del archivo en Gemini.")
             
        # 2. Prompt Multimodal con 3 Bloques Estrictos
        prompt = f'''
        Analiza este manual técnico del dispositivo EZVIZ "{modelo}".
        Extrae la información técnica y devuélvela en un formato JSON estructurado con estos 3 bloques obligatorios:
        
        BLOQUES A EXTRAER:
        1. "bloque_instalacion": Pasos detallados para el montaje físico y conexión de cables. Describe diagramas si los hay.
        2. "bloque_configuracion": Pasos para vincular a la app EZVIZ y configuración de red/Wi-Fi.
        3. "bloque_solucion_problemas": Función de botones (RESET), estados de LEDs y problemas comunes.
        
        ADICIONAL:
        4. "variaciones_nombre": Lista de 5 variaciones comerciales del nombre "{modelo}" (ej. minúsculas, con/sin guiones).
        
        Responde SOLO el JSON con esta estructura:
        {{
          "variaciones_nombre": [...],
          "secciones": [
            {{"titulo": "Instalación", "contenido": "..."}},
            {{"titulo": "Configuración de Software", "contenido": "..."}},
            {{"titulo": "Solución de Problemas (Reset/LEDs)", "contenido": "..."}}
          ]
        }}
        '''
        
        logging.info(f"Extracción multimodal para {modelo}...")
        response = genai_client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[uploaded_file, prompt]
        )
        
        genai_client.files.delete(name=uploaded_file.name)
        if os.path.exists(temp_filename): os.remove(temp_filename)
        
        texto_crudo = response.text.strip()
        if "```json" in texto_crudo:
            texto_crudo = texto_crudo.split("```json")[1].split("```")[0].strip()
        elif "```" in texto_crudo:
            texto_crudo = texto_crudo.split("```")[1].split("```")[0].strip()
            
        return json.loads(texto_crudo)
        
    except Exception as e:
        logging.error(f"Error en Gemini para {modelo}: {e}")
        raise e

def generar_embeddings_y_subir(datos_ia: Dict[str, Any], modelo: str, url: str):
    if not pinecone_index: return
        
    secciones = datos_ia.get("secciones", [])
    variaciones = datos_ia.get("variaciones_nombre", [modelo])
    timestamp = datetime.now().isoformat()
    
    for i, sec in enumerate(secciones):
         texto = f"Modelo: {modelo}. Sección: {sec.get('titulo')}\n{sec.get('contenido')}"
         
         @retry_with_backoff(retries=3)
         def operacion_vectorial():
             res = genai_client.models.embed_content(
                model="text-embedding-004",
                contents=texto,
                config={'task_type': 'RETRIEVAL_DOCUMENT', 'title': f"EZVIZ {modelo}"}
             )
             vec = res.embeddings[0].values
             
             metadata = {
                 "modelo_comercial": modelo,
                 "seccion": sec.get('titulo'),
                 "url_pdf": url,
                 "variaciones": ", ".join(variaciones),
                 "timestamp": timestamp,
                 "texto_original": texto
             }
             pinecone_index.upsert(vectors=[(f"web_{modelo}_{i}", vec, metadata)], namespace=PINECONE_NAMESPACE)
             return True

         try:
             operacion_vectorial()
         except Exception as e:
              logging.error(f"Fallo vectorización {modelo}: {e}")
              
    logging.info(f"Subidos {exitos} vectores para el modelo {modelo}.")

# --- Orquestación Principal ---

async def procesar_modelo_comercial(producto: Dict[str, str]):
    modelo_comercial = producto['modelo']
    pdf_url = producto['pdf_url']
    
    logging.info(f"\n--- Iniciando vectorización para: [{modelo_comercial}] ---")
    
    # 1. Bajar
    pdf_buffer = descargar_pdf_a_memoria(pdf_url)
    if not pdf_buffer: return
    
    # 2. Analizar (con reintentos internos y generación de variaciones)
    try:
        datos_ia = analizar_documento_con_gemini(pdf_buffer, modelo_comercial)
        if not datos_ia or not datos_ia.get("secciones"): 
            logging.warning(f"Extracción vacía para {modelo_comercial}.")
            return
            
        # 3. Insertar a Vector DB (con variaciones)
        generar_embeddings_y_subir(datos_ia, modelo_comercial, pdf_url)
        logging.info(f"✓ Modelo {modelo_comercial} completado exitosamente.")
    except Exception as e:
        logging.error(f"❌ Abortando procesamiento de {modelo_comercial} tras fallos persistentes: {e}")

async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Ingestor Web Movilmar v2.0")
    parser.add_argument('--test-mode', action='store_true', help="Solo extrae y procesa los primeros 3 módulos")
    args = parser.parse_args()

    logging.info("🚀 INICIANDO INGESTOR WEB MOVILMAR v2.0")
    
    # 1. Cargar checkpoints
    procesados = cargar_progreso()
    
    # 2. Obtener catálogo
    productos = await obtener_catalogo_web_ezviz(test_mode=args.test_mode)
    if not productos: return
        
    # 3. Ingerir con skipping y rate limit
    for idx, prod in enumerate(productos):
        modelo = prod['modelo_comercial']
        
        if modelo in procesados:
            logging.info(f"⏩ Saltando {modelo} (Identificado en progreso.json)")
            continue
            
        try:
             await procesar_modelo_comercial(prod)
             guardar_progreso(modelo)
        except Exception as e:
             logging.error(f"Error fatal en {modelo}: {e}")
             
        if idx < len(productos) - 1:
            logging.info(">>> Pausa de seguridad (35s) - 2 manuales/min...")
            await asyncio.sleep(35)

if __name__ == "__main__":
    asyncio.run(main())
