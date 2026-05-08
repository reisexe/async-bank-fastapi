#!/usr/bin/env bash
set -e

POETRY_BIN="/opt/render/project/poetry/bin/poetry"

echo "Aplicando migrações do banco de dados com Poetry..."
$POETRY_BIN run alembic upgrade head

echo "Iniciando o servidor..."

$POETRY_BIN run uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-10000}