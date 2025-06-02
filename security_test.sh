#!/bin/bash
set -e  # Detiene el script ante cualquier error

# Análisis estático
echo "🔍 Ejecutando Bandit..."
bandit -r app/ -ll

# Dependencias vulnerables
echo "🔍 Escaneo con Safety..."
pip install safety
safety check --full-report

# Prueba de endpoints (opcional)
echo "✅ Tests de seguridad completados"
