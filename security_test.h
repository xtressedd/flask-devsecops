#!/bin/bash
# Análisis estático con Bandit
bandit -r app/

# Escaneo de dependencias vulnerables
pip install safety
safety check
