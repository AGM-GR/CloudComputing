#!/bin/bash

# Crea el grupo de recursos
az group create --name CC --location eastus

# Crea la máquina virtual en el grupo de recursos y gruarda la salida con la 
#  información de la máquina en el archivo tmpconexionfile
az vm create --resource-group CC --name clivm --image UbuntuLTS --generate-ssh-keys > tmpconexionfile

# Obtiene la ip de la máquina recien creada del archivo tmpconexionfile
ip=$(jq -r '.publicIpAddress' tmpconexionfile)

# Elimina el archivo tmpconexionfile
rm tmpconexionfile

# (A?)Provisiona la nueva máquina creada
cd provision/ansible/
echo $ip >> hosts
ansible-playbook provision.yml
