# debug_search.py (Final Corrected Version)
import sys
import os
import logging
from dotenv import load_dotenv

# Add the project root to the Python path to find the 'src' module
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.knowledge_search import KnowledgeSearch
from src.ai_model import generate_response

load_dotenv()
logging.basicConfig(level=logging.INFO)

def run_debug(query: str):
    """
    Runs a full end-to-end test: search for context and generate a response.
    """
    if not query:
        print("Please provide a question to search for.")
        return

    print(f"--- Running full diagnostic for question ---")
    print(f"Question: \"{query}\"")
    print("-" * 50)

    try:
        print("Initializing knowledge search...")
        searcher = KnowledgeSearch()
        
        print("\nStep 1: Finding relevant context from Pinecone...")
        contexto = searcher.find_relevant_chunks(query)
        
        if "ERROR" in contexto or "No se encontró" in contexto:
            print(f"\nContext search failed or found no results: {contexto}")
            return
            
        print("--- Context Found ---")
        print(contexto)
        print("-" * 50)
        
        print("\nStep 2: Sending context and question to AI for final answer...")
        respuesta_ia = generate_response(contexto, query)
        
        print("\n--- Final AI Response ---")
        print(respuesta_ia)
        print("-" * 50)

    except Exception as e:
        print(f"\nAn error occurred during the process: {e}")

if __name__ == "__main__":
    user_question = " ".join(sys.argv[1:])
    run_debug(user_question)