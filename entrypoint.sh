#!/bin/sh
# entrypoint.sh (Versión Corregida con python -m)

# Llamamos a gunicorn como un módulo de python para evitar problemas de PATH
exec python3 -m gunicorn --bind "0.0.0.0:$PORT" --workers 1 --threads 8 --timeout 0 api:app