FROM python:3.9-alpine3.13
LABEL maintainer="boatbot.seven"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000
ARG DEV=false  # แก้จาก flase เป็น false

RUN apk add --update --no-cache postgresql-dev gcc musl-dev && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt ; fi && \
    rm -rf /tmp

RUN /py/bin/pip install flake8

RUN adduser \
        --disabled-password \
        --home /home/django-user \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user
