import socket
import threading
import os
 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
CHUNKSIZE = 4 * 1024
SEPARATOR = "<SEPARATOR>"

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
 
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
 
    while True:
        data = conn.recv(1024).decode()
        if data == "SEND":
            conn.send("OK".encode())
            filename = conn.recv(1024).decode()
            receive_file(conn)
        elif data == "RECEIVE":
            conn.send("OK".encode())
            filename = conn.recv(1024).decode()
            send_file(conn, filename)
        else:
            break
 
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

def send_file(conn, filename):
    filesize = os.path.getsize(filename)
    conn.send(f"{filename}{SEPARATOR}{filesize}".encode())
 
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(CHUNKSIZE)
            if not bytes_read:
                break
            conn.sendall(bytes_read)
 
def receive_file(conn):
    data = conn.recv(1024).decode()
    filename, filesize = data.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
 
    with open(filename, "wb") as f:
        while True:
            bytes_read = conn.recv(CHUNKSIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
 
if __name__ == '__main__':
    start_server()