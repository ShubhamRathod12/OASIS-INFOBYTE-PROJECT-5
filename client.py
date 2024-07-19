import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to connect to

def receive_messages(client_socket):
    """Receive messages from the server and print them"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
            else:
                break
        except:
            break

def start_client():
    """Start the client and handle sending/receiving messages"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        threading.Thread(target=receive_messages, args=(client_socket,)).start()

        print("Connected to the chat server. Type your messages below.")

        while True:
            message = input()
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode('utf-8'))

        client_socket.close()

if __name__ == "__main__":
    start_client()

