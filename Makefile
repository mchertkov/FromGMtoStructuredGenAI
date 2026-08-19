.PHONY: install validate list run-all

install:
	python -m pip install -r requirements.txt

validate:
	python scripts/validate_notebooks.py

list:
	python scripts/list_notebooks.py

run-all:
	python scripts/execute_notebooks.py --all
