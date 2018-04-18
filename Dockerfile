FROM ubuntu:16.04

COPY . /code

RUN apt-get update -y && \
    apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code
RUN pip install -r requeriments.txt

CMD scrapyd

