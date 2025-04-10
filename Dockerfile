FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev libjpeg-dev zlib1g-dev curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN echo "POSTGRES_USER=${POSTGRES_USER}" >> .env && \
    echo "POSTGRES_PASSWORD=${POSTGRES_PASSWORD}" >> .env && \
    echo "POSTGRES_DB=${POSTGRES_DB}" >> .env && \
    echo "POSTGRES_HOST=${POSTGRES_HOST}" >> .env && \
    echo "POSTGRES_PORT=${POSTGRES_PORT}" >> .env && \
    echo "SECRET_KEY=${SECRET_KEY}" >> .env && \
    echo "DEBUG=${DEBUG}" >> .env && \
    echo "REDIS_HOST=${REDIS_HOST}" >> .env && \
    echo "CELERY_BROKER_URL={$CELERY_BROKER_URL}" >> .env && \
    echo "CELERY_RESULT_BACKEND={$CELERY_RESULT_BACKEND}" >> .env && \
    cat .env

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
