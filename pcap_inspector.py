"""
DOCUMENTATION:
	File header length = 24 bytes
	Packet header length = 16 bytes
		- Packet data length  --> offset: 8
	Packet data: 
		- Link layer: 4 bytes
		- IP header:
			- Length in IHL   --> offset: 0 (IHL = first 4 bits)
			- Source IP       --> offset: 12
			- Destination IP  --> offset: 16
		- TCP header: 
			- ACK / SYN       --> offset: 13(SYN = 2nd bit, ACK = 5th bit)
"""

with open("./synflood.pcap", "rb") as file:
	data = file.read()

start = 24
total_count = 0
SYN_count = 0
ACK_count = 0

while True: 
	packet_header = data[start:start + 16]
	if len(packet_header) == 0:
		break
	next_packet_length = int(packet_header[8])
	packet_data = data[start + 16:start + 16 + next_packet_length]
	IP_header_length = (packet_data[4] & 0x0F) << 2
	TCP_start = 4 + IP_header_length
	source_port = int.from_bytes(packet_data[TCP_start:TCP_start + 2], "big")
	destination_port = int.from_bytes(packet_data[TCP_start + 2:TCP_start + 4], "big")
	syn = packet_data[TCP_start + 13] & 0x02 == 0x02
	ack = packet_data[TCP_start + 13] & 0x10 == 0x10

	print(f'{source_port} -> {destination_port} {" SYN" if syn else ""} {" ACK" if ack else ""}')

	if destination_port == 80 and syn:
		SYN_count += 1
	if source_port == 80 and ack:
		ACK_count += 1
	
	total_count += 1
	start += 16 + next_packet_length

print('Total number of packets: ', total_count)
print('Total number of SYN sent to port 80: ', SYN_count)
print('Total number of SYN acknowledged by the server:', ACK_count)
print(f'Percentage of ACKed SYNs: {ACK_count / SYN_count * 100:.2f}%')