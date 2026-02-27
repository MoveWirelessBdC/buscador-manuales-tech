import os, json, logging, uuid, time
from openai import OpenAI
import config
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

load_dotenv()
client = OpenAI()

def get_openai_embedding(text_chunk: str):
    try:
        sanitized_chunk = text_chunk.replace("\n", " ").strip().encode('ascii', 'ignore').decode('utf-8')
        if not sanitized_chunk: return None
        response = client.embeddings.create(input=[sanitized_chunk], model=config.OPENAI_EMBEDDING_MODEL)
        return response.data[0].embedding
    except Exception as e:
        logging.error(f"Fallo al generar embedding: {e}")
        return None

def recursive_character_split(text, chunk_size, chunk_overlap):
    if len(text) <= chunk_size: return [text]
    chunks, start_index = [], 0
    while start_index < len(text):
        end_index = start_index + chunk_size
        chunks.append(text[start_index:end_index])
        start_index += chunk_size - chunk_overlap
    return chunks

import os, json, logging, uuid, time, re
from openai import OpenAI

def process_source_file(file_path, file_type):
    filename = os.path.basename(file_path)
    try:
        with open(file_path, 'r', encoding='utf-8') as f: content = f.read()
        text_chunks = recursive_character_split(content, config.CHUNK_SIZE, config.CHUNK_OVERLAP)
        knowledge_chunks = []
        for i, chunk_text in enumerate(text_chunks):
            embedding_vector = get_openai_embedding(chunk_text.strip())
            if embedding_vector:
                image_urls = re.findall(r'<img src="(.*?)"', chunk_text)
                video_urls = re.findall(r'<iframe src="(.*?)"', chunk_text)
                knowledge_chunks.append({
                    "id": str(uuid.uuid4()), "source": filename, "title": f"{os.path.splitext(filename)[0]} - Parte {i+1}",
                    "content": chunk_text.strip(), "type": file_type, "embedding": embedding_vector,
                    "image_urls": image_urls, "video_urls": video_urls
                })
        return knowledge_chunks
    except Exception as e:
        logging.error(f"Fallo crítico al procesar el archivo {filename}.", exc_info=True)
        return []

def run():
    logging.info("Iniciando fragmentación y guardando en archivo JSON local...")
    source_files = []
    if os.path.exists(config.MARKDOWN_DIR):
        for f in os.listdir(config.MARKDOWN_DIR):
            if f.endswith(".md"): source_files.append((os.path.join(config.MARKDOWN_DIR, f), "manual"))
    if not source_files:
        logging.warning("No se encontraron archivos .md para fragmentar.")
        return

    all_chunks = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(process_source_file, fp, ft): fp for fp, ft in source_files}
        for future in as_completed(futures):
            all_chunks.extend(future.result())
    
    os.makedirs(config.KNOWLEDGE_BASE_DIR, exist_ok=True)
    with open(config.KB_JSON_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)
    logging.info(f"--- Base de conocimiento local creada. Total de fragmentos: {len(all_chunks)} ---")