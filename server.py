import socket
import threading
from crypto_utils import decrypt_message, encrypt_message

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

server.bind(("127.0.0.1", 5000))
server.listen()

clients = {}


def broadcast(message, sender):
    for client in clients:

        if client != sender:
            try:
                client.send(message)
            except:
                pass


def handle_client(client_socket,username):

    while True:

        try:
            encrypted_message = client_socket.recv(4096)

            if not encrypted_message:
                break

            message = decrypt_message(
                encrypted_message
            )

            print(f"\n[{username}]: {message}")

            formatted_message = f"[{username}] {message}"

            encrypted_message = encrypt_message(
                formatted_message)

            broadcast(
                encrypted_message,client_socket
            )

        except:
            break

    if client_socket in clients:
        del clients[client_socket]

    print(f"[{username}] disconnected.")

    client_socket.close()


print("Server is listening...")

while True:

    client_socket, address = server.accept()
    username = client_socket.recv(1024).decode()

    print(f"New Client Connected: {address}")

    clients[client_socket] = username

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket,username)
    )

    thread.start()