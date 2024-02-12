#!/usr/bin/python

import = socket
ip = input('[+] Enter the Ip Address: ')
port = input('[+] Enter the Port Number: ')
tcp = socket.socket()
tcp.connect((ip, port))

banner = tcp.recv(1024) #I need to write in python3
print(banner)

tcp.send('USER ftp\r\n')
user = tcp.recv(1024)
print(user)
