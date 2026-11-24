# Usamos una imagen ligera de Python
FROM python:3.11-slim

# Instalamos FFmpeg y limpiamos el caché para que el contenedor sea más liviano
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero el requirements.txt para aprovechar la caché de Docker
COPY requirements.txt .

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos del proyecto (incluyendo app.py, core/ y cookies.txt)
COPY . .

# Comando para iniciar la aplicación usando Gunicorn en el puerto que asigna Render
CMD gunicorn app:app --bind 0.0.0.0:$PORT