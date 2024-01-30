#!/usr/bin/python
import socket as s
import sys

for port in range (1,65535):
    mysocket = s.socket(s.AF_INET, s.SOCK_STREAM)
    if mysocket.connect_ex((sys.argv[1],port)) == 0:
        print("port",port,"[ABERTA]")
        mysocket.close()

