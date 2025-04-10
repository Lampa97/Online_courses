FROM python:3.12-slim

WORKDIR /code

RUN apt-get update \
    && apt-get install -y gcc libpq-dev libjpeg-dev zlib1g-dev curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .

RUN echo "POSTGRES_USER=${POSTGRES_USER}" >> .env && \
    echo "POSTGRES_PASSWORD=${POSTGRES_PASSWORD}" >> .env && \
    echo "POSTGRES_DB=${POSTGRES_DB}" >> .env && \
    echo "POSTGRES_HOST=db" >> .env && \
    echo "POSTGRES_PORT=${POSTGRES_PORT}" >> .env && \
    echo "SECRET_KEY=${SECRET_KEY}" >> .env && \
    echo "DEBUG=${DEBUG}" >> .env && \
    echo "REDIS_HOST=redis://redis:6379//" >> .env && \
    echo "CELERY_BROKER_URL=redis://redis:6379/1" >> .env && \
    echo "CELERY_RESULT_BACKEND=redis://redis:6379/1" >> .env && \
    cat .env

ENV PYTHONPATH=/code
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["sh", "-c", "python manage.py runserver"]
