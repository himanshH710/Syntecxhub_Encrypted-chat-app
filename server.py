import socket

# Create a TCP socket

server = socket.socket(             
    socket.AF_INET,          # IPv4
    socket.SOCK_STREAM       # TCP
)                            # Create an IPv4 TCP socket.

server.bind(("127.0.0.1", 5000))    #Bind the socket to an address and port.  
                                    #"127.0.0.1" is the loopback address, which means the server will only accept connections from the local machine.

server.listen(5)                    #Listen for incoming connections. The argument specifies the maximum number of queued connections.

print("Server is waiting for a connection...")

client_socket, address = server.accept()  #Accept an incoming connection. This method blocks until a client connects, and returns a new socket object for the connection and the address of the client.

message = client_socket.recv(1024)  #Receive data from the client. The argument specifies the maximum amount of data to be received at once (in bytes).

message = message.decode()   #Decode the received bytes into a string using the default UTF-8 encoding.

print(f"Received message from {address}: {message}")  #Print the received message along with the client's address.

client_socket.close()  #Close the client socket to free up resources.

server.close()  #Close the server socket to free up resources.