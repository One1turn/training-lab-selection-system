.PHONY: install seed run test lint demo clean

PY ?= .venv/Scripts/python.exe
ifeq ($(OS),Windows_NT)
PY := .venv\\Scripts\\python.exe
endif

install:
	python -m venv .venv
	$(PY) -m pip install -U pip
	$(PY) -m pip install -r backend/requirements.txt

seed:
	$(PY) scripts/seed.py

run:
	$(PY) -m uvicorn app.main:app --app-dir backend --reload --port 8000

test:
	$(PY) -m pytest backend/tests -q

lint:
	$(PY) -m ruff check backend/app backend/tests scripts

demo:
	$(PY) scripts/demo_flow.py

clean:
	rm -rf backend/app/__pycache__ backend/tests/__pycache__ .pytest_cache .ruff_cache
