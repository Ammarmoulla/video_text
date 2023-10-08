script_path=$(readlink -f "$0")
script_dir=$(dirname "$script_path")
python manage.py migrate
python ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin_git', 'admin@example.com', 'admingit')"
python ${script_dir}/server.py 
