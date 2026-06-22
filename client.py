import socket

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(("127.0.0.1", 5000))

print("Enter a message to send to the server:")
message = input()

client.send(
    message.encode()
)

client.close()