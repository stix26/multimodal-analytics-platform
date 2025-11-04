#!/usr/bin/env python3
"""
Setup script for Advanced Multi-Modal Computational Analytics Platform.
"""

from setuptools import setup, find_packages
import os

def read_requirements():
    """Read requirements from requirements.txt file."""
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

def read_long_description():
    """Read long description from README.md."""
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name="multimodal-analytics-platform",
    version="1.0.0",
    author="Advanced Multi-Modal Computational Analytics Platform Contributors",
    author_email="contributors@multimodal-platform.org",
    description="Research-grade computational analysis platform combining Computer Vision, Audio Processing, and Advanced Mathematics",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/multimodal-analytics-platform",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/multimodal-analytics-platform/issues",
        "Documentation": "https://github.com/yourusername/multimodal-analytics-platform/wiki",
        "Source Code": "https://github.com/yourusername/multimodal-analytics-platform",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Multimedia :: Graphics :: Capture :: Digital Camera",
        "Topic :: Education",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.900",
            "pre-commit>=2.15.0",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "myst-parser>=0.17.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "multimodal-platform=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.json", "*.html", "*.css", "*.js"],
    },
    keywords="multimodal machine-learning computer-vision audio-processing mathematics research academic",
    zip_safe=False,
)
