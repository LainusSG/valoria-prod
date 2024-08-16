#!/bin/sh

echo 'Running collectsatic...'
python manage.py collectstatic --no-input --settings=core.settings.production


echo 'apliying migrations...'
python manage.py wait_for_db --settings=core.settings.production
python manage.py migrate --settings=core.settings.production
python manage.py migrate --run-syncdb --settings=core.settings.production

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=core.settings.production core.wsgi:application --bind 0.0.0.0:8000