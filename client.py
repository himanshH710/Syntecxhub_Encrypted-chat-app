import socket
from crypto_utils import KEY, decrypt_message
print(KEY)
from crypto_utils import encrypt_message

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(
    ("127.0.0.1", 5000)
)

import threading


def send_messages():
    while True:
        message = input("You: ")

        encrypted_message = encrypt_message(message)

        client.send(encrypted_message)

        if message.lower() == "exit":
            break


def receive_messages():
    while True:
        try:
            encrypted_reply = client.recv(4096)

            if not encrypted_reply:
                break

            reply = decrypt_message(
                encrypted_reply
            )

            print(f"\nServer: {reply}")

        except:
            break


send_thread = threading.Thread(
    target=send_messages
)

receive_thread = threading.Thread(
    target=receive_messages
)

send_thread.start()
receive_thread.start()

send_thread.join()
receive_thread.join()

client.close()