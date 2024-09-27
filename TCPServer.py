# Jacob D Reeder
# CS 440

from socket import *

# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# Bind to port 12000
serverSocket.bind(('', 12000))
# Listen for incoming connections
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    # Accept connection from client
    connectionSocket, addr = serverSocket.accept()
    
    while True:
        try:
            # Receive message from client
            message = connectionSocket.recv(1024).decode()
            if not message:
                break
            
            # Capitalize the message
            message = message.upper()
            
            # Send the response back to the client
            connectionSocket.send(message.encode())
        except:
            break
    
    connectionSocket.close()
