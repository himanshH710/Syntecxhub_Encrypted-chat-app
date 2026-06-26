import socket
import threading
from datetime import datetime
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

def log_message(message):

    current_time = datetime.now().strftime(
        "%H:%M:%S"
    )

    with open(
        "chat_history.txt",
        "a"
    ) as file:

        file.write(
            f"[{current_time}] {message}\n"
        )

def private_message(sender,receiver,message):
    if receiver in clients:
        target_socket = clients[receiver]
        formatted_message = (f"[Private] {sender}: {message}")
        encrypted_message =encrypt_message(formatted_message)
        target_socket.send(encrypted_message)

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
            log_message(formatted_message)

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

    log_message(f"{username} left the chat")

    client_socket.close()


print("Server is listening...")

while True:

    client_socket, address = server.accept()
    username = client_socket.recv(1024).decode()

    print(f"New Client Connected: {address}")

    clients[client_socket] = username

    log_message(f"{username} joined the chat")

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket,username)
    )

    thread.start()