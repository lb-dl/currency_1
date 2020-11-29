FROM python:3.9

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python-dev \
    python-setuptools

WORKDIR /srv/project

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SERVER=production \
    MODE=wsgi

# MODE=[wsgi,celery,celerybeat]

COPY src/ src/

COPY ./run.sh ./run.sh

RUN chmod +rx ./run.sh

RUN useradd -ms /bin/bash ubuntu
RUN chown -R ubuntu:ubuntu /srv/project
USER ubuntu

CMD bash -C "./run.sh"
