# Makefile for Advanced Multi-Modal Computational Analytics Platform

.PHONY: help install install-dev clean test lint format run docker-build docker-run docs

# Default target
help:
	@echo "🔬 Advanced Multi-Modal Computational Analytics Platform"
	@echo ""
	@echo "Available commands:"
	@echo "  install      Install the package and dependencies"
	@echo "  install-dev  Install development dependencies"
	@echo "  clean        Clean up temporary files and caches"
	@echo "  test         Run the test suite"
	@echo "  lint         Run code linting"
	@echo "  format       Format code with black"
	@echo "  run          Start the development server"
	@echo "  docker-build Build Docker image"
	@echo "  docker-run   Run in Docker container"
	@echo "  docs         Generate documentation"

# Installation
install:
	@echo "📦 Installing package and dependencies..."
	pip install -e .

install-dev: install
	@echo "🛠️ Installing development dependencies..."
	pip install -e .[dev,docs]
	pre-commit install

# Cleanup
clean:
	@echo "🧹 Cleaning up temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type f -name "*.pyd" -delete 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -name "._*" -delete 2>/dev/null || true
	find . -name ".DS_Store" -delete 2>/dev/null || true

# Testing
test:
	@echo "🧪 Running test suite..."
	python -m pytest tests/ -v --cov=src --cov-report=term-missing

# Code quality
lint:
	@echo "🔍 Running code linting..."
	flake8 src/ tests/ app.py
	mypy src/ app.py --ignore-missing-imports

format:
	@echo "✨ Formatting code..."
	black src/ tests/ app.py
	isort src/ tests/ app.py

# Development server
run:
	@echo "🚀 Starting development server..."
	python app.py

# Docker
docker-build:
	@echo "🐳 Building Docker image..."
	docker build -t multimodal-analytics-platform .

docker-run: docker-build
	@echo "🐳 Running Docker container..."
	docker run -p 5000:5000 multimodal-analytics-platform

# Documentation
docs:
	@echo "📚 Generating documentation..."
	cd docs && make html

# Quality checks
check: lint test
	@echo "✅ All quality checks passed!"

# Full development setup
setup: install-dev
	@echo "🎉 Development environment ready!"
	@echo "Run 'make run' to start the server"
