import socket
import threading
import sys

#Variables globales
clients = []
nicknames = []

#Set server - Done
def setup_server(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(5)
    print(f"Server listening on {host}:{port}")
    return s

#Manage Clients, accept client connection and save its name
def handle_client(s):
    global clients
    global nicknames
    while True:
        #Accept clients connection and save it
        client, addr = s.accept()
        clients.append(client)
        print(f"Connection from {addr}")
        
        #Store Nickname 
        client.send('Name:'.encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")     
        nicknames.append(nickname)
        client.send("You are now connected.".encode('utf-8'))
        #Handle client thread    
        thread = threading.Thread(target=receive_data, args=(client,))
        thread.start()
        
def receive_data(client):
    global clients
    global nicknames
    while True:
        
        index = clients.index(client)
        nickname = nicknames[index]
        try:  
            data = client.recv(1024).decode('utf-8')
            if  not data:
                break
            broadcast(data, client)
            print(f"\nData recieved: {data}")
        except:
            clients.remove(client)
            client.close()
            broadcast('{} left!'.format(nickname).encode('utf-8'),client)
            nicknames.remove(nickname)
            break
            
    client.close()
    remove(client)


#Function to remove client from global variable clients
def remove(client):
    global clients
    if client in clients:
        clients.remove(client)

def broadcast(data, connection):
    global clients
    for client in clients:
        if client != connection:
            try:
                client.send(data.encode('utf-8'))
            except:
                client.close()
                remove(client)

#Asuring to close al clients before closing the server
def close_server(s):
    global clients
    for client in clients:
        client.close()
    s.close()
    print("Clients and Server closed")
