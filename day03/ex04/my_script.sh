#!/bin/bash

# Create a virtual environment named django_venv
py -m venv django_venv

# Activate the virtual environment
source django_venv/bin/activate

# Install the required packages from requirement.txt
pip install -r requirement.txt

# Deactivate the virtual environment
deactivate

echo "Virtual environment 'django_venv' created and activated."
