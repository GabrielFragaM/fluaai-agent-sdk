import os
import setuptools

# Lê o conteúdo do arquivo README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Lê o conteúdo do arquivo requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="fluaai-agent-sdk",
    version="0.1.0",
    author="Gabriel Fraga",
    author_email="seu.email@example.com",
    description="SDK para integração com agentes da plataforma FluaAI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/agentsdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
)