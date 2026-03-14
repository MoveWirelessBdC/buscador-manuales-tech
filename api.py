import logging
from quart import Quart, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()


from src.marcas.ezviz import obtener_pdf_ezviz

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app = Quart(__name__)


@app.route('/')
def index():
    """Sirve la interfaz de chat web."""
    return render_template('index.html')

@app.route('/get_manual', methods=['POST'])
async def handle_get_manual():
    """Busca el manual PDF de un modelo en la web usando Playwright."""
    data = await request.get_json()
    if not data or 'modelo' not in data:
        return jsonify({"status": "error", "message": "La petición debe contener el 'modelo' del equipo a buscar."}), 400
        
    modelo = data.get('modelo', '').strip()
    if not modelo:
        return jsonify({"status": "error", "message": "El 'modelo' no puede estar vacío."}), 400
    
    try:
        resultado = await obtener_pdf_ezviz(modelo)
        return jsonify(resultado)
    except Exception as e:
        logging.error(f"Excepción al ejecutar Playwright desde Flask: {e}")
        return jsonify({"status": "error", "message": "Fallo al ejecutar el motor de búsqueda interno."}), 500

if __name__ == '__main__':
    # El modo debug debe estar en False para cualquier uso que no sea desarrollo local.
    app.run(host='0.0.0.0', port=5001, debug=False)