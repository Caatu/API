FROM python:3.7.0b2-stretch

RUN apt update

RUN apt -y install \
    python3-pip \
    gcc

RUN pip3 install pipenv --upgrade

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --dev --deploy --system