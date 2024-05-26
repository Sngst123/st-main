import socket

def run_client(socket_name):
    client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        client_socket.connect(socket_name)
        while True:
            message = input("Enter message to send (type 'EXIT' to stop server): ")
            client_socket.sendall(message.encode('utf-8'))
            print(f"Sent: {message}")
            if message == "EXIT":
                break
    finally:
        client_socket.close()

if __name__ == "__main__":
    socket_name = input("Enter socket name (path to socket file): ")
    run_client(socket_name)
