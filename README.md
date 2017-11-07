# Cloud Computing

## Descripción del Problema

Se pretende desarrollar una solución para una serie de videjuegos en distintas plataformas, los cuales almacenarán datos de los jugadores y puntuaciones, permitiendo en cada uno ver distintos rankings y datos sobre ese videojuego.

## Solución del Problema

Para solucionar este problema se plantea crear una aplicación en red que ofrezca métodos para obtener y almacenar los datos de los jugadores:
* Almacenará los datos de los jugadores en una base de datos NoSQL.
* Constará de una API REST.
* Juegos multiplataforma hará uso de la API.

## Arquitectura de la Solución

* La solución se basará en una arquitectura de microservicios.
* La API REST se programará en Python.
* Los juegos estarán desarrollados en C# con el motor gráfico Unity.

## Aprovisionamiento

* Python 2.7
* Pip
* MongoDB
* Librerías python:
  * flask
  * flask-restful
  * flask-jsonpify
  * pymongo

## Licencia
Este proyecto está desarrollado bajo una licencia [GNU GLP V3](https://github.com/AGM-GR/CloudComputing/blob/master/LICENSE)
