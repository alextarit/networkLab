import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 33030)  

while True:
    client_socket.sendto(input().encode("utf-8"), server_address)  

    data, server_address = client_socket.recvfrom(1024)  
    print("Сервер:", data.decode("utf-8"))

