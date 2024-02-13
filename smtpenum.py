#!/usr/bin/python
#rewrite in python3 <-------------

import socket

ip = input("[+] Enter the IP Address: ")

tcp = socket.socket()
tcp.connect((ip,25))
banner = tpc.recv(1024)

print(banner)
