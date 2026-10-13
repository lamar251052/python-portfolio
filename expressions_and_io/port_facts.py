# port_facts.py
# Sources:
# RFC 9293 (TCP): Source Port and Destination Port are 16 bits each in the TCP header.
# RFC 791 (IP): IPv4 addresses are fixed length of four octets (32 bits).

PORT_BITS = 16
IPV4_BITS = 32

port_count = 2 ** PORT_BITS
highest_port = 2 ** PORT_BITS - 1
ipv4_count = 2 ** IPV4_BITS

print(f"Possible port numbers: {port_count}")
print(f"Highest port number: {highest_port}")
print(f"Possible IPv4 addresses: {ipv4_count}")