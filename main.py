import threading
from src.server import *

def main()
    clients = []    #Global variable to save client connections
    nicknames = []  #Global variable to save client names
    host = "127.0.0.1"
    port = 4444

    s = setup_server(host, port
    try:
        handle_client(s)
    except KeyboardInterrupt:
        close_server(s)
        
if __name__ == "__init__":
    main()
