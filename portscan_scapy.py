#!/usr/bin/python
import sys
from scapy.all import *

# Define the list of ports to be checked
ports = [21, 22, 23, 25, 80, 443, 110]

# Check if the destination IP address is provided as an argument
if len(sys.argv) != 2:
    print("Usage: {} <destination_ip>".format(sys.argv[0]))
    sys.exit(1)

# Define the destination IP address
destination_ip = sys.argv[1]

# Configure Scapy verbosity
conf.verb = 0 

# Loop over ports and send SYN packets
for port in ports:
    # Create the IP packet with the destination address
    p_ip = IP(dst=destination_ip)
    # Create the TCP packet with the destination port and SYN flag
    p_tcp = TCP(dport=port, flags="S")
    # Combine the IP and TCP packets
    packet = p_ip / p_tcp
    # Send the packet and get the response
    answer, noanswer = sr(packet, timeout=1)
    # Check the response
    if answer:
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))

