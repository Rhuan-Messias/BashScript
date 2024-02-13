#!/usr/bin/python

#rewrite in python 3 

import socket,sys,re

file = open("list_of_usernames.txt") #put your wordlist for usernames here

#when the user exists, the code 252 is returned
#when the user doesn't exist, the code 550 is returned

for user in file:
  tcp = socket.socket()
  tcp.connect((sys.argv[1],25))
  banner = tcp.recv(1024)
  tcp.send("VRFY" + user)
  print(user)

if re.search("252", user): #let's search in the user variable for the positive code 252 with re library
  print("User Found:" + user.strip("252 2.0.0")) #let's strip the part of the answer we don't want, for a cleaner results
  
