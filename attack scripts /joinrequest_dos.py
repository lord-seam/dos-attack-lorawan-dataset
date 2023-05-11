from scapy.all import *

# Define the destination address and port
dest_addr = '192.168.56.104'
dest_port = 1700

# Define the payload as a string of hexadecimal characters
#payload_hex = '02c0ad02b4562d94afcda48d'

payloadx = '029cad00b4562d94afcda48d7b227278706b223a5b7b2274696d65223a22323032332d30342d31335430313a31303a30365a222c22746d6d73223a313336353338333432343635362c22746d7374223a313638313334383230362c226368616e223a302c2272666368223a302c2273746174223a312c2266726571223a3836382e312c22627264223a302c2272737369223a2d36302c2264617472223a225346374257313235222c226d6f6475223a224c4f5241222c22636f6472223a22342f35222c226c736e72223a372c2273697a65223a32332c2264617461223a2241414141414141414141414163314563453470376359505052346f683332633d227d5d2c2273746174223a7b2274696d65223a22323032332d30342d31332030313a31303a303620555443222c226c617469223a35302e38313831373439373637313133352c226c6f6e67223a342e34343332343031363537313034352c22616c7469223a302c2272786e62223a382c2272786f6b223a382c2272786677223a372c2261636b72223a372c2264776e62223a32382c2274786e62223a377d7d'

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
