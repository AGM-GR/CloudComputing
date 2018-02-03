FROM alpine:3.6

MAINTAINER Alejandro Guerrero Martínez

WORKDIR /gameservice

RUN apk --update add python3

RUN pip3 install flask flask-restful flask-jsonpify flask-cors pymongo

COPY gamedataservice.py /gameservice

ENTRYPOINT python3 gamedataservice.py
