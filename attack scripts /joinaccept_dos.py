from scapy.all import *

# Define the destination address and port
dest_addr = '192.168.56.102'
dest_port = 56300

# Define the payload as a string of hexadecimal characters

payloadx = '020fb4037b227478706b223a7b22696d6d65223a66616c73652c2272666368223a302c22706f7765223a31342c22616e74223a302c22627264223a302c22746d7374223a313638363334383230362c2266726571223a3836382e312c226d6f6475223a224c4f5241222c2264617472223a225346374257313235222c22636f6472223a22342f35222c2269706f6c223a747275652c2273697a65223a33332c2264617461223a22494c397a3158673558524f476f4f64344d7653774876495036475335383133444944496a6d62493354423152227d7d'

# Convert the payload to binary format using the bytes.fromhex() method
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
