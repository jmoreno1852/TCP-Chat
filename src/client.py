import socket
import threading

nickname = input("Enter your nickname: ")

#Connect to server

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1',4444))

def receive(c):
    while True: 
        try:
            message = c.recv(1024).decode('utf-8')
            if message == 'Name:':
                c.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Client side error")
            c.close()
            break

def write(c):
    while True:
        message = '{}: {}'.format(nickname, input(''))
        c.send(message.encode('utf-8'))
#Main

receive_thread = threading.Thread(target=receive, args=(c,))
receive_thread.start()

write_thread = threading.Thread(target=write, args=(c,))
write_thread.start()

