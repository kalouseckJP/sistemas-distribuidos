Para crear un contendor a compartir se utiliza

sudo docker build -t chat-client ./Clientes
sudo docker save -o chat-client.tar chat-client

esto crea un archivo .tar 

Este archivo es compartido al dispositivo cliente.

En el dispositivo cliente se utiliza

sudo docker load -i chat-client.tar
sudo docker run -it chat-client
