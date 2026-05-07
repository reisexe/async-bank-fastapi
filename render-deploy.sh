#!/usr/bin/env bash
set -e

# O Render instala o binário do poetry aqui
POETRY_BIN="/opt/render/project/poetry/bin/poetry"

echo "Aplicando migrações do banco de dados com Poetry..."
$POETRY_BIN run alembic upgrade head

echo "Iniciando o servidor..."
# Usando o caminho src.main:app que confirmamos antes
$POETRY_BIN run uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-10000}