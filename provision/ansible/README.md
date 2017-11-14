# Aprovisionamiento con Ansible

Para utilizar este aprovisionamiento lo primero será instalar Ansible en nuestra máquina local:

`sudo apt-get install ansible`

Lo siguiente será modificar el archivo **host** en el cual debemos sustituir la ip escrita por la/las ips de las máquinas a aprovisionar y en el archivo **provision.yml** modificar el usuario por el usuario de nuestra máquina.

Una vez hecho esto solo ejecutar el siguiente comando estando situado en la carpeta del aprovisionamiento:

`ansible-playbook provision.yml`
