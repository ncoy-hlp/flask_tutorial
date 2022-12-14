FROM python:3.10

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y netcat
RUN apt-get install -y pgloader
RUN apt-get install nano
RUN apt-get -y install python3-pip

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./
COPY app/ ./app/

RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

WORKDIR /usr/src/app/app
