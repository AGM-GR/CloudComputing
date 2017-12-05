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

El aprovisionamiento en la máquina servidora se realiza mediante Ansible, el cual instalará:

* MongoDB -> La base de datos sobre la que trabaja.
* Python 2.7 -> El lenguaje utilizado.
* Pip -> Instalador de librerías para python.
* Librerías python:
  * flask -> Microframework sobre el que montaremos la API.
  * flask-restful -> Librerías de flask para manejar una API RESTFUL.
  * flask-jsonpify -> Transforma datos de la BD a JSON.
  * pymongo -> Conexión con la base de datos MongoDB.

[Cómo realizar el Aprovisionamiento y ejecución](https://agm-gr.github.io/CloudComputing/Aprovisionamiento)

## Despliegue

El despliegue en Azure se realiza ejecutando el script acopio.sh
Para su ejecución sera necesario tener instalado y configurado Azure CLI 2.0 y el programa "jq".
Este script crea un grupo de recursos "CC" en Est-EU y una máquina virtual en dicho grupo, la cual es aprovisionada automáticamente.
En la máquina se instala Ubuntu 16.0, imágen elegida por su ligereza, facilidad de instalación con azure y conocimiento previo con ésta distribución.

[Cómo realizar el Despliegue y ejecución](https://agm-gr.github.io/CloudComputing/Despliegue)

## Orquestación

Podremos orquestar el despliegue usando Vagrant, una vez configurado nuestra cuenta de azure con AzureCLI, ejecutaremos el comando `vagrant up` en la carpeta de [orquestacion](https://github.com/AGM-GR/CloudComputing/tree/master/orquestacion).

Nos creará dos máquinas nuevas en azure, una para la API y otra para la base de datos, ambas con Ubuntu 16.0 y totalmente aprovisionadas como anteriormente.

Cómo ejecutar la orquestación y más información en el [enlace](https://agm-gr.github.io/CloudComputing/Orquestacion).

## Licencia
Este proyecto está desarrollado bajo una licencia [GNU GLP V3](https://github.com/AGM-GR/CloudComputing/blob/master/LICENSE)
