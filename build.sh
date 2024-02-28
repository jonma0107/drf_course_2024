#!/bin/bash

# Instalar dependencias de Python
python3.10 -m venv venv
source venv/bin/activate
pip install -r source/requirements.txt

# Construir la documentación
make html
