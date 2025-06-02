# Build stage
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.9-slim
WORKDIR /app

RUN useradd -m appuser && \
    chown -R appuser:appuser /app

# Copia solo las dependencias necesarias
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia la aplicación
COPY . .

USER appuser

ENV FLASK_APP=app.app
ENV FLASK_ENV=production

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "app.app:application"]
