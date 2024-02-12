#!/usr/bin/python

import = socket
ip = input('[+] Enter the Ip Address: ')
port = input('[+] Enter the Port Number: ')
tcp = socket.socket()
tcp.connect((ip, port))

banner = tcp.recv(1024) #I need to write in python3
print(banner)

#Passing my user to the ftp server
tcp.send('USER ftp\r\n')
user = tcp.recv(1024)
print(user)

#Passing the password to the ftp server
tcp.send("pass ftp\r\n")
pw = tcp.recv(1024)
print(pw)

tcp.send("HELP\r\n")
cmd = tcp.recv(2048)
print(cmd)

