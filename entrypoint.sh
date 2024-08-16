#!/bin/sh

echo 'Running collectsatic...'
python manage.py collectstatic --no-input 


echo 'apliying migrations...'
python manage.py wait_for_db 
python manage.py migrate 
python manage.py migrate 

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=core core.wsgi:application --bind 0.0.0.0:8000