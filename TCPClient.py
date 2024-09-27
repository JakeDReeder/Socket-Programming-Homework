# Jacob D Reeder
# CS 440

import time
import socket

# Server details
serverName = 'localhost'
serverPort = 12000

# Create a TCP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
clientSocket.connect((serverName, serverPort))

# Send 10 ping requests
for sequence_number in range(1, 11):
    # Create the ping message
    send_time = time.time()
    message = f"Ping {sequence_number} {send_time}"
    
    try:
        # Send the ping message
        clientSocket.send(message.encode())
        
        # Wait for the response from the server
        response = clientSocket.recv(1024).decode()
        recv_time = time.time()
        
        # Calculate RTT
        rtt = recv_time - send_time
        
        # Print the server response and RTT
        print(f"Received from server: {response}")
        print(f"RTT: {rtt:.4f} seconds")
        
    except socket.timeout:
        # If no response within 1 second, consider the packet lost
        print("Request timed out")
    
# Close the socket
clientSocket.close()
