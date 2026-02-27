# src/ai_model.py
import logging
from openai import OpenAI
import config

client = OpenAI()
# En src/ai_model.py

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
        completion = client.chat.completions.create(
            model=config.AI_MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"CONTEXTO:\n{contexto}\n\n---\n\nPREGUNTA:\n{pregunta}"}
            ],
            temperature=0.3,
            max_tokens=config.AI_GENERATION_CONFIG.get("max_tokens", 1024)
        )
        return completion.choices[0].message.content
    except Exception as e:
        logging.error(f"Error al generar respuesta de OpenAI: {e}", exc_info=True)
        return "Ha ocurrido un problema al contactar el servicio de IA."