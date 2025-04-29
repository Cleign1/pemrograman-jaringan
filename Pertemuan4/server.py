import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5555))
server_socket.listen()
print("Server is listening on port 5555...")

client, address = server_socket.accept()

while True:
    print("Waiting for message...")
    message = client.recv(1024).decode('utf-8')
    print(f"Received message: {message} from: {address}")
    
    reply = input("Reply: ")
    client.send(reply.encode('utf-8'))
    print("Reply sent.")