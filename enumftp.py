#!/usr/bin/python

import = socket
ip = input('[+] Enter the Ip Address: ')
port = input('[+] Enter the Port Number: ')
tcp = socket.socket()
tcp.connect((ip, port))

print("[+] Connecting with the Server")
banner = tcp.recv(1024) #I need to write in python3
print(banner)

print("[+] Sending user Name (anonymous/ftp)") # need to put the Anonymous option later
tcp.send('USER ftp\r\n')
user = tcp.recv(1024)
print(user)

print("[+] Sending password (anoymous/ftp)") # need to put the anonymous option here too
tcp.send("pass ftp\r\n")
pw = tcp.recv(1024)
print(pw)

print("[+] Testing cmd with help command")
tcp.send("HELP\r\n")
cmd = tcp.recv(2048)
print(cmd)

