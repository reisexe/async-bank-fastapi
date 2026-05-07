#!/usr/bin/env bash

# Encerra o script imediatamente se algum comando falhar
set -e

# 1. Roda as migrações do banco de dados (Alembic)
# Usamos 'python -m' para garantir que ele use o binário do ambiente virtual
echo "Aplicando migrações do banco de dados..."
python -m alembic upgrade head

# 2. Inicia a aplicação com Uvicorn
# Importante: host 0.0.0.0 e a porta vinda da variável de ambiente do Render
echo "Iniciando o servidor..."
uvicorn main:app --host 0.0.0.0 --port ${PORT:-10000}