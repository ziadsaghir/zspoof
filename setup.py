"""
ZSPOOF v3.0.0 - Setup Configuration
AI-Powered Network Security Platform
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme = Path(__file__).parent / "README.md"
long_description = readme.read_text(encoding="utf-8") if readme.exists() else ""

setup(
    name="zspoof",
    version="3.0.0",
    author="Ziad SAGHIR",
    author_email="ziadsaghir8@gmail.com",
    description="AI-Powered MAC Spoofing Framework for Security Research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ziadsaghir/zspoof",
    project_urls={
        "Bug Reports": "https://github.com/ziadsaghir/zspoof/issues",
        "Source": "https://github.com/ziadsaghir/zspoof",
        "Documentation": "https://github.com/ziadsaghir/zspoof#readme",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.8",
    install_requires=[
        "tqdm>=4.66.0",
        "colorama>=0.4.6",
        "flask>=3.0.0",
        "flask-cors>=4.0.0",
        "flask-socketio>=5.3.5",
        "python-socketio>=5.10.0",
        "eventlet>=0.33.3",
        "scapy>=2.5.0",
        "netifaces>=0.11.0",
        "psutil>=5.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "zspoof=zspoof_ultimate:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
