FROM python:3.9-alpine3.14

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD admin

RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev mariadb-dev && \
    apk add --no-cache mariadb-connector-c && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir django gunicorn mysqlclient && \
    apk del .build-deps

RUN mkdir /app
WORKDIR /app

CMD while ! python3 manage.py migrate--noinput ; do sleep 1 ; done && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --user admin --email admin@localhost --noinput; \
    gunicorn -b 0.0.0.0:8000 config.wsgi
