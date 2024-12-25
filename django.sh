#!/bin/bash

echo "Applying Migrations..."
python apps/manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python apps/manage.py migrate
echo ====================================

echo "Starting Server..."
python apps/manage.py runserver 0.0.0.0:8000
