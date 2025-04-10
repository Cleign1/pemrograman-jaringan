import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9000))
server_socket.listen()
print("Server is listening on port 9000...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Koneksi dari {address} telah diterima.")
    
    client_socket.send(bytes("Nama saya Muhamad Ibnu Khaidar Hafiz, ini adalah protokol TCP", "utf-8"))
    client_socket.close()