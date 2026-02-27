# verify_openai.py
import os
from openai import OpenAI

print("--- Iniciando verificación de la clave de API de OpenAI ---")

try:
    # Intenta inicializar el cliente. Esto leerá la variable de entorno.
    client = OpenAI()
    
    # Realiza una llamada simple y de bajo costo a la API para listar modelos
    print("Clave encontrada. Intentando conectar con la API de OpenAI...")
    client.models.list()
    
    print("\n--- ✅ ÉXITO ---")
    print("Tu clave de API es válida y la conexión con OpenAI funciona correctamente.")
    
except Exception as e:
    print("\n--- ❌ FALLO ---")
    print("Hubo un error al verificar tu clave de API.")
    print(f"Detalle del error: {e}")