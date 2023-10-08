script_path=$(readlink -f "$0")
script_dir=$(dirname "$script_path")
python ${script_dir}/server.py 
