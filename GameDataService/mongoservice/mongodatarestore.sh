#!/bin/bash

# Inicia el servicio de mongodb
mongod --bind_ip 0.0.0.0 &

# Inserta las tablas iniciales, si no se puede conectar lo sigue reintentando (con un timeout de 50s)
CONTADOR=0
mongoimport --db gamedata --collection games --file /gamedataservice/gamedata/games.json
mongoimport --db gamedata --collection players --file /gamedataservice/gamedata/players.json
while [[ $? -ne 0 && $CONTADOR -lt 50 ]] ; do
    sleep 2
    let CONTADOR+=2
    echo "Esperando a que mongo se inicie... ($CONTADOR)"
    mongoimport --db gamedata --collection games --file /gamedataservice/gamedata/games.json
    mongoimport --db gamedata --collection players --file /gamedataservice/gamedata/players.json
done

# Mantiene el contenedor encendido
tail -f /dev/null
