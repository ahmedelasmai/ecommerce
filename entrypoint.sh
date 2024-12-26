#!/bin/bash

# This script runs migrations, collects static files, and starts the Gunicorn server.

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Gunicorn server
echo "Starting Gunicorn server..."
exec gunicorn ecom.wsgi:application --bind 0.0.0.0:8000