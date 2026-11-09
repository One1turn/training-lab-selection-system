# 开发环境启动（Windows PowerShell）
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$python = Join-Path $root '.venv\Scripts\python.exe'

if (-not (Test-Path $python)) {
    Write-Host '未找到 .venv，正在创建虚拟环境...'
    python -m venv (Join-Path $root '.venv')
    & $python -m pip install -U pip
    & $python -m pip install -r (Join-Path $root 'backend\requirements.txt')
}

$env:PYTHONPATH = Join-Path $root 'backend'
if (-not (Test-Path (Join-Path $root 'data\app.db'))) {
    Write-Host '首次启动，写入种子数据...'
    & $python (Join-Path $root 'scripts\seed.py')
}

Write-Host '启动开发服务器: http://127.0.0.1:8000/docs'
& $python -m uvicorn app.main:app --app-dir (Join-Path $root 'backend') --reload --port 8000
