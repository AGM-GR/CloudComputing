FROM alpine:3.3

MAINTAINER Alejandro Guerrero Martínez

WORKDIR /statusservice

RUN apk --update add python py-pip

RUN pip install flask flask-restful flask-jsonpify pymongo

COPY service.py /statusservice

ENTRYPOINT python service.py
