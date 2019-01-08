#!bin/bash
echo "정적 파일 관리"
python3 ./src/manage.py collectstatic --noinput
echo "데이터베이스 마이그레이션"
python3 ./src/manage.py makemigrations
python3 ./src/manage.py migrate
exec "$@"