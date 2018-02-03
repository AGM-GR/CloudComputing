# CloudComputing

Repositorio creado por Alejandro Guerrero Martínez para la asignatura de Cloud Computing en el máster de Ingeniería Informática de la Universidad de Granada.

La documentación completa del proyecto se encuentra en: [agm-gr.github.io/CloudComputing](https://agm-gr.github.io/CloudComputing/)

#### Descripción

El proyecto tratará de un servicio de datos para juegos, en el cual se almacenarán los datos de los jugadores de distintos juegos (IDs, puntuación, localización, amigos ...)

Para ello se despliega una API Restful, sobre una base de datos MongoDB que guardará la información, para que los juegos puedan acceder a los datos en todo momento.

#### Aprovisionamiento

El aprovisionamiento del servidor se realiza con Ansible, el cual instalará en la/las máquinas indicadas:
* Python 3.6, el lenguaje sobre el que se reliza la API.
* Pip para instalar librerías de python:
  * flask, flask-restful flask-cors y flask-jsonpify, el cual sera el microframework sobre el que montaremos la API REST.
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
https://hub.docker.com/r/agmgr/cloudcomputing/
Despliegue Vagrant: 52.168.23.89

Cómo ejecutar la orquestación y más información en el [enlace](https://agm-gr.github.io/CloudComputing/Orquestacion).

#### Contenedores

El servicio se podrá desplegar en un contenedor de Docker destinado a la ejecución de este. El contenedor tiene una imagen del sistema Alpine, elegido por su simplicidad y ligereza (la imagen completa apenas ocupa 60 mb) dejando más espacio para datos y necesitando menos cpu para el servicio.

Contenedor: [https://dockerstatus.azurewebsites.net](https://dockerstatus.azurewebsites.net)

Imagen del contenedor en Docker Hub: [https://hub.docker.com/r/agmgr/cloudcomputing/](https://hub.docker.com/r/agmgr/cloudcomputing/)

Como lanzar el contenedor en Azure y más información en el [enlace](https://agm-gr.github.io/CloudComputing/Contenedores).

### Composición

El servicio final desarrollado [GameDataService](GameDataService/gamedataservice.py), consta de dos contenedores para su composición, uno que ejecuta el servicio REST, sobre una imagen de Alpine con python3, como ya se había comentado anteriormente se ha elegido por su ligereza y simplicidad. Y otro contenedor con la base de datos MongoDB la cual será consultada por la API para obtener los datos, la imagen elegida es la oficial de MongoDB, ya que viene preparada para servir solo la base de datos totalmente configurada.

Hito6: [https://ccdockercompose.westeurope.cloudapp.azure.com](ccdockercompose.westeurope.cloudapp.azure.com)

Como lanzar el docker-compose en Azure y más información en el [enlace](https://agm-gr.github.io/CloudComputing/Composicion).
