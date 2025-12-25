from setuptools import setup, find_packages

setup(
    name="zspoof",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["tqdm"],
    entry_points={
        "console_scripts": [
            "zspoof = zspoof.toolkit:main",
        ],
    },
)
