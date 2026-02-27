# config.py (Versión Final Verificada)
import os

# --- ESTRUCTURA DE DIRECTORIOS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MARKDOWN_DIR = os.path.join(DATA_DIR, '3_manuales_md')
KNOWLEDGE_BASE_DIR = os.path.join(DATA_DIR, '5_knowledge_base')
KB_JSON_FILENAME = "knowledge_base.json"
KB_JSON_FILE_PATH = os.path.join(KNOWLEDGE_BASE_DIR, KB_JSON_FILENAME)

# --- CONFIGURACIÓN DE IA (OPENAI) ---
OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"
AI_MODEL_NAME = "gpt-3.5-turbo"

# --- ¡CONFIGURACIÓN FALTANTE! ---
AI_GENERATION_CONFIG = {
    "temperature": 0.2,
    "max_tokens": 1024
}

# --- CONFIGURACIÓN DEL FRAGMENTADOR ---
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

# --- (Otras configuraciones del pipeline) ---
INDEX_URL = "https://portal.move-wifi.com/guide/index.html"
DEFAULT_TIMEOUT = 60000
HEADLESS_MODE = True
LOGIN_USER_SELECTOR = "#login-page-login-input"
LOGIN_PASS_SELECTOR = "#login-page-password-input"
LOGIN_BUTTON_SELECTOR = "#login-page-login-button"
TFA_REMIND_SELECTOR = "button:has-text('Remind me later')"
GUIDE_LINK_SELECTOR = ".md-nav__link"
CONTENT_SELECTORS = [".article-body", ".md-content"]
HTML_TAGS_TO_REMOVE = ['header', 'nav', 'footer', 'script', 'style', 'aside', 'form']
GCS_BUCKET_NAME = "move-kb-audio-files-unique"
GCP_PROJECT_ID = "move-agent-prod"
GCP_REGION = "us-west1"
VIDEO_URLS_FILE = os.path.join(DATA_DIR, "videos_a_procesar.txt")
TRANSCRIPTION_LANG = "es-VE"