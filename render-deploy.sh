#!/usr/bin/env bash

# Para o script se der erro
set -e

# Garante que o Python encontre a pasta 'src' e a raiz
export PYTHONPATH=$PYTHONPATH:$(pwd)

echo "Aplicando migrações do banco de dados..."
# Usamos 'python' (sem o 3) porque o Render mapeia esse comando 
# para o ambiente virtual onde ele instalou o seu requirements.txt
python -m alembic upgrade head

echo "Iniciando o servidor..."
# Ajustado para src.main:app porque seu main.py está dentro da pasta src
python -m uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-10000}