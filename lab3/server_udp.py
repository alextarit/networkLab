import socket

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 33030)) 

while True:
    data, client_address = server_socket.recvfrom(1024)  
    print("Клиент:", data.decode("utf-8"))

    server_socket.sendto(input().encode("utf-8"), client_address)  
