SHELL := /bin/bash

.PHONY: run

# run django server
run:
	python manage.py runserver
# delete build elements
clean-pyc:
	@find . -type d -name "__pycache__" -not -path "./.venv/*" -exec rm -rf {} +
