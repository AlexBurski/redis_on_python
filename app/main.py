import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client_socket, client_address = server_socket.accept()

    response = "+PONG\r\n"
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(response.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
