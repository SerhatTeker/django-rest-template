# delete build elements
clean:
	find . -name "*.pyc" -not -path "./.venv/*" -exec rm -rf {} \;
	find . -name __pycache__ -not -path "./.venv/*" -exec rm -rf {} \;
