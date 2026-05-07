#!/usr/bin/env bash
set -e

# Tenta encontrar se o comando é python ou python3
if command -v python3 >/dev/null 2>&1; then
    PYTHON_EXE=$(command -v python3)
elif command -v python >/dev/null 2>&1; then
    PYTHON_EXE=$(command -v python)
else
    echo "Erro crítico: Python não encontrado no ambiente de deploy."
    exit 1
fi

echo "Usando executável: $PYTHON_EXE"
export PYTHONPATH=$PYTHONPATH:$(pwd)

echo "Aplicando migrações do banco de dados..."
$PYTHON_EXE -m alembic upgrade head

echo "Iniciando o servidor..."
# Usando src.main:app porque seu main.py está na pasta src
$PYTHON_EXE -m uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-10000}