-- Semtech UDP Protocol dissector for Wireshark
semtechudp_proto = Proto("SemtechUDP", "Semtech UDP Protocol")

-- Protocol fields
local fields = semtechudp_proto.fields
fields.version = ProtoField.uint8("semtechudp.version", "Protocol Version", base.DEC)
fields.token = ProtoField.uint16("semtechudp.token", "Random Token", base.DEC)
fields.identifier = ProtoField.uint8("semtechudp.identifier", "Packet Identifier", base.HEX)
fields.packet_type = ProtoField.string("semtechudp.type", "Packet Type")
fields.gateway_eui = ProtoField.new("Gateway EUI", "semtechudp.gateway", ftypes.BYTES)
fields.json_payload = ProtoField.string("semtechudp.json", "JSON payload")

local packet_types = {
    [0x00] = "PUSH_DATA",
    [0x01] = "PUSH_ACK",
    [0x02] = "PULL_DATA",
    [0x03] = "PULL_RESP",
    [0x04] = "PULL_ACK",
    [0x05] = "TX_ACK",
}

-- Dissect Packet
function semtechudp_proto.dissector(buffer, pinfo, tree)
    pinfo.cols.protocol = semtechudp_proto.name

    local subtree = tree:add(semtechudp_proto, buffer(), "Semtech UDP Data")
    subtree:add(fields.version, buffer(0,1))
    subtree:add(fields.token, buffer(1,2))

    local identifier = buffer(3,1):uint()
    subtree:add(fields.identifier, buffer(3,1))
    subtree:add(fields.packet_type, packet_types[identifier] or "Unknown")

    if identifier == 0x00 or identifier == 0x02 or identifier == 0x05 then
        subtree:add(fields.gateway_eui, buffer(4,8))
    end

    if identifier == 0x00 or identifier == 0x05 then
        if buffer:len() > 12 then
            subtree:add(fields.json_payload, buffer(12))
        end
    elseif identifier == 0x03 then
        if buffer:len() > 4 then
            subtree:add(fields.json_payload, buffer(4))
        end
    elseif identifier == 0x01 or identifier == 0x04 then
        -- No payload for PUSH_ACK and PULL_ACK
    else
        -- Handle other packet types here, if necessary
    end
end

-- Register protocol to handle UDP ports
local udp_port = DissectorTable.get("udp.port")
udp_port:add(1700, semtechudp_proto)
udp_port:add(56300, semtechudp_proto)
