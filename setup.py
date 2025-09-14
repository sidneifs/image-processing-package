#Realização de um pacote Python para processamento de imagens
# Este pacote inclui funcionalidades para combinação, transformação, leitura, salvamento e visualização de imagens

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-package-sidneifs",
    version="0.0.4",
    author="Sidnei Silva",
    author_email="sidneifs@gmail.com",
    description="Pacote Python para processamento de imagens: combinação, transformação, leitura, salvamento e visualização.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sidneifs/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
)