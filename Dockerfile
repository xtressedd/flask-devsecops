FROM python:3.9-slim

# Configuración de seguridad (TODO en un solo RUN para reducir capas)
RUN useradd -m appuser && \
    apt-get update && \
    apt-get install -y --no-install-recommends libssl-dev curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia requirements e instala dependencias
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia la aplicación
COPY ./app .

# Permisos y usuario
RUN chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:5000/ || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
