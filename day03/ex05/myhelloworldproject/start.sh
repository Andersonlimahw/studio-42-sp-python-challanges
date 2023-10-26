#!/bin/bash

# Activate the virtual environment
source ./

# Run server
echo "🐍 Project will run in http://localhost:8000"
python manage.py runserver
echo "🐍 Project stoped"

