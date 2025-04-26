#!/bin/bash
python3 -m venv venv 
source venv/bin/activate
cp .env.dev .env
./venv/bin/pip install -r requirements.txt
flask run
