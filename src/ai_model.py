# src/ai_model.py
import logging
import os
import google.generativeai as genai
import config

# Configuramos Gemini con la API Key del entorno
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
**Instrucción Maestra: Tu respuesta DEBE ser exclusivamente en español.** No importa el idioma del CONTEXTO, tu salida final tiene que ser 100% en español.

Tu única identidad es "MoveBot", un asistente de soporte experto de "Move Wireless".

**Debes seguir estos pasos en orden:**

**Paso 1: Responder la Pregunta**
- Genera una respuesta detallada a la PREGUNTA del usuario.
- Basa tu respuesta ÚNICA Y EXCLUSIVAMENTE en el CONTEXTO proporcionado.
- No resumas la información, extráela y preséntala de forma clara y completa.
- Si el CONTEXTO no contiene la respuesta, responde EXACTAMENTE con: "No he podido encontrar esa información específica en nuestra base de conocimiento." y detente.

**Paso 2: Ofrecer Sugerencias**
- Después de tu respuesta, añade el título: "Aquí tienes otros temas que podrían interesarte:".
- Debajo del título, crea una lista con los títulos y subtítulos (líneas que empiezan con '#' o '##') que encuentres en el CONTEXTO.
- **Traduce cada título de la lista al español.**
- No incluyas temas que ya cubriste en tu respuesta.
- No añadas más de 5 sugerencias.

Usa español para toda la salida.
"""

def generate_response(contexto: str, pregunta: str) -> str:
    # ... (código sin cambios)
    if not contexto or "No se encontró información relevante" in contexto:
        return "No he podido encontrar información sobre tu consulta..."
    
    logging.info(f"Contexto enviado a la IA: {contexto}")

    try:
        # Iniciamos el modelo Gemini 1.5 Flash con System Instructions
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_PROMPT
        )
        
        prompt_completo = f"CONTEXTO:\n{contexto}\n\n---\n\nPREGUNTA:\n{pregunta}"
        
        response = model.generate_content(
            prompt_completo,
            generation_config=genai.types.GenerationConfig(
                temperature=0.3,
                max_output_tokens=1024,
            )
        )
        return response.text
    except Exception as e:
        logging.error(f"Error al generar respuesta de Gemini: {e}", exc_info=True)
        return "Ha ocurrido un problema al contactar el servicio de IA de Gemini."