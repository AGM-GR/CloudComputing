# CloudComputing

Repositorio creado por Alejandro Guerrero Martínez para la asignatura de Cloud Computing en el máster de Ingeniería Informática de la Universidad de Granada.

La documentación completa del proyecto se encuentra en: [agm-gr.github.io/CloudComputing](https://agm-gr.github.io/CloudComputing/)

#### Descripción

El proyecto tratará de un servicio de datos para juegos, en el cual se almacenarán los datos de los jugadores de distintos juegos (IDs, puntuación, localización, amigos ...)

Para ello se despliega una API Restful, sobre una base de datos MongoDB que guardará la información, para que los juegos puedan acceder a los datos en todo momento.

#### Aprovisionamiento

El aprovisionamiento del servidor se realiza con Ansible, el cual instalará en la/las máquinas indicadas:
* Python 2.7, el lenguaje sobre el que se reliza la API.
* Pip para instalar librerías de python:
  * flask, flask-restful y flask-jsonpify, el cual sera el microframework sobre el que montaremos la API REST.
  * pymongo, para poder trabajar con MongoDB en python.
* MongoDB, la base de datos que utilizaremos.

Cómo ejecutar el aprovisionamiento y más información en el [enlace](https://agm-gr.github.io/CloudComputing/Aprovisionamiento).

#### Despliegue

También es posible crear el sistema automáticamente en azure ejecutando el script [acopio.sh](https://github.com/AGM-GR/CloudComputing/blob/master/acopio.sh)
Para su ejecución sera necesario tener instalado y configurado Azure CLI 2.0 y el programa "jq".
Este script nos creará un grupo de recursos "CC" y una máquina virtual aprovisionada en nuestra cuenta de Azure.
En ésta máquina se instalará una imagen de Ubuntu 16.0, elegida por su ligereza, facilidad de instalación con azure y conocimiento previo con ésta distribución.

La máquina desplegada para el hito 3 le corresponde la siguiente IP.

Despliegue: 52.168.162.6

Cómo ejecutar el despliegue y más información en el [enlace](https://agm-gr.github.io/CloudComputing/Despliegue).

#### Orquestación

Podremos orquestar el despliegue usando Vagrant, una vez configurado nuestra cuenta de azure con AzureCLI, ejecutaremos el comando `vagrant up` en la carpeta de [orquestacion](https://github.com/AGM-GR/CloudComputing/tree/master/orquestacion).

Nos creará dos máquinas nuevas en azure, una para la API y otra para la base de datos, ambas con Ubuntu 16.0 y totalmente aprovisionadas como anteriormente.

Despliegue Vagrant: 52.168.23.89

Cómo ejecutar la orquestación y más información en el [enlace](https://agm-gr.github.io/CloudComputing/Orquestacion).
