# Proyecto Move KB: Base de Conocimiento y API de Consultas

Este proyecto tiene dos componentes principales:

1.  **Pipeline de Datos:** Un conjunto de scripts que extraen contenido de un portal web, lo procesan y construyen una base de conocimiento vectorial.
2.  **API de Consultas:** Un servidor web que utiliza la base de conocimiento para responder preguntas en lenguaje natural.

## Arquitectura General

El sistema está diseñado para ser desplegado en Google Cloud y ejecutado en entornos locales, e incluye las siguientes tecnologías y servicios principales:

*   **Google Cloud Storage y Cloud Run:** Para almacenar artefactos y desplegar el backend.
*   **Google Gemini AI:** Motor del sistema conversacional (`gemini-1.5-flash`) y de la creación de *embeddings* vectoriales (`text-embedding-004`).
*   **FAISS:** Base de datos vectorial optimizada instalada en local.
*   **Playwright (Asíncrono):** Para la automatización web tipo RPA (Robotic Process Automation), permitiendo interactuar con sitios de soporte oficiales y evadir barreras anti-bot.
*   **APIs Híbridas (DuckDuckGo + Navegación Directa):** Para la localización de manuales PDF de distintas marcas tecnológicas corporativas.

## Componentes del Proyecto

### 1. Servidor de Consultas / Endpoints (`api.py`)

Una aplicación robusta construida sobre Flask que expone interfaces de atención al usuario:

*   `POST /query` -> **Buscador IA Base de Conocimiento:**
    1. Acepta una pregunta (ej. `{"pregunta": "¿Cómo instalo la cámara?"}`).
    2. Convierte la pregunta a vector 3D mediante **Google Gemini**.
    3. Busca los fragmentos literarios más exactos en la base de datos local **FAISS**.
    4. Envía el contexto estructurado al modelo **Gemini 1.5 Flash**.
    5. Retorna la respuesta oficial en español y con recomendaciones de lectura.

*   `POST /get_manual` -> **Microservicio Extractor de Manuales Web (Playwright):**
    1. Acepta y registra una petición para una marca específica (Actualmente: **EZVIZ**). Por ejemplo: `{"modelo": "h1c"}`.
    2. Ejecuta una orden asíncrona a un navegador web Chromium invisible.
    3. Traza una red híbrida de búsqueda: consulta en el buscador DuckDuckGo por el centro de descargas oficial local, y de fallar, extrae el enlace exacto navegando con Python MFS.
    4. Devuelve el enlace directo y limpio al manual PDF corporativo.

*(Nota: Dentro de la carpeta `src/marcas` el sistema tiene un diseño componetizado, preparado para agregar en el futuro integraciones con Dahua, Hikvision, etc).*

### 2. Pipeline ETL Original (`main.py` y tools antiguas)

El proyecto aún conserva bajo sus carpetas la lógica ETL para el relleno de la base de conocimiento vectorial antigua (scraping de web, conversión MD, y subida a la nube), lista para ser invocada mediante los scripts correspondientes o los jobs de `main.py`.

## Despliegue y Ejecución

### Configuración Local

1.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configurar variables de entorno (`.env`):**
    Crea un archivo `.env` en la raíz con tus claves:
    ```env
    PORTAL_USER="tu_usuario_del_portal"
    PORTAL_PASS="tu_contraseña_del_portal"
    GEMINI_API_KEY="tu_api_key_de_Google_Gemini"
    ```

3.  **Descargar navegadores de Playwright:**
    ```bash
    playwright install chromium
    ```

### Iniciar la API

Para levantar el servidor dual de IA y Playwright:

```bash
python api.py
```
*(Se recomienda siempre ejecutar dentro de un entorno virtual `.venv`)*.

### Despliegue en Google Cloud Run

El proyecto incluye un `Dockerfile` y un `entrypoint.sh` para facilitar el despliegue.

1.  **Construir la imagen de Docker:**
    ```bash
    gcloud builds submit --tag gcr.io/$(gcloud config get-value project)/buscador-manuales-tech
    ```

2.  **Desplegar en Cloud Run:**
    ```bash
    gcloud run deploy buscador-manuales-tech \
      --image gcr.io/$(gcloud config get-value project)/buscador-manuales-tech \
      --platform managed \
      --region us-central1 \
      --allow-unauthenticated
    ```

## Scripts de Utilidad

*   `diagnose_url.py`: Script para depurar problemas de carga de URLs específicas con Playwright.
*   `run_diagnostics.sh`: Ejecuta `diagnose_url.py` para una lista predefinida de URLs.
*   `verify_openai.py`: Verifica que la clave de API de OpenAI esté configurada correctamente.
*   `test_server.py`: Un servidor Flask de prueba para verificar el entorno.