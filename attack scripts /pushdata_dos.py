from scapy.all import *

# Define the destination address and port
dest_addr = '192.168.56.104'
dest_port = 1700

# Define the payload as a string of hexadecimal characters
#payload_hex = '02c0ad02b4562d94afcda48d'

payloadx = '02c0ad02b4562d94afcda48d'

# Convert the payload to binary format using the bytes.fromhex() method
#payload = bytes.fromhex(payload_hex)
payload = bytes.fromhex(payloadx)
# Define the IP and UDP headers
ip = IP(dst=dest_addr)
udp = UDP(dport=dest_port)

# Construct the packet by combining the headers and payload
packet = ip / udp / payload

# Prompt the user to enter the number of times the packet should be sent
num_times = int(input("Enter the number of times to send the packet: "))

# Send the packet to the destination IP address and port the specified number of times
for i in range(num_times):
    send(packet)

print("Packets sent!")
