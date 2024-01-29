#!/usr/bin/bash 
import socket as s
import sys

host = sys.argv[1]

print(host, "--->", s.gethostbyname(host))
