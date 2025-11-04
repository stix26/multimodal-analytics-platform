# 📁 Project Structure

This directory contains all the project files organized into logical categories:

## 📂 Directory Structure

```
project/
├── config/                  # Configuration & setup files
│   ├── app.py              # Main Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── pyproject.toml      # Modern Python packaging
│   ├── setup.py            # Legacy packaging
│   ├── Makefile            # Development commands
│   └── .gitignore          # Git ignore rules
├── src/                    # Source code
│   ├── processors/         # ML processing modules
│   ├── utils/              # Mathematical utilities
│   ├── templates/          # Web interface
│   └── static/             # Static assets
├── samples/                # Test data
│   ├── audio/              # Audio samples
│   ├── images/             # Image samples
│   └── metadata/           # JSON configurations
├── docs/                   # Documentation
│   ├── user-guide/         # User documentation
│   └── research/           # Academic documentation
├── tests/                  # Test suite
├── documentation/          # Project policies
│   ├── CHANGELOG.md        # Version history
│   ├── CONTRIBUTING.md     # Contribution guidelines
│   └── SECURITY.md         # Security policies
├── github/                 # GitHub templates
│   └── .github/            # Issue templates
└── scripts/                # Utility scripts (future)
```

## 🚀 Quick Start

1. Navigate to the project directory: `cd project/`
2. Install dependencies: `pip install -r config/requirements.txt`
3. Run the application: `python config/app.py`
4. Open browser: `http://127.0.0.1:5000`

## 📋 Development

Use the Makefile for common development tasks:
```bash
cd project/config/
make install    # Install dependencies
make run        # Start development server
make test       # Run tests
make clean      # Clean temporary files
```
