import socket

SERVER_ADDRESS = ('localhost', 100)

DOMAIN_NAME = 'www.gunadarma.ac.id'
PORT = 100

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(DOMAIN_NAME.encode('utf-8'), (SERVER_ADDRESS))
print(f"Request sent to DNS server for {DOMAIN_NAME}")
print("Waiting for response...")
response, _ = client_socket.recvfrom(1024)
print(f"Received response: {response.decode('utf-8')}")