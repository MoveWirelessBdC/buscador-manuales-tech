# create_faiss_index.py
import json
import logging
import os
import numpy as np
import faiss
import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_index():
    """
    Lee la base de conocimiento en formato JSON, extrae los embeddings y el contenido,
    y crea un índice FAISS para los embeddings y un archivo JSON para el contenido.
    """
    try:
        logging.info(f"Cargando base de conocimiento original desde: {config.KB_JSON_FILE_PATH}")
        if not os.path.exists(config.KB_JSON_FILE_PATH):
            raise FileNotFoundError(f"No se encontró el archivo '{config.KB_JSON_FILE_PATH}'. Asegúrate de que el pipeline se haya ejecutado.")

        with open(config.KB_JSON_FILE_PATH, 'r', encoding='utf-8') as f:
            knowledge_base = json.load(f)

        # Validar que la base de conocimiento no esté vacía
        if not knowledge_base:
            logging.warning("La base de conocimiento está vacía. No se creará ningún índice.")
            return

        logging.info("Separando embeddings y contenido de texto...")
        embeddings = [item['embedding'] for item in knowledge_base if 'embedding' in item]
        content_store = [
            {
                "source": item.get('source'), 
                "content": item.get('content'),
                "image_urls": item.get('image_urls', []),
                "video_urls": item.get('video_urls', [])
            } 
            for item in knowledge_base
        ]

        if not embeddings:
            raise ValueError("No se encontraron embeddings en la base de conocimiento.")

        # Convertir a matriz de numpy
        embeddings_matrix = np.array(embeddings, dtype='float32')

        # Crear el índice FAISS
        dimension = embeddings_matrix.shape[1]
        index = faiss.IndexFlatL2(dimension)  # Usando L2 para la distancia
        index = faiss.IndexIDMap(index)
        ids = np.arange(len(knowledge_base)).astype('int64')
        index.add_with_ids(embeddings_matrix, ids)

        # Definir las nuevas rutas desde config
        faiss_index_path = os.path.join(config.KNOWLEDGE_BASE_DIR, "kb.index")
        content_path = os.path.join(config.KNOWLEDGE_BASE_DIR, "kb_content.json")

        logging.info(f"Guardando índice FAISS en: {faiss_index_path}")
        faiss.write_index(index, faiss_index_path)

        logging.info(f"Guardando contenido de texto en: {content_path}")
        with open(content_path, 'w', encoding='utf-8') as f:
            json.dump(content_store, f, ensure_ascii=False, indent=4)

        logging.info(f"¡Proceso completado! Se creó el índice con {index.ntotal} vectores.")

    except Exception as e:
        logging.critical(f"Ocurrió un error al crear el índice FAISS: {e}", exc_info=True)

if __name__ == '__main__':
    create_index()
