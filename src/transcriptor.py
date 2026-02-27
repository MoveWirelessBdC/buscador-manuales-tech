# src/transcriptor.py
import os
import logging
import uuid
import time
from google.cloud import speech, storage
import yt_dlp
import config

def initialize_vertexai():
    """Inicializa Vertex AI solo si es necesario."""
    try:
        import vertexai
        # Estas variables son necesarias para el pipeline de datos, no para la API en vivo.
        gcp_project_id = getattr(config, 'GCP_PROJECT_ID', None)
        gcp_region = getattr(config, 'GCP_REGION', None)
        if gcp_project_id and gcp_region:
            vertexai.init(project=gcp_project_id, location=gcp_region)
        else:
            logging.warning("GCP_PROJECT_ID o GCP_REGION no están configurados. La funcionalidad de Vertex AI estará deshabilitada.")
    except ImportError:
        logging.warning("Vertex AI SDK no encontrado.")
    except Exception as e:
        logging.error(f"Error al inicializar Vertex AI: {e}")

# No se inicializa aquí, se hará dentro de las funciones si es necesario.

def upload_to_gcs(local_file_path: str, destination_blob_name: str) -> str:
    """Sube un archivo a un bucket de GCS."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(config.GCS_BUCKET_NAME)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(local_file_path)
    gcs_uri = f"gs://{config.GCS_BUCKET_NAME}/{destination_blob_name}"
    logging.info(f"Archivo subido a GCS: {gcs_uri}")
    return gcs_uri

def delete_from_gcs(blob_name: str):
    """Elimina un archivo de un bucket de GCS."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(config.GCS_BUCKET_NAME)
        blob = bucket.blob(blob_name)
        if blob.exists():
            blob.delete()
            logging.info(f"Archivo de GCS limpiado: {blob_name}")
    except Exception as e:
        logging.error(f"No se pudo eliminar el blob {blob_name} de GCS. Causa: {e}")

def transcribe_single_video(url: str):
    safe_video_id = url.replace("https://", "").replace("http://", "").replace("/", "_").replace("?", "_").replace("=", "_").replace("%", "")

    temp_filename_base = os.path.join(config.TEMP_DIR, f"{safe_video_id}_{uuid.uuid4()}")
    local_audio_file = None
    gcs_blob_name = f"audio-transcripts/{safe_video_id}.wav"

    try:
        logging.info(f"Descargando y convirtiendo para video ID: {safe_video_id}")
        ydl_opts = {
            'format': 'bestaudio/best', 'outtmpl': temp_filename_base,
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'}],
            'postprocessor_args': ['-ac', '1', '-ar', '16000'],
            'quiet': True, 'no_warnings': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([url])
        local_audio_file = temp_filename_base + ".wav"

        gcs_uri = upload_to_gcs(local_audio_file, gcs_blob_name)

        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(uri=gcs_uri)
        recognition_config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code=config.TRANSCRIPTION_LANG,
            enable_automatic_punctuation=True
        )
        operation = client.long_running_recognize(config=recognition_config, audio=audio)
        logging.info(f"Trabajo de transcripción enviado para {safe_video_id}. Esperando resultado...")
        response = operation.result(timeout=1800)

        transcript = " ".join([result.alternatives[0].transcript for result in response.results])
        if not transcript:
            logging.warning(f"La transcripción para {safe_video_id} resultó vacía.")
            return False

        transcript_path = os.path.join(config.TRANSCRIPTS_DIR, f"{safe_video_id}.txt")
        with open(transcript_path, 'w', encoding='utf-8') as f: f.write(transcript)
        return True

    except Exception as e:
        logging.error(f"Fallo al procesar {safe_video_id}. Causa: {e}", exc_info=False)
        return False
    finally:
        if local_audio_file and os.path.exists(local_audio_file):
            os.remove(local_audio_file)
        delete_from_gcs(gcs_blob_name)

def run():
    initialize_vertexai() # Se llama solo cuando se ejecuta este paso
    logging.info("Iniciando proceso de transcripción (modo GCS secuencial)...")
    os.makedirs(config.TRANSCRIPTS_DIR, exist_ok=True); os.makedirs(config.TEMP_DIR, exist_ok=True)
    try:
        with open(config.VIDEO_URLS_FILE, 'r') as f: video_urls = [l.strip() for l in f if l.strip()]
    except FileNotFoundError:
        logging.warning(f"No se encontró '{config.VIDEO_URLS_FILE}'. Saltando paso."); return
    if not video_urls: logging.warning("No hay URLs de video para procesar."); return
    
    urls_to_process = []
    for url in video_urls:
        safe_vid_id = url.replace("https://", "").replace("http://", "").replace("/", "_").replace("?", "_").replace("=", "_").replace("%", "")
        if not os.path.exists(os.path.join(config.TRANSCRIPTS_DIR, f"{safe_vid_id}.txt")):
            urls_to_process.append(url)
    if not urls_to_process: logging.info("No hay videos nuevos para transcribir."); return

    success_count, failure_count = 0, 0
    for i, url in enumerate(urls_to_process):
        logging.info(f"--- Procesando video {i+1} de {len(urls_to_process)} ---")
        if transcribe_single_video(url): success_count += 1
        else: failure_count += 1
        time.sleep(1)

    logging.info(f"--- Reporte de Transcripción ---")
    logging.info(f"Videos transcritos exitosamente: {success_count}")
    logging.info(f"Videos fallidos: {failure_count}")
    logging.info("Proceso de transcripción finalizado.")
