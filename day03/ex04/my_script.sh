#!/bin/bash

# Create a virtual environment named django_venv
py -m venv django_venv

# Activate the virtual environment
source django_venv/Scripts/activate

# Install the required packages from requirement.txt
pip install -r requirements.txt

# Deactivate the virtual environment
# source django_venv/Scripts/deactivate

echo "Virtual environment 'django_venv' created and activated."
