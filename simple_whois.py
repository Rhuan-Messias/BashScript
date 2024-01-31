#!/usr/bin/env python
import socket as s
from codecs import encode,decode  # Import encode function
import sys

# Establishing Python connection
my_socket = s.socket(s.AF_INET, s.SOCK_STREAM)  # Adjust AF_INET to AF_INET6 if using IPv6
my_socket2 = s.socket(s.AF_INET, s.SOCK_STREAM)
#iana whois will show us who is the referer
my_socket.connect(("whois.iana.org", 43))  # Update address if needed, (using domain is better cuz the IP can change) 

query = sys.argv[1] + "\r\n"
my_socket.send(encode(query, "utf-8"))  # Encode query before sending
answer = my_socket.recv(1024)  # Receive up to 1024 bytes of answer
my_socket.close()  # Close the socket


refer_list = (answer.decode('latin-1')).split()
refer = str(refer_list[19])
my_socket2.connect((f"{refer}",43))
my_socket2.send(encode(query, "utf-8")) 
local_answer =my_socket2.recv(1024)  
print("\n***** IANA WHOIS *****\n")
print(answer.decode('latin-1')) #decode the received bytes to latin-1, utf-8 didn't work 
print(f"\n***** {refer} *****\n")
print(local_answer.decode('latin-1'))
my_socket2.close()  # Close the socket
