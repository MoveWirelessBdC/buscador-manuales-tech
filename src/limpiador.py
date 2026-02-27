# src/limpiador.py (Versión 2 - Paralelo y Configurable)
import os
import logging
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor, as_completed
import config

def clean_html_file(file_path):
    """
    Toma la ruta de un archivo HTML, lo limpia según la configuración y lo guarda.
    Diseñada para ser ejecutada en un proceso paralelo.
    """
    filename = os.path.basename(file_path)
    try:
        # Leer el contenido del archivo de entrada
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_html = f.read()

        # Usar BeautifulSoup para analizar y limpiar el HTML
        soup = BeautifulSoup(raw_html, 'html.parser')

        # Eliminar etiquetas no deseadas (definidas en config.py)
        for tag_name in config.HTML_TAGS_TO_REMOVE:
            for tag in soup.find_all(tag_name):
                tag.decompose()

        cleaned_html = str(soup)

        # Escribir el contenido limpio en el directorio de salida
        output_path = os.path.join(config.HTML_CLEANED_DIR, filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_html)

        return filename, "Éxito"
    except Exception as e:
        logging.error(f"No se pudo limpiar el archivo '{filename}'. Causa: {e}", exc_info=False)
        return filename, str(e)

def run():
    """
    Punto de entrada que orquesta la limpieza de archivos HTML en paralelo.
    """
    logging.info("Iniciando proceso de limpieza de archivos HTML...")

    if not os.path.exists(config.HTML_CLEANED_DIR):
        os.makedirs(config.HTML_CLEANED_DIR)
        logging.info(f"Directorio de salida '{config.HTML_CLEANED_DIR}' creado.")

    try:
        raw_files = [os.path.join(config.HTML_RAW_DIR, f) 
                     for f in os.listdir(config.HTML_RAW_DIR) if f.endswith(".html")]

        if not raw_files:
            logging.warning("No se encontraron archivos HTML en el directorio de entrada. Saltando paso de limpieza.")
            return

        logging.info(f"Se encontraron {len(raw_files)} archivos para limpiar. Iniciando procesamiento en paralelo...")

        success_count = 0
        failure_count = 0
        failed_files = []

        # Usar un pool de procesos para ejecutar las tareas de limpieza en paralelo
        with ProcessPoolExecutor() as executor:
            # Enviar cada tarea de limpieza al pool
            future_to_file = {executor.submit(clean_html_file, file_path): file_path for file_path in raw_files}

            # Procesar los resultados a medida que se completan
            for future in as_completed(future_to_file):
                filename, result = future.result()
                if result == "Éxito":
                    success_count += 1
                else:
                    failure_count += 1
                    failed_files.append((filename, result))

        # --- Reporte Final de la Limpieza ---
        logging.info("--- Reporte de Limpieza ---")
        logging.info(f"Archivos limpiados exitosamente: {success_count}")
        logging.info(f"Archivos fallidos: {failure_count}")
        if failure_count > 0:
            logging.warning("Los siguientes archivos no pudieron ser limpiados:")
            for filename, error in failed_files:
                logging.warning(f"  - Archivo: {filename} | Causa: {error}")

        logging.info("Proceso de limpieza finalizado.")

    except Exception as e:
        logging.critical(f"Ocurrió un error fatal durante la orquestación de la limpieza. Causa: {e}", exc_info=True)
        raise