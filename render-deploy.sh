#!/usr/bin/env bash

# Para o script se der erro
set -e

echo "Aplicando migrações do banco de dados..."
# Usamos apenas 'python' sem o caminho /usr/bin/
# Isso garante que ele use o Python do ambiente onde o pip instalou as coisas
python -m alembic upgrade head

echo "Iniciando o servidor..."
uvicorn main:app --host 0.0.0.0 --port ${PORT:-10000}