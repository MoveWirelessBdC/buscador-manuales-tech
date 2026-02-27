import logging
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

from src.knowledge_search import KnowledgeSearch
from src.ai_model import generate_response
import config

# Módulos para integración asíncrona
import asyncio
from src.marcas.ezviz import obtener_pdf_ezviz

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app = Flask(__name__)
knowledge_searcher = None

try:
    logging.info("Iniciando API y conectando a servicios...")
    knowledge_searcher = KnowledgeSearch()
    logging.info("¡API lista para recibir consultas!")
except Exception as e:
    logging.critical(f"NO SE PUDO INICIAR LA API: {e}", exc_info=True)

@app.route('/')
def index():
    """Sirve la interfaz de chat web."""
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def handle_query():
    """Recibe preguntas y devuelve respuestas de la IA."""
    if knowledge_searcher is None:
        return jsonify({"error": "El buscador de conocimiento no está inicializado."}), 503
    
    data = request.get_json()
    if not data or 'pregunta' not in data:
        return jsonify({"error": "La petición debe contener una 'pregunta'"}), 400
        
    pregunta = data.get('pregunta', '').strip()
    if not pregunta:
        return jsonify({"error": "La 'pregunta' no puede estar vacía"}), 400
        
    contexto = knowledge_searcher.find_relevant_chunks(pregunta)
    respuesta_ia = generate_response(contexto, pregunta)
    
    return jsonify({"respuesta": respuesta_ia})

@app.route('/get_manual', methods=['POST'])
def handle_get_manual():
    """Busca el manual PDF de un modelo en la web usando Playwright."""
    data = request.get_json()
    if not data or 'modelo' not in data:
        return jsonify({"status": "error", "message": "La petición debe contener el 'modelo' del equipo a buscar."}), 400
        
    modelo = data.get('modelo', '').strip()
    if not modelo:
        return jsonify({"status": "error", "message": "El 'modelo' no puede estar vacío."}), 400
    
    # Flask es síncrono, usamos asyncio.run para ejecutar la función asíncrona de Playwright
    try:
        resultado = asyncio.run(obtener_pdf_ezviz(modelo))
        return jsonify(resultado)
    except Exception as e:
        logging.error(f"Excepción al ejecutar Playwright desde Flask: {e}")
        return jsonify({"status": "error", "message": "Fallo al ejecutar el motor de búsqueda interno."}), 500

if __name__ == '__main__':
    # El modo debug debe estar en False para cualquier uso que no sea desarrollo local.
    app.run(host='0.0.0.0', port=5001, debug=False)