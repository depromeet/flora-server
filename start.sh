#!/bin/bash
source venv/bin/activate
export $(cat .env | xargs)
python manage.py runserver