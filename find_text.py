# find_text.py (Versión Optimizada)
import os
import sys

if len(sys.argv) < 2:
    print("Uso: python3 find_text.py <palabra_a_buscar>")
    sys.exit(1)

search_term = sys.argv[1]
search_dir = '.' # Directorio actual

print(f"Buscando la palabra '{search_term}' en los archivos de código y configuración...")
print("-" * 50)

found = False
for root, _, files in os.walk(search_dir):
    if '.git' in root or '.venv' in root or '__pycache__' in root:
        continue # Ignorar carpetas comunes

    for file in files:
        # ¡CAMBIO CLAVE! Ignoramos el archivo knowledge_base.json
        if file == "knowledge_base.json":
            continue

        if file.endswith(('.py', '.txt', '.sh', 'Dockerfile', '.json', '.env')):
            try:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_num, line in enumerate(f, 1):
                        if search_term in line:
                            print(f"Encontrado en: {file_path} (Línea: {line_num})")
                            print(f"  -> {line.strip()}")
                            found = True
            except Exception:
                continue
    
if not found:
    print(f"No se encontró la palabra '{search_term}' en ningún archivo del proyecto.")
print("-" * 50)