# main.py
import sys, logging
from dotenv import load_dotenv
load_dotenv()

# Los módulos se importan después de cargar las variables
from src import fragmentador 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Solo necesitamos el fragmentador por ahora
steps = {
    "fragmentador": fragmentador.run
}

def run_pipeline(step_to_run):
    if step_to_run in steps:
        steps[step_to_run]()
    else:
        logging.error(f"Paso '{step_to_run}' no válido. El único paso disponible es 'fragmentador'.")

if __name__ == "__main__":
    step = sys.argv[1] if len(sys.argv) > 1 else "fragmentador"
    run_pipeline(step)