import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 33030))

    print("Вы подключились к серверу. Можете начинать чат.")

    try:
        while True:
            data = client.recv(1024)
            print(f"Сервер: {data.decode('utf-8')}")

            message = input()
            client.send(message.encode("utf-8"))

    except KeyboardInterrupt:
        print("Чат завершен.")
        client.close()

if __name__ == "__main__":
    main()
