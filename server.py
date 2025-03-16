import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port to listen on

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Allow up to 5 clients to connect

    print(f"Server is listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")

        # Receive data from client
        request = client_socket.recv(1024).decode()
        print(f"Client says: {request}")

        # Respond to client
        response = "Hello from Server!"
        client_socket.send(response.encode())

        # Close connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
