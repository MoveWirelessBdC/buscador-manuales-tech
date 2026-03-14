import asyncio
import os
import time
import logging
import xmlrpc.client
import ssl
import json
import urllib.request
import io
import PyPDF2
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

import google.genai as genai
from pinecone import Pinecone

# --- Configuración inicial ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Credenciales y Variables de Entorno ---
ODOO_URL = os.getenv("ODOO_URL", "https://tu-odoo.com")
ODOO_DB = os.getenv("ODOO_DB", "nombre_db")
ODOO_USER = os.getenv("ODOO_USER", "usuario@email.com")
ODOO_PASSWORD = os.getenv("ODOO_PASSWORD", "tu_password_odoo")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "manuales-tech")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE", "ezviz")

# Inicializar clientes de API
if GEMINI_API_KEY:
    genai_client = genai.Client(api_key=GEMINI_API_KEY)
else:
    logging.warning("GEMINI_API_KEY no encontrada.")
    genai_client = None

if PINECONE_API_KEY:
    pc = Pinecone(api_key=PINECONE_API_KEY)
    pinecone_index = pc.Index(PINECONE_INDEX_NAME)
else:
    logging.warning("PINECONE_API_KEY no encontrada.")
    pinecone_index = None

# Configuración de Odoo SSL (ignorar certificados inválidos si es necesario en local, quitar context en prod seguro)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Importar la función existente de Playwright para obtener PDFs
try:
    from src.marcas.ezviz import obtener_pdf_ezviz
except ImportError:
    logging.error("No se pudo importar 'obtener_pdf_ezviz'. Asegúrate de ejecutar este script desde la raíz del proyecto.")
    # Creando una función mock rápida en caso de test
    async def obtener_pdf_ezviz(modelo):
         raise NotImplementedError("Dependencia no encontrada src.marcas.ezviz")

# --- Funciones Core ---

def obtener_modelos_odoo_ezviz() -> List[str]:
    """Se conecta a Odoo mediante XML-RPC y lista todos los productos (modelos) de la categoría EZVIZ."""
    logging.info(f"Conectando a Odoo en {ODOO_URL}...")
    try:
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL), context=ctx)
        uid = common.authenticate(ODOO_DB, ODOO_USER, ODOO_PASSWORD, {})
        if not uid:
            logging.error("Fallo la autenticación en Odoo.")
            return []
            
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL), context=ctx)
        
        # 1. Buscar plantillas de producto que contengan 'EZVIZ' en el nombre
        product_template_ids = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'product.template', 'search',
            [[['name', 'ilike', 'EZVIZ']]])

        # Obtener los nombres/modelos (ej. campo 'default_code' o 'name')
        if not product_template_ids:
             logging.info("No se encontraron plantillas de productos (product.template) con la palabra EZVIZ en Odoo.")
             return []
             
        # Leer el campo que tiene el modelo, usualmente 'default_code' (Referencia interna)
        productos = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'product.template', 'read',
            [product_template_ids],
            {'fields': ['default_code', 'name']})
            
        lista_modelos = []
        for p in productos:
            # Preferir referencia interna, sino el nombre
            modelo = p.get('default_code')
            if not modelo:
                 modelo = p.get('name', '').replace('EZVIZ', '').strip()
            
            if modelo and modelo not in lista_modelos:
                lista_modelos.append(modelo)
                
        logging.info(f"Se encontraron {len(lista_modelos)} modelos de EZVIZ en Odoo.")
        return lista_modelos

    except Exception as e:
        logging.error(f"Error al conectar con Odoo o extraer modelos: {e}")
        return []

def descargar_pdf_a_memoria(url: str) -> Optional[io.BytesIO]:
    """Descarga el PDF desde la URL y lo mantiene en memoria."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            pdf_bytes = response.read()
            return io.BytesIO(pdf_bytes)
    except Exception as e:
        logging.error(f"Fallo al descargar PDF desde {url}: {e}")
        return None

def extraer_texto_pdf(pdf_buffer: io.BytesIO) -> str:
    """Extrae texto base del PDF (usado como respaldo si Gemini falla o para chunking ligero)."""
    try:
        reader = PyPDF2.PdfReader(pdf_buffer)
        texto = ""
        for page in reader.pages:
            t = page.extract_text()
            if t: texto += t + "\n"
        return texto
    except Exception as e:
         logging.error(f"Fallo al extraer texto con PyPDF2: {e}")
         return ""

def analizar_documento_con_gemini(pdf_buffer: io.BytesIO, link_pdf: str, modelo: str) -> List[Dict[str, Any]]:
    """
    Sube el documento a Gemini 1.5 Flash y le pide un análisis estructurado
    de cada sección, diagramas y botones.
    Devuelve fragmentos procesados listos para vectorizar.
    """
    logging.info(f"Subiendo documento temporal a la API de Gemini File API...")
    # Guardar en temp para subir a Gemini API
    temp_filename = f"/tmp/manual_{modelo}.pdf"
    with open(temp_filename, "wb") as f:
         f.write(pdf_buffer.getbuffer())
         
    try:
        # Subir el PDF a Gemini usando Client de genai
        if not genai_client:
            raise Exception("Cliente Gemini no inicializado.")
            
        uploaded_file = genai_client.files.upload(file=temp_filename, display_name=f"Manual {modelo}")
        
        # Esperar a que el archivo sea procesado
        while uploaded_file.state.name == "PROCESSING":
             logging.info("Esperando que Gemini procese el archivo...")
             time.sleep(2)
             uploaded_file = genai_client.files.get(name=uploaded_file.name)
             
        if uploaded_file.state.name == "FAILED":
             raise Exception("Fallo el procesamiento del archivo en Gemini.")
             
        prompt = '''
        Analiza este manual técnico de una cámara o dispositivo EZVIZ.
        Necesito que extraigas la información clave y la devuelvas en un formato de lista estructurada de secciones JSON-like.
        Para cada sección importante del manual, extrae:
        - "titulo": El nombre de la sección (ej. "Instalación", "Conexión a Wi-Fi", "Solución de Problemas")
        - "contenido": Un resumen técnico detallado de la sección.
        
        Presta especial atención a:
        1. Describir detalladamente con palabras cualquier diagrama de conexión eléctrica o de red que veas.
        2. Describir cuál es la función de los botones físicos (especialmente el de RESET) y los pasos exactos para usarlos.
        3. Interpretación de los LEDs de estado (qué significa luz roja, luz azul parpadeante, etc.).
        
        Responde SOLO con una lista válida en formato JSON, usando esta estructura exacta:
        [
          {
            "titulo": "Diagrama de conexión",
            "contenido": "..."
          },
          {
            "titulo": "Botón de Reset",
            "contenido": "..."
          }
        ]
        No añadas texto markdown tipo ```json fuera de la estructura pura si es posible, o asegúrate de que sea parseable.
        '''
        
        logging.info("Ejecutando prompt en Gemini 1.5 Flash...")
        response = genai_client.models.generate_content(
            model='gemini-1.5-flash-latest',
            contents=[uploaded_file, prompt]
        )
        
        # Limpiar archivo de Gemini
        genai_client.files.delete(name=uploaded_file.name)
        os.remove(temp_filename)
        
        # Parsear respuesta (limpiar markdown ticks)
        texto_crudo = response.text.strip()
        if texto_crudo.startswith("```json"):
            texto_crudo = texto_crudo[7:]
        if texto_crudo.startswith("```"):
            texto_crudo = texto_crudo[3:]
        if texto_crudo.endswith("```"):
            texto_crudo = texto_crudo[:-3]
            
        fragmentos = json.loads(texto_crudo)
        return fragmentos
        
    except Exception as e:
        logging.error(f"Error analizando con Gemini: {e}")
        # Intentar limpieza por si acaso
        if os.path.exists(temp_filename):
             os.remove(temp_filename)
        return []

def generar_embeddings_y_subir(fragmentos: List[Dict[str, Any]], modelo: str, url: str):
    """Convierte el texto en embeddings usando text-embedding-004 y sube a Pinecone."""
    if not pinecone_index:
        logging.error("Pinecone no está configurado, omitiendo subida.")
        return
        
    for i, frag in enumerate(fragmentos):
         texto_para_vectorizar = f"Modelo: {modelo}. Sección: {frag.get('titulo', 'General')}\n{frag.get('contenido', '')}"
         
         try:
             # Generar vector con text-embedding-004
             if not genai_client:
                 raise Exception("Cliente Gemini no inicializado.")
                 
             result = genai_client.models.embed_content(
                model="text-embedding-004",
                contents=texto_para_vectorizar,
                config={
                     "task_type": "RETRIEVAL_DOCUMENT",
                     "title": f"Manual {modelo} - {frag.get('titulo')}"
                }
             )
             
             # Verificar estructura de respuesta sdk genai 1.4+
             vector = result.embeddings[0].values if getattr(result, 'embeddings', None) else []
             if not vector:
                 logging.error("No se generó el vector.")
                 continue
             
             # Generar ID único
             id_vector = f"ezviz_{modelo}_{i}"
             
             # Subir a Pinecone
             metadata = {
                 "modelo": modelo,
                 "marca": "EZVIZ",
                 "url": url,
                 "titulo_seccion": frag.get('titulo', ''),
                 "texto_original": texto_para_vectorizar
             }
             
             pinecone_index.upsert(
                 vectors=[(id_vector, vector, metadata)],
                 namespace=PINECONE_NAMESPACE
             )
             logging.info(f"Vector {id_vector} subido exitosamente a Pinecone.")
             
         except Exception as e:
              logging.error(f"Fallo al vectorizar/subir fragmento de {modelo}: {e}")

# --- Flujo Principal Asíncrono ---

async def procesar_manual_modelo(modelo: str):
    """Coordina todo el proceso para un solo modelo."""
    logging.info(f"\n--- Iniciando procesamiento para el modelo: {modelo} ---")
    
    # 1. Obtener URL del PDF usando Playwright
    logging.info(f"Buscando manual PDF usando Playwright de la interfaz existente...")
    resultado_busqueda = await obtener_pdf_ezviz(modelo)
    
    if resultado_busqueda.get('status') != 'success' or not resultado_busqueda.get('url_documento'):
         logging.warning(f"No se encontró un PDF válido para {modelo}. Motivo: {resultado_busqueda.get('message', 'Desconocido')}")
         return
         
    url_pdf = resultado_busqueda['url_documento']
    logging.info(f"URL del PDF encontrada: {url_pdf}")
    
    # 2. Descargar PDF a memoria
    pdf_buffer = descargar_pdf_a_memoria(url_pdf)
    if not pdf_buffer:
        return
        
    # 3. Analizar documento con Gemini 1.5 Flash
    fragmentos = analizar_documento_con_gemini(pdf_buffer, url_pdf, modelo)
    if not fragmentos:
         logging.warning(f"La extracción falló para {modelo}. Intentando chunking simple (respaldo)...")
         # Respaldo simple (opcional, en este caso retornaremos vacío como fallback primario)
         return
         
    logging.info(f"Gemini extrajo {len(fragmentos)} secciones estructuradas.")
    
    # 4. Vectorizar texto en embeddings 004 y subir a Pinecone
    # Se recomienda esperar un segundo entre embeddings por rate limits
    logging.info("Generando Embeddings y subiendo a Pinecone...")
    generar_embeddings_y_subir(fragmentos, modelo, url_pdf)
    
    logging.info(f"Finalizado procesamiento para el modelo: {modelo}")

async def main():
    logging.info("INICIANDO INGESTOR DE ODOO -> GEMINI -> PINECONE")
    
    # 1. Extraer lista de modelos desde Odoo
    modelos = obtener_modelos_odoo_ezviz()
    
    if not modelos:
        logging.info("No hay modelos para procesar. Saliendo.")
        return
        
    logging.info(f"Comenzando procesamiento de {len(modelos)} modelos.")
    
    # 2. Iterar por modelo y procesarlo secuencialmente con delay
    for idx, modelo in enumerate(modelos):
        try:
             await procesar_manual_modelo(modelo)
        except Exception as e:
             logging.error(f"Excepción fatal al procesar {modelo}: {e}")
             
        # Delay de 20 segundos para evitar bloqueos por rate limit (anti bot EZVIZ y Gemini)
        if idx < len(modelos) - 1:
            logging.info("Esperando 20 segundos antes del siguiente modelo para evitar bloqueos (anti-bot)...")
            await asyncio.sleep(20)
            
    logging.info("PROCESO INGESTOR FINALIZADO")

if __name__ == "__main__":
    asyncio.run(main())
