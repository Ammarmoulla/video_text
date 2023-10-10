#!/bin/sh


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done


python manage.py collectstatic --noinput

# python manage.py createsuperuser --noinput
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin_git', 'admin@example.com', 'admingit')"

# gunicorn core.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
python manage.py runserver 0.0.0.0:8000