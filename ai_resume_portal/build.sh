#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Download spaCy language model
python -m spacy download en_core_web_sm

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
