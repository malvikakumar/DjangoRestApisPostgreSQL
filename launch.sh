#!/bin/sh

echo "Launching the app"

python3 manage.py makemigrations && python3 manage.py migrate
python3 manage.py makemigrations authentication && python3 manage.py migrate authentication
python3 manage.py makemigrations products && python3 manage.py migrate products


python3 manage.py runserver 0.0.0.0:8080