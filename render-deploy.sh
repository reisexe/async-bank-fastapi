#!/usr/bin/env bash

# Encerra o script se algo der erro
set -e

# Tenta usar python3, se não existir, usa python
PYTHON_BIN=$(command -v python3 || command -v python)

echo "Aplicando migrações do banco de dados usando $PYTHON_BIN..."
$PYTHON_BIN -m alembic upgrade head

echo "Iniciando o servidor..."
uvicorn main:app --host 0.0.0.0 --port ${PORT:-10000}