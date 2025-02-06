import socket
import threading
import sys

#Funciones necesarias
#Setear el servidor
#Manejar a los clientes
#Broadcast de los mensajes
#Eliminar conexiones 

#Necesito una lista de clientes
def setup_server(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(5)
    print(f"Server listentint on {host}:{port}")

def handle_client(client):
    while True:
        data = client.recv(1024).decode('utf-8')
        if  not data:
            break
        print(f"\nData recieved: {data}")
    client.close()

def remove(client):
    if client in clients:
        clients.remove(client)

def broadcast(data, connection, clients):
    for client in clients:
        if client != connection:
            try:
                client.send(data)
            except:
                client.close()
                remove(client)

