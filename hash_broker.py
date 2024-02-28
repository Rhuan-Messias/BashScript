#!/usr/share/python

#I must use a wordlist and hash each word, after that I'll compare with the hash inputed to see if it matches
#if it match, then that's probably the answer, then I'll print the password cracked

import crypt

salt = "$1$n5vwmwca$"
password = "123"
crypt.crypt(password,salt)
