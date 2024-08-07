#!/bin/bash

echo "BUILD START"
# Ensure Python and pip are available, if necessary
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"
