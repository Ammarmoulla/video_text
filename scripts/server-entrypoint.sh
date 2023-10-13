#!/bin/sh
script_path=$(readlink -f "$0")
script_dir=$(dirname "$script_path")

#ngrok auth and run
token=$(sed -n "s/ngrok_token=\(.*\)/\1/p" < ${PWD}/.env)
ngrok config add-authtoken $token
ngrok http 8000


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done


# python manage.py collectstatic --noinput

# python manage.py createsuperuser --noinput
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin_git', 'admin@example.com', 'admingit')"

# gunicorn  --bind 0.0.0.0:8000 --workers 5 --threads 3

gunicorn core.wsgi --worker-class=gevent --worker-connections=1000 --workers=5

# for debug
# python manage.py runserver 0.0.0.0:8000 &
