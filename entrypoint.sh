#!/bin/sh

if [ "$DATABASE" = "postgresql" ]
then
    echo "Waiting for postgreSQL..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"
