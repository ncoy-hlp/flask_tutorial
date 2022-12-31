FROM python:3.10

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python3-pip

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./
COPY app/ ./app/

RUN pip3 install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

WORKDIR /usr/src/app/app

EXPOSE 5000

CMD ["sh", "start.sh"]
