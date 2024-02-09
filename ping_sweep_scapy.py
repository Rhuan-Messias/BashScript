#!/usr/bin/python

from scapy.all import * 
import sys

# Verbosity configuration for Scapy
conf.verb = 0 

#here i need to make an option if none ip were typed
#explaining how to use this small script
#remember to set 2> /dev/null to remove the warnings

print("Active Hosts:")
for ip in range(1, 255):
    dst_ip = f"{sys.argv[1]}.{ip}"
    packet = IP(dst=dst_ip) / ICMP()
    reply = sr1(packet, timeout=1, verbose=False)
    
    if reply is not None:
        print(f"Host {dst_ip} is active")
    else:
        pass
