import socket
import threading
import sys

#Funciones necesarias
#Setear el servidor
#Manejar a los clientes
#Broadcast de los mensajes
#Eliminar conexiones 

def setup_server(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(5)
    print(f"Server listentint on {host}:{port}")

def handle_client(client):
    pass

def broadcast(data):
    pass

