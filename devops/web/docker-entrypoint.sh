#!/usr/bin/env bash


# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Collect static folders
echo "Collect static folders"
python manage.py collectstatic --noinput

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000