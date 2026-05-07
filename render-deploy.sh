#!/usr/bin/env bash
set -e

which python3
which pip
pip show alembic
python3 -m alembic upgrade head
python3 -m uvicorn src.main:app --host 0.0.0.0 --port $PORT