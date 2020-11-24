FROM python:3.9

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python-dev \
    python-setuptools

WORKDIR /srv/project

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY src/ src/

CMD ["python", "./src/manage.py", "runserver", "0:8000"]