import os
import json
from dotenv import load_dotenv
from pinecone import Pinecone

# Cargar variables de entorno
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "manuales-tech")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE", "ezviz_knowledge")

def verificar():
    if not PINECONE_API_KEY:
        print("❌ Error: PINECONE_API_KEY no encontrada en .env")
        return

    print(f"🔍 Conectando a Pinecone (Index: {PINECONE_INDEX_NAME}, Namespace: {PINECONE_NAMESPACE})...")
    
    try:
        pc = Pinecone(api_key=PINECONE_API_KEY)
        index = pc.Index(PINECONE_INDEX_NAME)
        
        # Consultar estadísticas del namespace
        stats = index.describe_index_stats()
        ns_stats = stats.get('namespaces', {}).get(PINECONE_NAMESPACE, {})
        vector_count = ns_stats.get('vector_count', 0)
        
        print(f"✅ Conexión exitosa. Vectores encontrados en este namespace: {vector_count}")
        
        if vector_count == 0:
            print("⚠️ El namespace está vacío. Asegúrate de haber ejecutado el ingestor.")
            return

        # Realizar una consulta aleatoria (dummy vector de ceros para traer los primeros resultados)
        # Nota: La dimensión debe coincidir con text-embedding-004 (768)
        dummy_vector = [0.0] * 768
        
        results = index.query(
            vector=dummy_vector,
            top_k=2,
            include_metadata=True,
            namespace=PINECONE_NAMESPACE
        )
        
        print("\n--- 📋 REVISIÓN DE METADATOS (2 Vectores Muestra) ---")
        for i, match in enumerate(results.get('matches', [])):
            metadata = match.get('metadata', {})
            print(f"\n[Vector {i+1}] ID: {match['id']}")
            print(f"📌 Modelo Comercial: {metadata.get('modelo_comercial', 'N/A')}")
            print(f"📂 Fuente: {metadata.get('fuente', 'N/A')}")
            print(f"🔗 File Path: {metadata.get('file_path', 'N/A')}")
            print(f"📝 Texto Original (Fragmento):")
            print("-" * 40)
            texto = metadata.get('texto_original', 'Sin texto')
            print(texto[:300] + ("..." if len(texto) > 300 else ""))
            print("-" * 40)
            
        print("\n✅ Verificación completada.")
        
    except Exception as e:
        print(f"❌ Error durante la verificación: {e}")

if __name__ == "__main__":
    verificar()
