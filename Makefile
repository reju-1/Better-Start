# Define virtual environment paths
PYTHON := .venv/bin/python
UVICORN := .venv/bin/uvicorn
APP_MODULE := src.main:app

# Default target
.DEFAULT_GOAL := help


run:  ## Run FastAPI server (reload for development)
	$(UVICORN) $(APP_MODULE) --reload


clean:  ## Clean Python cache and temporary files
	find src/ -type d -name '__pycache__' -exec rm -r {} + -o -name '*.pyc' -delete -o -name '*.pyo' -delete


install:  ## Install dependencies from requirements.txt using virtual env
	$(PYTHON) -m pip install -r requirements.txt


help:  ## Show all available targets
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'
