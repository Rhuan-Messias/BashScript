#!/usr/bin/python
#rewrite in python3 <-------------

import socket,sys

#check if it the arguments was input
if len(sys.argv) != 3: 
  print("[+] Example: python3 smtpenum.py 192.168.0.1 root")
  sys.exit(0)
  #this will connect to the IP in port 25 and VRFY verify if there's a root user

tcp = socket.socket()
tcp.connect((sys.argv[1],25))
banner = tpc.recv(1024)
print(banner)

tcp.send("VRFY root" + sys.argv[2] + "\r\n")
user = tcp.recv(1024)
print(user)
