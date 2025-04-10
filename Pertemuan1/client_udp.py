import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "Halo, nama saya Muhamad Ibnu Khaidar Hafiz 50421867, ini adalah protokol UDP"
client_socket.sendto(message.encode('utf-8'), ('localhost', 9001))
data, address = client_socket.recvfrom(1024)
print(f"Pesan dari server: {data.decode('utf-8')}")