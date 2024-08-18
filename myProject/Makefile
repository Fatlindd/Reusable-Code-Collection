# Install the project dependencies from requirements.txt
install:
	pip install -r requirements.txt  # Indented with a tab

update:
	pip install --upgrade -r requirements.txt

# Run the Python script
run:
	python3 main.py  # Indented with a tab

# Clean up any unnecessary files
clean:
	rm -rf __pycache__/  # Indented with a tab

# Run tests
test:
	pytest  # Indented with a tab

# Format the code
format:
	black .  # Indented with a tab

# Lint the code
lint:
	pylint *.py  # Indented with a tab

# Build the project
build:
	python setup.py build  # Indented with a tab

# Help command
help:
	@echo "Available targets:"  # Indented with a tab
	@echo "  install - Install dependencies"  # Indented with a tab
	@echo "  update - Update dependencies"  # Indented with a tab
	@echo "  run - Run the application"  # Indented with a tab
	@echo "  clean - Clean up files"  # Indented with a tab
	@echo "  test - Run tests"  # Indented with a tab
	@echo "  format - Format code"  # Indented with a tab
	@echo "  lint - Lint code"  # Indented with a tab
	@echo "  build - Build the project"  # Indented with a tab
	@echo "  help - Show this help message"  # Indented with a tab
