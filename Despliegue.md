# Despliegue automático en Azure

Para realizar el Despliegue será necesario contar con una cuenta de Azure y tener instalado el Azure CLI 2.0:

`sudo apt-get install azure-cli`

o

`pip install azule-cli`

Y configurarlo para conectar con nuestra cuenta de azure, ejecutando el siguiente comando:

`az configure`

También necesitaremos tener instalado el programa "jq":

`sudo apt-get install jq`

Hecho esto podemos ya ejecutar el scrip [acopio.sh](https://github.com/AGM-GR/CloudComputing/blob/master/acopio.sh)

`sh acopio.sh`

Este script nos creará un grupo de recursos "CC" y una máquina virtual aprovisionada en nuestra cuenta de azure.

Resultado de la ejecución del Despliegue:

![EjecuciónDelAprovisionamiento](images/resultado_ejecucion_despliegue.png?raw=true)
