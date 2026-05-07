#!/usr/bin/env bash
set -e

/opt/render/project/python/bin/python3 -m alembic upgrade head
/opt/render/project/python/bin/python3 -m uvicorn src.main:app --host 0.0.0.0 --port $PORT