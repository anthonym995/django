#!/bin/bash

echo "BUILD START"
# Ensure Python and pip are available, if necessary
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 manage.py migrate --noinput
python3 manage.py add_features || echo "add_features failed"
python3 manage.py create_post || echo "create_post failed"
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"
