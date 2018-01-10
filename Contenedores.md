# Despliegue del contenedor Docker en Azure

El contenedor Docker contiene la API REST desarrollada en python con el framework flask-rest, en el sistema Alpine, elegido por su simplicidad y ligereza (la imagen completa apenas ocupa 60 mb) dejando más espacio para datos y necesitando menos cpu para el servicio.
En el se se instala python, pip y las correspondientes librerías de python necesarias desde pip.

A la hora de desplegar el Contenedor sobre Azure, necesitaremos añadir un usuario para aplicaciones web desde el CLI 2.0 de azure:

`az webapp deployment user set --user-name agmgr --password $PasswordUsuario`

Posteriormente crearemos un Grupo de Recursos para los servicios desplegados:

`az group create --name DockerGroup --location westeurope`

Dentro de este grupo crearemos un plan para los servicios que despleguemos, en esta caso indicamos que van a ser sistemas basados en linux en máquinas S1:

`az appservice plan create --name DockerServicePlan --resource-group DockerGroup --sku S1 --is-linux`

Por último añadiremos un nuevo servicio, con nuestra imagen del contenedor docker subida a dockerhub:

`az webapp create --resource-group DockerGroup --plan DockerServicePlan --name DockerStatus --deployment-container-image-name agmgr/cloudcomputing`

Para que el servicio de nuestra API sea accesible debemos indicar el puerto del servicio (5000):

`az webapp config appsettings set -g DockerGroup -n  DockerStatus --settings PORT=5000`

Con esto nuestro servicio ya estará disponible en el contenedor Docker.
