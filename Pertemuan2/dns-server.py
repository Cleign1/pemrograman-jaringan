import socket

DNS_TABLE = {
    'www.google.com':'192.168.1.2',
    'youtube.com':'192.168.1.3',
    'www.facebook.com':'192.168.1.4'
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 100))
print("DNS Server is running...")

while True:
    data, address = server_socket.recvfrom(1024)
    print(f"Received request from {address}")
    domain_name = data.decode('utf-8')
    
    if domain_name in DNS_TABLE:
        ip_address = DNS_TABLE[domain_name]
        response = f"{domain_name} resolved to {ip_address}"
    else:
        response = f"{domain_name} not found"
        
    server_socket.sendto(response.encode('utf-8'), address)
    