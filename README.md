# Proyecto Move KB: Base de Conocimiento y API de Consultas

Este proyecto tiene dos componentes principales:

1.  **Pipeline de Datos:** Un conjunto de scripts que extraen contenido de un portal web, lo procesan y construyen una base de conocimiento vectorial.
2.  **API de Consultas:** Un servidor web que utiliza la base de conocimiento para responder preguntas en lenguaje natural.

## Arquitectura General

El sistema está diseñado para ser desplegado en Google Cloud, utilizando los siguientes servicios:

*   **Google Cloud Run:** Para ejecutar la API de consultas de forma escalable.
*   **Google Cloud Storage:** Para almacenar los artefactos generados por el pipeline (HTML, transcripciones, y la base de conocimiento final).
*   **Google Cloud Speech-to-Text:** Para transcribir el contenido de los videos.
*   **OpenAI API:** Para generar los *embeddings* vectoriales y las respuestas a las preguntas.

## Componentes del Proyecto

### 1. Pipeline de Datos (`main.py` y `src/`)

El pipeline automatiza la creación de la base de conocimiento. Se ejecuta localmente y sube los resultados a Google Cloud Storage.

**Pasos del Pipeline:**

1.  **Extractor (`src/extractor.py`):
    *   Inicia sesión en el portal web.
    *   Extrae las URLs de todas las guías.
    *   Descarga el contenido HTML de cada guía.
    *   Extrae las URLs de imágenes y videos.
    *   Descarga las imágenes.

2.  **Limpiador (`src/limpiador.py`):
    *   Limpia los archivos HTML eliminando etiquetas innecesarias (headers, footers, etc.).

3.  **Conversor (`src/conversor.py`):
    *   Convierte los archivos HTML limpios a formato Markdown.

4.  **Transcriptor (`src/transcriptor.py`):
    *   Descarga el audio de los videos de YouTube.
    *   Sube los archivos de audio a Google Cloud Storage.
    *   Utiliza Google Cloud Speech-to-Text para transcribir el audio.
    *   Guarda las transcripciones como archivos de texto.

5.  **Fragmentador (`src/fragmentador.py`):
    *   Divide los archivos Markdown y las transcripciones en fragmentos (chunks).
    *   Utiliza la API de OpenAI para generar un *embedding* vectorial para cada fragmento.
    *   Crea el archivo `knowledge_base.json` con los fragmentos y sus vectores, y lo sube a Google Cloud Storage.

### 2. API de Consultas (`api.py`)

Una aplicación Flask que expone un endpoint `/query` para responder preguntas.

**Funcionamiento:**

1.  **Carga de la Base de Conocimiento:** Al iniciar, la API descarga el archivo `knowledge_base.json` desde Google Cloud Storage.
2.  **Recepción de Consultas:** Recibe una pregunta en formato JSON (`{"pregunta": "..."}`).
3.  **Búsqueda Semántica:**
    *   Genera un *embedding* para la pregunta del usuario.
    *   Compara el vector de la pregunta con los vectores de la base de conocimiento para encontrar los fragmentos más relevantes (búsqueda por similitud de coseno).
4.  **Generación de Respuesta:**
    *   Envía los fragmentos relevantes y la pregunta original a un modelo de lenguaje de OpenAI.
    *   El modelo genera una respuesta basada únicamente en el contexto proporcionado.
5.  **Respuesta al Usuario:** Devuelve la respuesta generada por el modelo.

## Despliegue y Ejecución

### Configuración Local

1.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configurar variables de entorno:**
    Crea un archivo `.env` (o configura las variables en tu sistema) con las siguientes claves:
    ```
    PORTAL_USER="tu_usuario_del_portal"
    PORTAL_PASS="tu_contraseña_del_portal"
    OPENAI_API_KEY="tu_clave_de_openai"
    ```

3.  **Autenticación de Google Cloud:**
    Asegúrate de tener `gcloud` CLI instalado y autenticado:
    ```bash
    gcloud auth application-default login
    ```

### Ejecución del Pipeline de Datos

Para ejecutar el pipeline completo:

```bash
python main.py
```

Para ejecutar un paso específico (p. ej., `fragmentador`):

```bash
python main.py fragmentador
```

### Despliegue en Google Cloud Run

El proyecto incluye un `Dockerfile` y un `entrypoint.sh` para facilitar el despliegue.

1.  **Construir la imagen de Docker:**
    ```bash
    gcloud builds submit --tag gcr.io/$(gcloud config get-value project)/move-kb-api
    ```

2.  **Desplegar en Cloud Run:**
    ```bash
    gcloud run deploy move-kb-api \
      --image gcr.io/$(gcloud config get-value project)/move-kb-api \
      --platform managed \
      --region us-central1 \
      --allow-unauthenticated
    ```

## Scripts de Utilidad

*   `diagnose_url.py`: Script para depurar problemas de carga de URLs específicas con Playwright.
*   `run_diagnostics.sh`: Ejecuta `diagnose_url.py` para una lista predefinida de URLs.
*   `verify_openai.py`: Verifica que la clave de API de OpenAI esté configurada correctamente.
*   `test_server.py`: Un servidor Flask de prueba para verificar el entorno.