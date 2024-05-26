import socket

def run_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    try:
        while True:
            message = input("Enter message to send (type 'EXIT' to stop server): ")
            client_socket.sendall(message.encode('utf-8'))
            print(f"Sent: {message}")
            if message == "EXIT":
                break
    finally:
        client_socket.close()

if __name__ == "__main__":
    host = input("Enter server IP: ")
    port = int(input("Enter server port: "))
    run_client(host, port)
