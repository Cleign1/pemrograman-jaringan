import socket
import threading
import os
 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
CHUNKSIZE = 4 * 1024
SEPARATOR = "<SEPARATOR>"

def send_file_to_server(filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
 
    client.send("SEND".encode())
    response = client.recv(1024).decode()

    if response == "OK":
        client.send(filename.encode())
        send_file(client, filename)
 
    client.close()

def receive_file_from_server(filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
 
    client.send("RECEIVE".encode())
    response = client.recv(1024).decode()
 
    if response == "OK":
        client.send(filename.encode())
        receive_file(client)
 
    client.close()

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
    # send_file_to_server("file_client.txt")
    receive_file_from_server("file_server.txt")