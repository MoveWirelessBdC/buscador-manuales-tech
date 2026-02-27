# test_server.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡El servidor de prueba Flask funciona!"

if __name__ == '__main__':
    print("--- Iniciando servidor de prueba en http://127.0.0.1:5001 ---")
    print("--- Si esto funciona, la terminal debe quedarse 'pegada' aquí. ---")
    print("--- Presiona Ctrl+C para detenerlo. ---")
    app.run(host='0.0.0.0', port=5001)