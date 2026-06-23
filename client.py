import socket
from crypto_utils import KEY
print(KEY)
from crypto_utils import encrypt_message

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(
    ("127.0.0.1", 5000)
)

message = input(
    "Enter Message: "
)

encrypted_message = encrypt_message(
    message
)


client.send(
    encrypted_message
)

client.close()