FROM python:3.6-slim

WORKDIR /opt
ARG INCLUDE_TEST=0

ENV PYTHONPATH=/opt/
ENV PYTHONUNBUFFERED=1

COPY requirements*.txt /opt/
COPY go.json /opt/go.json
COPY hsa.tab /opt/hsa.tab

RUN apt -y update && apt -y install build-essential libxml2-dev zlib1g-dev python-dev python-pip pkg-config libffi-dev libcairo-dev

RUN REQUERIMENTS_FILE="requirements.txt"; \
    if [ $INCLUDE_TEST == 1 ]; then \
        REQUERIMENTS_FILE="requirements-test.txt"; \
    fi;\
    pip install -r /opt/$REQUERIMENTS_FILE

COPY go-basic.obo /opt/go-basic.obo
