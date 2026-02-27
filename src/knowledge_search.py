# src/knowledge_search.py (Optimizado con FAISS)
import json
import logging
import os
import numpy as np
import faiss
import google.generativeai as genai
import config

# Configurando Gemini con la API Key obtenida (asegúrese de que GEMINI_API_KEY esté en su .env)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
class KnowledgeSearch:
    def __init__(self):
        self.index = None
        self.content_store = None
        self._load_optimized_knowledge_base()

    def _load_optimized_knowledge_base(self):
        """Carga el índice FAISS y el almacén de contenido de texto."""
        try:
            faiss_index_path = os.path.join(config.KNOWLEDGE_BASE_DIR, "kb.index")
            content_path = os.path.join(config.KNOWLEDGE_BASE_DIR, "kb_content.json")

            logging.info(f"Cargando índice FAISS desde: {faiss_index_path}")
            if not os.path.exists(faiss_index_path):
                raise FileNotFoundError(f"¡FATAL! No se encontró el índice '{faiss_index_path}'. Ejecuta create_faiss_index.py primero.")
            self.index = faiss.read_index(faiss_index_path)

            logging.info(f"Cargando contenido desde: {content_path}")
            if not os.path.exists(content_path):
                raise FileNotFoundError(f"¡FATAL! No se encontró el archivo de contenido '{content_path}'.")
            with open(content_path, 'r', encoding='utf-8') as f:
                self.content_store = json.load(f)

            logging.info(f"Base de conocimiento optimizada cargada. {self.index.ntotal} vectores listos para búsqueda.")

        except Exception as e:
            logging.critical(f"¡FATAL! No se pudo cargar la base de conocimiento optimizada. Error: {e}")
            raise

    def find_relevant_chunks(self, query: str, top_k: int = 3):
        """Encuentra los fragmentos más relevantes usando el índice FAISS."""
        try:
            # Obtener embedding del query usando Gemini
            response = genai.embed_content(
                model="models/text-embedding-004",
                content=query,
                task_type="retrieval_query",
            )
            query_vector = np.array(response['embedding'], dtype='float32')
            query_vector = np.expand_dims(query_vector, axis=0) # Faiss espera un array 2D

            # Realizar la búsqueda en el índice FAISS
            distances, indices = self.index.search(query_vector, top_k)

            if indices.size == 0:
                return "No se encontró información relevante."

            # Construir el contexto con los resultados
            context_parts = []
            for i in indices[0]:
                if i != -1 and i < len(self.content_store):
                    item = self.content_store[i]
                    context_str = f"Fuente: {item.get('source')}\nContenido: {item.get('content')}"
                    if item.get('image_urls'):
                        context_str += f"\nImage URLs: {item.get('image_urls')}"
                    if item.get('video_urls'):
                        context_str += f"\nVideo URLs: {item.get('video_urls')}"
                    context_parts.append(context_str)
            
            return "\n\n---\n\n".join(context_parts) if context_parts else "No se encontró información relevante."
        except Exception as e:
            logging.error(f"Error durante la búsqueda de similitud: {e}", exc_info=True)
            return "Error al procesar la búsqueda de conocimiento."
