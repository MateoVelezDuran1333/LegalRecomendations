# Imagen base ligera
FROM python:3.10-slim-bullseye

# Evitar archivos pyc y buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias necesarias para spaCy y nltk
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Crear el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . /app

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Descargar modelos necesarios de spaCy y nltk
RUN python -m spacy download en_core_web_sm --no-cache-dir && \
    python -m nltk.downloader stopwords

# Exponer el puerto
EXPOSE 8000

# Comando de arranque
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
