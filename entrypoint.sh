#!/bin/sh

# Выполняем миграции
python manage.py migrate

python init_db.py
# Запускаем сервер
exec "$@"
