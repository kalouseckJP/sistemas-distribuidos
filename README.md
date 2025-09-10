# Qué es
Este conjunto de código python y Docker permite crear un chat entre clientes utilizando un servidor como intermedio.
## Características
- Dentro de cada archivo `.py` se encuentra que puerto utilizará el chat, por defecto es el puerto 8080.
- El cliente puede ingresar la IP del servidor al que desea unirse.
  - En linux se puede encontrar la IP del servidor utilizando `hostname -I` o `ip addr show` en la terminal del servidor.
  - En windows se puede encontrar utilizando `ip config` en CMD o Powershell.
- Se pueden crear y utilizar múltiples clientes.
- Los clientes pueden añadir un nombre para identificarse.

# Instalación
Se debe clonar el repositorio base utilizando.  

```
git clone https://github.com/kalouseckJP/sistemas-distribuidos
```  

## Para usar cliente

Dentro de la carpeta del repositorio, abrir una terminal.  
Y ejecutar los siguientes comandos.  

```
sudo docker build -t chat-client ./Clientes
sudo docker run -it chat-client
```

## Para usar el servidor

Dentro de la carpeta del repositorio, abrir una terminal.  
Y ejecutar los siguientes comandos.  

```
sudo docker build -t chat-server ./Servidor
sudo docker run -it -p 8080:8080 chat-server
```
