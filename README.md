# Proyecto Move KB: RAG Industrial EZVIZ (v3.6.0)

Sistema avanzado de **Generación Aumentada por Recuperación (RAG)** diseñado para automatizar el soporte técnico de dispositivos de seguridad mediante el procesamiento de manuales técnicos oficiales.

## Arquitectura de Alta Disponibilidad (v3.6.0)

El proyecto ha sido refactorizado para soportar operaciones de carga masiva industrial, superando bloqueos de red y límites de cuota de IA:

*   **Ingestor Industrial (`ingestor_total_ezviz.py`)**: Arquitectura de rescate que utiliza **Playwright** para navegación profunda, evitando errores 403 y capturando enlaces reales de manuales en español.
*   **Resiliencia 429**: Protocolo inteligente que detecta saturación de cuota en **Gemini 2.0 Flash** y aplica enfriamientos automáticos de 180 segundos.
*   **Optimización de Tokens**: Fragmentación de documentos para analizar solo secciones críticas (Instalación, Reset, LEDs), reduciendo drásticamente el consumo de tokens por modelo.
*   **Base Vectorial**: Integración nativa con **Pinecone** para búsqueda semántica de alta precisión en el namespace `ezviz`.

## Componentes Técnicos

1.  **Ingestor de Alto Rendimiento**:
    *   **Unificación Maestra**: Uso estricto de `modelo_id` para trazabilidad total.
    *   **Validación Binaria**: Chequeo del header `%PDF` antes de cualquier procesamiento de IA.
    *   **Persistencia de Progreso**: Registro atómico en `progreso_v3.json` para permitir reanudaciones sin duplicidad.

2.  **API de Consultas (`api.py`)**:
    *   Servidor basado en **Quart** (Async Flask).
    *   Endpoint `/get_manual`: Recuperación dinámica de links de descarga.
    *   Próximamente: Integración de chat conversacional RAG.

## Configuración y Ejecución

### 1. Preparación del Entorno
```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. Variables de Entorno (`.env`)
```env
GEMINI_API_KEY="tu_llave"
PINECONE_API_KEY="tu_llave"
PINECONE_INDEX_NAME="manuales-tech"
PINECONE_NAMESPACE="ezviz"
```

### 3. Ejecución Industrial (Carga de 306 modelos)
Para iniciar la maratón de ingesta en segundo plano:
```bash
nohup python3 ingestor_total_ezviz.py > ingesta_v36.log 2>&1 &
```

Para validaciones rápidas:
```bash
python3 ingestor_total_ezviz.py --test-mode --reset
```

## Monitoreo de Ingesta
*   **Logs**: `tail -f ingesta_v36.log`
*   **Reporte de Éxito**: `cat resumen_ingesta.txt`

## Historial de Versiones
*   `v3.4.0`: Implementación de Navegación Profunda (Bypass 403).
*   `v3.5.0`: Flujo Descarga -> Validación -> IA (Eficiencia de Tokens).
*   `v3.6.0`: Arquitectura de Alta Disponibilidad y unificación de variables.

---
*Mantenido por el equipo de Arquitectura de Datos de MoveWireless.*