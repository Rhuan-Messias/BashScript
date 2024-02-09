#!/usr/bin/python

from scapy.all import * 
import sys

# verbosity configuration for scapy
conf.verb = 0
print("Up Hosts")
for ip in range(1,255): #remember that the range function only gets until max-1
    ip_testing = "172.30.0." + str(ip)
    p_ip = IP(dst=ip_testing)
    packet = p_ip/ICMP()
    answer,noanswer = sr(packet,timeout=1)
    if answer:
        print("Host is UP:", answer[0][1].src)
    else:
        pass
    
