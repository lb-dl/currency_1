#!/bin/bash

if [[ "$MODE" == "wsgi" ]]; then
  if [[ "$SERVER" == "dev" ]]; then
    python ./src/manage.py runserver 0:8000
  else
    gunicorn \
      -w 4 \
      -b 0.0.0.0:8000 \
      --chdir /srv/project/src currency.wsgi \
      --timeout 30 \
      --max-requests 10000
  fi
elif [[ "$MODE" == "celery" ]]; then
  cd src && celery -A currency worker -l INFO
elif [[ "$MODE" == "celerybeat" ]]; then
  cd src && celery -A currency beat -l INFO
else
  echo "NO SUCH MODE"
fi