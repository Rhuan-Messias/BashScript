#!/usr/bin/python
import socket as s 

print("Trying a FTP Server")
ip = input("Type the IP:")
port = 21

#you need to use str.encode to transform the str in bytes, otherwise mysocket wont recognize strings

mysocket = s.socket(s.AF_INET, s.SOCK_STREAM)
mysocket.connect((ip,port))
banner = mysocket.recv(1024)
print(banner)

print("Sending user")
mysocket.send(str.encode('USER root\r\n'))
banner = mysocket.recv(1024)
print(banner)

print("Sending Password")
mysocket.send(str.encode('PASS root\r\n'))
mysocket.recv(1024)
print(banner)
