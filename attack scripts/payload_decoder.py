import sys
import json
from scapy.all import *

def parse_ascii_data(ascii_data):
    try:
        data_dict = json.loads(ascii_data)
        return data_dict
    except json.JSONDecodeError:
        print("Error: Unable to parse JSON data.")
        return None

def dissect_semtech_v2(pkt):
    # Semtech UDP protocol version 2 header structure:
    # [Version: 1 byte | Token: 2 bytes | Packet Type: 1 byte | Data: variable length]

    PACKET_TYPES = {
        0x00: "PUSH_DATA",
        0x01: "PUSH_ACK",
        0x02: "PULL_DATA",
        0x03: "PULL_RESP",
        0x04: "PULL_ACK",
        0x05: "TX_ACK",
    }

    # Extract fields from packet
    version = pkt[0]
    token = pkt[1:3]
    packet_type = pkt[3]

    # Print extracted fields
    print(f"Version: {version}")
    print(f"Token: {token.hex()}")
    print(f"Packet Type: {PACKET_TYPES.get(packet_type, 'Unknown')} ({hex(packet_type)})")

    # Check if packet type is PUSH_DATA, PULL_DATA, or TX_ACK
    if packet_type in {0x00, 0x02, 0x05}:
        gateway_id = pkt[4:12]
        data = pkt[12:]
        ascii_data = data.decode(errors='replace')
        parsed_data = parse_ascii_data(ascii_data)
        print(f"Gateway ID: {gateway_id.hex()}")
        print(f"Data: {data.hex()}\nASCII: {ascii_data}")
        if parsed_data is not None:
            print(f"Parsed Data: {parsed_data}")

    elif packet_type == 0x03:  # PULL_RESP
        data = pkt[4:]
        ascii_data = data.decode(errors='replace')
        parsed_data = parse_ascii_data(ascii_data)
        print(f"Data: {data.hex()}\nASCII: {ascii_data}")
        if parsed_data is not None:
            print(f"Parsed Data: {parsed_data}")

def extract_data_from_pcap(filename, packet_index=None):
    # Read pcap file
    pcap = rdpcap(filename)

    # Iterate through packets in pcap file
    for pkt in pcap:
        # Check if packet is UDP
        if UDP in pkt:
            udp = pkt[UDP]
            # Check if packet has a payload
            if Raw in pkt:
                raw_data = bytes(pkt[Raw])

                # Check if payload starts with Semtech UDP protocol version 2
                if raw_data[0] == 2:
                    current_index = pcap.index(pkt)
                    if packet_index is None or current_index == packet_index:
                        print(f"Packet {current_index}:")
                        dissect_semtech_v2(raw_data)

if __name__ == "__main__":
    if len(sys.argv) not in {2, 3}:
        print("Usage: python extract_data.py <pcap_file> [<packet_index>]")
        sys.exit(1)

    pcap_file = sys.argv[1]
    packet_index = int(sys.argv[2]) if len(sys.argv) == 3 else None
    extract_data_from_pcap(pcap_file, packet_index)
