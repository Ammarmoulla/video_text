script_path=$(readlink -f "$0")
script_dir=$(dirname "$script_path")
python manage.py migrate
python ${script_dir}/server.py 
