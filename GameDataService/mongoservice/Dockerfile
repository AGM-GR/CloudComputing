FROM mongo:3.6.2

MAINTAINER Alejandro Guerrero Martínez

WORKDIR /gamedataservice

COPY gamedata /gamedataservice/gamedata

COPY mongodatarestore.sh /gamedataservice
RUN chmod 777 /gamedataservice/mongodatarestore.sh

ENTRYPOINT /gamedataservice/mongodatarestore.sh
