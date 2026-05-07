#!/usr/bin/env bash

# Para o script se der erro
set -e

echo "Diretório atual: $(pwd)"
echo "Versão do Python:"
python3 --version

echo "Aplicando migrações do banco de dados..."
# Forçando o uso de python3
python3 -m alembic upgrade head

echo "Iniciando o servidor..."
uvicorn main:app --host 0.0.0.0 --port ${PORT:-10000}