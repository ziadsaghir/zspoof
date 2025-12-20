from setuptools import setup

setup(
    name="zspoof",
    version="0.1.0",
    py_modules=["toolkit"],
    install_requires=["tqdm"],
    include_package_data=True,
    package_data={
        "": ["header.txt"],
    },
    entry_points={
        "console_scripts": [
            "zspoof=toolkit:main"
        ]
    },
    author="Ziad SAGHIR",
    description="MAC address manipulation & analysis tool",
    license="MIT",
)
