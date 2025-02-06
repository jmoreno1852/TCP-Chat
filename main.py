import threading
from src.server import *

def main():
    host = "127.0.0.1"
    port = 4444

    s = setup_server(host, port)
    try:
        thread_handle=threading.Thread(target=handle_client, args=(s,))
        thread_handle.start()
    except KeyboardInterrupt:
        close_server(s)
        
if __name__ == "__main__":
    main()
