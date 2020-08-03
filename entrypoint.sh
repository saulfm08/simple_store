#!/bin/sh
cd /code/
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py shell -c "\
from django.contrib.auth import get_user_model; \
User=get_user_model(); \
User.objects.create_superuser('admin', 'admin@admin.com', 'admin')"

gunicorn store.wsgi:application --bind 0.0.0.0:8000

exec "$@"