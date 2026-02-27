# src/conversor.py (Versión 2 - Paralelo y Robusto)
import os
import logging
from markdownify import markdownify as md
from concurrent.futures import ProcessPoolExecutor, as_completed
import config

def convert_file_to_markdown(file_path):
    """
    Toma la ruta de un archivo HTML, lo convierte a Markdown y lo guarda.
    Diseñada para ser ejecutada en un proceso paralelo.
    """
    filename = os.path.basename(file_path)
    try:
        # Leer el contenido del archivo HTML limpio
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Convertir a Markdown usando la librería y el estilo deseado
        markdown_text = md(html_content, heading_style="ATX", strip=[])

        # Generar la ruta del archivo de salida
        output_filename = os.path.splitext(filename)[0] + ".md"
        output_path = os.path.join(config.MARKDOWN_DIR, output_filename)

        # Escribir el archivo Markdown
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_text)

        return filename, "Éxito"
    except Exception as e:
        logging.error(f"No se pudo convertir el archivo '{filename}'. Causa: {e}", exc_info=False)
        return filename, str(e)

def run():
    """
    Punto de entrada que orquesta la conversión de archivos HTML a Markdown en paralelo.
    """
    logging.info("Iniciando proceso de conversión a Markdown...")

    if not os.path.exists(config.MARKDOWN_DIR):
        os.makedirs(config.MARKDOWN_DIR)
        logging.info(f"Directorio de salida '{config.MARKDOWN_DIR}' creado.")

    try:
        cleaned_files = [os.path.join(config.HTML_CLEANED_DIR, f)
                         for f in os.listdir(config.HTML_CLEANED_DIR) if f.endswith(".html")]

        if not cleaned_files:
            logging.warning("No se encontraron archivos HTML limpios para convertir. Saltando paso.")
            return

        logging.info(f"Se encontraron {len(cleaned_files)} archivos para convertir. Iniciando procesamiento en paralelo...")

        success_count = 0
        failure_count = 0
        failed_files = []

        # Usar un pool de procesos para ejecutar las tareas de conversión en paralelo
        with ProcessPoolExecutor() as executor:
            future_to_file = {executor.submit(convert_file_to_markdown, file_path): file_path for file_path in cleaned_files}

            for future in as_completed(future_to_file):
                filename, result = future.result()
                if result == "Éxito":
                    success_count += 1
                else:
                    failure_count += 1
                    failed_files.append((filename, result))

        # --- Reporte Final de la Conversión ---
        logging.info("--- Reporte de Conversión ---")
        logging.info(f"Archivos convertidos exitosamente: {success_count}")
        logging.info(f"Archivos fallidos: {failure_count}")
        if failure_count > 0:
            logging.warning("Los siguientes archivos no pudieron ser convertidos:")
            for filename, error in failed_files:
                logging.warning(f"  - Archivo: {filename} | Causa: {error}")

        logging.info("Proceso de conversión a Markdown finalizado.")

    except Exception as e:
        logging.critical(f"Ocurrió un error fatal durante la orquestación de la conversión. Causa: {e}", exc_info=True)
        raise