import struct
import binascii
from Crypto.Cipher import AES
import base64

# Set these to the correct values for your device
MHDR = 0x00  # Join Request
DevEUI = "1122334455667788"  # Replace with your device EUI
AppEUI = "0000000000000000"  # Replace with your application EUI
AppKey = "00112233445566778899aabbccddeeff"  # Replace with your application key

for DevNonce_int in range(0, 65536):
    # Convert DevNonce to bytes
    DevNonce = DevNonce_int.to_bytes(2, byteorder='little')

    # Pack everything into a binary message
    msg = struct.pack(">B8s8sH",
                      MHDR,
                      binascii.unhexlify(AppEUI)[::-1],  # Little endian
                      binascii.unhexlify(DevEUI)[::-1],  # Little endian
                      DevNonce_int)  # Little endian
