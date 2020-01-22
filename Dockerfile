FROM python:3.7-slim 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile /code
COPY Pipfile.lock /code/


RUN pip install pipenv && pipenv install --system 

COPY . /code