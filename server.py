import socket
from crypto_utils import KEY
print(KEY)
from crypto_utils import decrypt_message

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(
    ("127.0.0.1", 5000)
)

server.listen()

print("Server is waiting...")

client_socket, address = server.accept()

print(f"Connected by {address}")

encrypted_message = client_socket.recv(1024)

message = decrypt_message(
    encrypted_message
)

print(
    "Client says:",
    message
)

client_socket.close()
server.close()