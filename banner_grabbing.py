#!/usr/bin/python
import socket as s

ip = input("Type the IP address:")
port = int(input("Type the port:"))

mysocket = s.socket(s.AF_INET, s.SOCK_STREAM)
mysocket.connect((ip,port))
banner = mysocket.recv(1024)
print(banner)
