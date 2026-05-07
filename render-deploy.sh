#!/usr/bin/env bash

# Para o script se der erro
set -e

# Garante que o Python procure bibliotecas na pasta local onde o Render instalou
export PYTHONPATH=$PYTHONPATH:.

echo "Aplicando migrações do banco de dados..."
# Usamos 'python' ou o binário do ambiente virtual
# O comando abaixo tenta rodar o alembic que foi instalado via pip
alembic upgrade head

echo "Iniciando o servidor..."
uvicorn main:app --host 0.0.0.0 --port ${PORT:-10000}