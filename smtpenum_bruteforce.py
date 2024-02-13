#!/usr/bin/python

import socket,sys

file = open("list_of_usernames.txt") #put your wordlist for usernames here

for user in file:
  tcp = socket.socket()
  tcp.connect((sys.argv[1],25))
  banner = tcp.recv(1024)
  tcp.send("VRFY" + user)
  print(user)

