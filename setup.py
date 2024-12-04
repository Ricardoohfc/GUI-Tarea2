from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Modelo_Estandar",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib"
    ],
    description="Paquete para analizar el Modelo Estándar de partículas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
