FROM python:3.11-slim

# Evitar que Python escriba archivos .pyc y forzar que la salida no tenga buffer
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Instalar dependencias del sistema requeridas por Playwright
RUN apt-get update && apt-get install -y \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libgbm1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instalar los navegadores de Playwright (solo Chromium) y sus dependencias (en caso de que falte alguna)
RUN playwright install chromium --with-deps

COPY . .

# Exponer el puerto configurado por Cloud Run
EXPOSE 8080

# Usar gunicorn con workers compatibles con asyncio y uvicorn
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 --timeout 0 api:app