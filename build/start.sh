#!bin/bash
echo "데이터베이스 마이그레이션"
python3 ./src/manage.py makemigrations
python3 ./src/manage.py migrate
exec "$@"