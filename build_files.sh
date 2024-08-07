echo "BUILD START"
python3.9 -m ensurepip --upgrade  # Ensure pip is installed
python3.9 -m pip install --upgrade pip  # Upgrade pip to the latest version
python3.9 -m pip install -r requirements.txt  # Install dependencies
python3.9 manage.py collectstatic --noinput --clear  # Collect static files
echo "BUILD END"