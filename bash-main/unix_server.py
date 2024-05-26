import socket
import os

def run_server(socket_name):
    # Удаляем старый сокет, если он существует
    try:
        os.remove(socket_name)
    except FileNotFoundError:
        pass

    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_socket.bind(socket_name)
    server_socket.listen(1)

    print(f"Listening on {socket_name}")
    try:
        while True:
            conn, _ = server_socket.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    message = data.decode('utf-8')
                    print(f"Received: {message}")
                    if message == "EXIT":
                        print("Shutting down server.")
                        return
    finally:
        server_socket.close()
        os.remove(socket_name)

if __name__ == "__main__":
    socket_name = input("Enter socket name (path to socket file): ")
    run_server(socket_name)
