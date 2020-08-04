#!/bin/sh
cd /code/
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py shell -c "\
import environ; \
from django.contrib.auth import get_user_model; \
User=get_user_model(); \
env = environ.Env(DEBUG=(bool, False),); \
User.objects.create_superuser(env('DJANGO_ADMIN_USER'), 'admin@admin.com', env('DJANGO_ADMIN_PASS'))"

gunicorn store.wsgi:application --bind 0.0.0.0:8000

exec "$@"