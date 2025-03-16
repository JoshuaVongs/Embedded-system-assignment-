import socket

def start_client():
    host = '127.0.0.1'  # Server IP
    port = 12345        # Port to connect to

    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send message to server
    message = "Hello from Client!"
    client_socket.send(message.encode())

    # Receive response from server
    response = client_socket.recv(1024).decode()
    print(f"Server Response: {response}")

    # Close connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
