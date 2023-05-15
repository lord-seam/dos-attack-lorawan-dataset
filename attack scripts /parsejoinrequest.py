import json
import codecs
import base64

# Hex dump as string
hex_dump = '029cad00b4562d94afcda48d7b227278706b223a5b7b2274696d65223a22323032332d30342d31335430313a31303a30365a222c22746d6d73223a313336353338333432343635362c22746d7374223a313638313334383230362c226368616e223a302c2272666368223a302c2273746174223a312c2266726571223a3836382e312c22627264223a302c2272737369223a2d36302c2264617472223a225346374257313235222c226d6f6475223a224c4f5241222c22636f6472223a22342f35222c226c736e72223a372c2273697a65223a32332c2264617461223a2241414141414141414141414163314563453470376359505052346f683332633d227d5d2c2273746174223a7b2274696d65223a22323032332d30342d31332030313a31303a303620555443222c226c617469223a35302e38313831373439373637313133352c226c6f6e67223a342e34343332343031363537313034352c22616c7469223a302c2272786e62223a382c2272786f6b223a382c2272786677223a372c2261636b72223a372c2264776e62223a32382c2274786e62223a377d7d'  # Add the rest of your hex dump here

# Convert hex dump to bytes
byte_data = codecs.decode(hex_dump, 'hex')

# Find the start and end of the JSON object in bytes
start = byte_data.find(b'{')
end = byte_data.rfind(b'}') + 1

# Extract the JSON object and decode to a string
json_string = byte_data[start:end].decode()

# Load as JSON
json_data = json.loads(json_string)

# Parse data
rxpk_data = json_data['rxpk'][0]  # Parsing the first received packet
stat_data = json_data['stat']

# Print data
print('Received Packet Data:')
print(f'Time: {rxpk_data["time"]}')
print(f'GPS Time of pkt RX: {rxpk_data["tmms"]}')
print(f'Internal Timestamp: {rxpk_data["tmst"]}')
print(f'IF Channel for RX: {rxpk_data["chan"]}')
print(f'RF Chain for RX: {rxpk_data["rfch"]}')
print(f'Status: {rxpk_data["stat"]}')
print(f'Frequency: {rxpk_data["freq"]}')
print(f'Board: {rxpk_data["brd"]}')
print(f'RSSI: {rxpk_data["rssi"]}')
print(f'Data Rate: {rxpk_data["datr"]}')
print(f'Modulation: {rxpk_data["modu"]}')
print(f'Coding Rate: {rxpk_data["codr"]}')
print(f'SNR Ratio: {rxpk_data["lsnr"]}')
print(f'Size: {rxpk_data["size"]}')
print(f'Data: {rxpk_data["data"]}')

print('\nStatus Data:')
print(f'Time: {stat_data["time"]}')
print(f'Latitude: {stat_data["lati"]}')
print(f'Longitude: {stat_data["long"]}')
print(f'Altitude: {stat_data["alti"]}')
print(f'Packets Received: {stat_data["rxnb"]}')
print(f'Packets with Correct CRC: {stat_data["rxok"]}')
print(f'Packets Forwarded: {stat_data["rxfw"]}')
print(f'Acknowledged Upstream Datagrams: {stat_data["ackr"]}')
print(f'Downlink Datagrams Received: {stat_data["dwnb"]}')
print(f'Packets Emitted: {stat_data["txnb"]}')

# Decode Base64 join request payload
data_base64 = rxpk_data['data']

# Decode Base64
data_bytes = base64.b64decode(data_base64)

# Parse join request payload
mhdr = data_bytes[0]  # Mac Header
appeui = data_bytes[1:9][::-1]  # LSB
deveui = data_bytes[9:17][::-1]  # LSB
mic = data_bytes[-4:]  # Message Integrity Code

# Convert bytes to hex for easier interpretation
mhdr_hex = format(mhdr, '02x')
appeui_hex = appeui.hex()
deveui_hex = deveui.hex()
mic_hex = mic.hex()

print('\nJoin Request Payload:')
print(f'MHDR: {mhdr_hex}')
print(f'AppEUI: {appeui_hex}')
print(f'DevEUI: {deveui_hex}')
print(f'MIC: {mic_hex}')
