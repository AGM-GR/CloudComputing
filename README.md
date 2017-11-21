# CloudComputing

Repositorio creado por Alejandro Guerrero Martínez para la asignatura de Cloud Computing en el máster de Ingeniería Informática de la Universidad de Granada.

La documentación completa del proyecto se encuentra en: [agm-gr.github.io/CloudComputing](https://agm-gr.github.io/CloudComputing/)

El proyecto tratará de un servicio de datos para juegos, en el cual se almacenarán los datos de los jugadores de distintos juegos (IDs, puntuación, localización, amigos ...)

Para ello se despliega una API Restful, sobre una base de datos MongoDB que guardará la información, para que los juegos puedan acceder a los datos en todo momento.

El aprovisionamiento del servidor se realiza con Ansible, el cual instalará en la/las máquinas indicadas:
* Python 2.7, el lenguaje sobre el que se reliza la API.
* Pip para instalar librerías de python:
  * flask, flask-restful y flask-jsonpify, el cual sera el microframework sobre el que montaremos la API REST.
  * pymongo, para poder trabajar con MongoDB en python.
* MongoDB, la base de datos que utilizaremos.

Podremos encontrar los archivos del aprovisionamiento y más información en el [enlace](https://github.com/AGM-GR/CloudComputing/tree/master/provision/ansible).

También es posible crear el sistema automáticamente en azure ejecutando el script [acopio.sh](https://github.com/AGM-GR/CloudComputing/blob/master/acopio.sh)
Para su ejecución sera necesario tener instalado y configurado Azure CLI 2.0 y el programa "jq".
Este script nos creará un grupo de recursos "CC" y una máquina virtual con Ubuntu 16.0 aprovisionada en nuestra cuenta de Azure.

La máquina desplegada para el hito 3 le corresponde la siguiente IP.

Despliegue: 52.179.97.106
