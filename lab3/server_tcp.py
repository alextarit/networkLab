import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 33030))
    server.listen(1)  # Подключение одного клиента

    print("Сервер запущен. Ожидание подключения клиента...")

    user, address = server.accept()
    print(f"Подключено к {address[0]}:{address[1]}")

    try:
        while True:
            message = input()
            user.send(message.encode("utf-8"))

            data = user.recv(1024)
            print(f"Клиент: {data.decode('utf-8')}")

    except KeyboardInterrupt:
        print("Сервер завершает работу.")
        server.close()

if __name__ == "__main__":
    main()
