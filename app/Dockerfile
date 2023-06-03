# Use specific version of Python with Alpine Linux
FROM python:3.9-alpine3.14

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD admin

# Install build dependencies and MariaDB connector
RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev mariadb-dev && \
    apk add --no-cache mariadb-connector-c && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir django==3.2.4 gunicorn==20.1.0 mysqlclient==2.0.3 && \
    apk del .build-deps

# Create app directory
RUN mkdir /app
WORKDIR /app

# Copy project files
COPY . /app/

# Run migrations, collect static files, and start the server
CMD while ! python3 manage.py migrate --noinput; do sleep 1; done && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --username admin --email admin@localhost --noinput && \
    gunicorn -b 0.0.0.0:8000 config.wsgi

# Expose port 8000 for the web application
EXPOSE 8000
