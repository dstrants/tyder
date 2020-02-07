#!/bin/bash
echo 'Creating Virtual Env'
virtualenv venv -p python3
echo 'Enabling Virtual Env'
source venv/bin/activate
echo 'Installing Dependencies'
pip install -r requirements.txt
echo 'Creating settings file'
touch setup.py
echo 'Done'