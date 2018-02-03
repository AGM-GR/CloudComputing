# Composición de contenedores con Docker-Compose

El servicio final desarrollado GameDataService, consta de dos contenedores para su composición, uno que ejecuta el servicio REST, sobre una imagen de Alpine con python3, como ya se había comentado anteriormente se ha elegido por su ligereza y simplicidad. Y otro contenedor con la base de datos MongoDB la cual será consultada por la API para obtener los datos, la imagen elegida es la oficial de MongoDB, ya que viene preparada para servir solo la base de datos totalmente configurada.

A la hora de desplegar la composición de contenedores sobre Azure, tras tener configurado Azure CLI 2.0, como se ha indicado anteriormente, lo primero será crear un Grupo de Recursos para los servicios:

`az group create --name DockerGroup --location westeurope`

Dentro de ese servicio crearemos una máquina virtual especifica de Azure para despliegues con docker-compose:

`az group deployment create --resource-group DockerGroup --template-uri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/docker-simple-on-ubuntu/azuredeploy.json`

Al ejecutar el comando, nos pedirá varios datos, un nombre para el dispositivo de almacenamiento, el usuario root, la contraseña de este y el dns de máquina.  
Una vez introducidos estos datos se creará la máquina y podremos acceder a ella mediante ssh con el dns introducida.

Una vez en la máquina debemos de obtener los archivos para la composición, ya sea transmitiendolos a la máquina desde ssh o clonando este repositorio. Y tras esto ejecutamos la composición del servicio, con la opción -d para que se queden ejecutados en background:

`sudo docker-compose up -d`

Y con esto nuestro servicio ya estará disponible en nuestro dns introducido y el puerto 5000. Con las siguientes rutas disponibles:

"/" -> GET: obtiene información del servicio.  
"/status" -> GET: devuelve status: ok.  
"/games" -> GET: devuelve una lista de juegos disponibles.  
"/game" -> POST: crea un nuevo juego.  
"/game/game_id" -> GET: obtiene información del juego.  
&nbsp;&nbsp;-> PUT: actualiza la información de un juegos.  
&nbsp;&nbsp;-> DELETE: elimina un juego y todos los juegadores asociados a este.  
"/game" -> POST: crea un nuevo juego.  
"/game/game_id/players" -> GET: obtiene todos los jugadores de un juego.  
"/game/game_id/player/player_id" -> GET: obtiene la información de un jugador.  
&nbsp;&nbsp;-> PUT: actualiza la información de un jugador  
&nbsp;&nbsp;-> DELETE: elimina un jugador.  
"/game/game_id/player" -> POST: crea un nuevo jugador de un juego.  

![Inicio Servicio](images/compose-info.png?raw=true)

![Servicio lista Juegos](images/compose-games.png?raw=true)
