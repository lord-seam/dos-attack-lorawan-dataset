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

    # Prepare B0 block for cmac computation
    # 0x49 is the constant value used in MIC computation for Join Request in LoRaWAN 1.0
    # Remaining values are zero-padded as per LoRaWAN 1.0 specification for cmac computation
    B0 = b'\x49' + b'\x00' * 7 + b'\x00' + b'\x00' + b'\x00' + b'\x00' + struct.pack(">B", len(msg)) + msg

    # Calculate the MIC
    key = binascii.unhexlify(AppKey)
    cipher = AES.new(key, AES.MODE_ECB)
    mic = cipher.encrypt(B0)[-4:]

    # Append the MIC to the end of the message
    msg += mic

    # Base64 encode the message
    msg_base64 = base64.b64encode(msg)

    print(f"DevNonce: {DevNonce_int}, Join Request (hex): {binascii.hexlify(msg).decode()}, Join Request (base64): {msg_base64.decode()}")
