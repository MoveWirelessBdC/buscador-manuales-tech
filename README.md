# Proyecto Move KB: Base de Conocimiento y API de Consultas

Este proyecto tiene como objetivo construir un sistema RAG (Retrieval-Augmented Generation) para asistencia técnica, utilizando manuales oficiales de productos de seguridad.

## Arquitectura General

El sistema se compone de un flujo de ingesta de datos y una API de consultas, utilizando las siguientes tecnologías:

*   **Google Gemini 2.0 Flash:** Motor para el procesamiento de documentos y generación de respuestas.
*   **Google Gemini Embeddings (text-embedding-004):** Para la vectorización del conocimiento técnico.
*   **Pinecone:** Base de datos vectorial en la nube para almacenamiento escalable y búsqueda rápida.
*   **Playwright:** Para la extracción automatizada de manuales directamente desde portales de soporte (fuente de verdad comercial).

## Componentes Principales

### 1. Ingestor Web Comercial (`ingestor_web.py`)
Un script avanzado que automatiza la recolección de conocimiento:
*   **Scraping Inteligente:** Navega por el Centro de Soporte de EZVIZ para identificar modelos por su nombre comercial (ej. H1C, C6N).
*   **Procesamiento IA:** Descarga los manuales PDF y utiliza Gemini para extraer secciones críticas: diagramas, funciones de botones (Reset), y LEDs de estado.
*   **Vectorización:** Sube los fragmentos procesados a Pinecone con metadatos claros para facilitar la búsqueda por nombre de producto.

### 2. API de Consultas (`api.py`)
Servidor basado en Flask/Quart que conecta al usuario con el conocimiento:
*   `POST /query`: Recibe preguntas sobre instalación o soporte, busca en Pinecone y genera una respuesta informada usando Gemini.
*   `POST /get_manual`: Busca y entrega el enlace directo al manual PDF oficial.

## Configuración y Ejecución

### 1. Requisitos Previos
*   Python 3.10+ (recomendado).
*   Entorno virtual configurado.
*   Playwright instalado: `playwright install chromium`.

### 2. Variables de Entorno (`.env`)
Configura las siguientes llaves en tu archivo `.env`:
```env
GEMINI_API_KEY="tu_llave_aqui"
PINECONE_API_KEY="tu_llave_aqui"
PINECONE_INDEX_NAME="manuales-tech"
PINECONE_NAMESPACE="ezviz"
```

### 3. Ejecución del Ingestor
Para poblar la base de datos con los últimos manuales comerciales:
```bash
python ingestor_web.py
```
*(Usa `--test-mode` para procesar solo los primeros 3 modelos y validar el flujo).*

### 4. Lanzar la API
```bash
python api.py
```

## Despliegue en GCP
El proyecto está preparado para correr como un **Cloud Run Job** (el ingestor) y un **Cloud Run Service** (la API). Consulta el `Dockerfile` para más detalles sobre la construcción de la imagen.