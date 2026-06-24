import socket
from crypto_utils import KEY, encrypt_message
print(KEY)
from crypto_utils import decrypt_message

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

server.bind(
    ("127.0.0.1", 5000)
)

server.listen()

print("Server is waiting...")

client_socket, address = server.accept() 

print(f"Connected by {address}")

import threading


def receive_messages():
    while True:
        try:
            encrypted_message = client_socket.recv(4096)

            if not encrypted_message:
                break

            message = decrypt_message(
                encrypted_message
            )

            print(f"\nClient: {message}")

            if message.lower() == "exit":
                break

        except:
            break


def send_messages():
    while True:
        try:
            reply = input("You: ")

            encrypted_reply = encrypt_message(
                reply
            )

            client_socket.send(
                encrypted_reply
            )

            if reply.lower() == "exit":
                break

        except:
            break


receive_thread = threading.Thread(
    target=receive_messages
)

send_thread = threading.Thread(
    target=send_messages
)

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()

client_socket.close()
server.close()