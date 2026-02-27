#!/bin/bash

# --- Script para diagnosticar múltiples URLs ---

# Configura las credenciales para que el script de diagnóstico pueda iniciar sesión
export PORTAL_USER="Userguide"
export PORTAL_PASS="H.eros2025"

# Lista de URLs a probar (extraídas de tu log de errores)
URLS_TO_TEST=(
  "https://portal.move-wifi.com/guide/user_guide/location_management/location_mode/floor_plan.html"
  "https://portal.move-wifi.com/guide/release_notes/2022/2022_09_16.html"
  "https://portal.move-wifi.com/guide/device_configuration/terabee.html"
  "https://portal.move-wifi.com/guide/use_cases/reflect_the_structure_of_your_business.html"
)

# Itera sobre la lista y ejecuta el diagnóstico para cada URL
for url in "${URLS_TO_TEST[@]}"; do
  echo "========================================================================"
  python diagnose_url.py "$url"
  echo "========================================================================"
  echo ""
done