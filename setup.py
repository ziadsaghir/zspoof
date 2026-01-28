#!/usr/bin/env python3
"""
ZSPOOF ULTIMATE - Setup Script
Enables installation as a Python package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    requirements = [
        line.strip() 
        for line in requirements_file.read_text().split('\n')
        if line.strip() and not line.startswith('#')
    ]

setup(
    name="zspoof",
    version="2.1.0",
    author="Ziad SAGHIR",
    author_email="ziadsghir8@gmail.com",
    description="Advanced Network Identity Manipulation Framework for Security Research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ziadsaghir/zspoof",
    project_urls={
        "Bug Reports": "https://github.com/ziadsaghir/zspoof/issues",
        "Source": "https://github.com/ziadsaghir/zspoof",
        "Documentation": "https://github.com/ziadsaghir/zspoof#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: C++",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Environment :: Console",
    ],
    keywords=[
        "security", "penetration-testing", "red-team", "mac-spoofing",
        "arp-spoofing", "network-security", "ethical-hacking", "infosec",
        "cybersecurity", "networking", "mitm", "spoofing"
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "black>=22.1.0",
            "pylint>=2.15.0",
            "pytest>=7.0.0",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md", "*.cpp", "*.h"],
    },
    entry_points={
        "console_scripts": [
            "zspoof=src.zspoof_ultimate:main",
        ],
    },
    zip_safe=False,
)
