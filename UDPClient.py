# Jacob D Reeder
# CS 440

import time
import socket

# Server details
serverName = 'localhost'
serverPort = 12000

# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set a timeout of 1 second
clientSocket.settimeout(1)

# Send 10 ping requests
for sequence_number in range(1, 11):
    # Create the ping message
    send_time = time.time()
    message = f"Ping {sequence_number} {send_time}"
    
    try:
        # Send the ping message
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        
        # Wait for the response from the server
        response, serverAddress = clientSocket.recvfrom(1024)
        recv_time = time.time()
        
        # Calculate RTT
        rtt = recv_time - send_time
        
        # Print the server response and RTT
        print(f"Received from server: {response.decode()}")
        print(f"RTT: {rtt:.4f} seconds")
        
    except socket.timeout:
        # If no response within 1 second, consider the packet lost
        print("Request timed out")
    
# Close the socket
clientSocket.close()
