#!/usr/bin/env bash
# 开发环境启动（Linux / macOS / WSL）
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

if [ ! -x .venv/bin/python ]; then
  echo "未找到 .venv，正在创建虚拟环境..."
  python3 -m venv .venv
  .venv/bin/python -m pip install -U pip
  .venv/bin/python -m pip install -r backend/requirements.txt
fi

if [ ! -f data/app.db ]; then
  echo "首次启动，写入种子数据..."
  .venv/bin/python scripts/seed.py
fi

exec .venv/bin/python -m uvicorn app.main:app --app-dir backend --reload --port 8000
