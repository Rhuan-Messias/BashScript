#!/usr/share/python

import hashlib
text = input("Type the Text to hash")
hashlib.md5(text).hexdigest()
hashlib.sha1(text).hexdigest()
hashlib.sha256(text).hexdigest()
hashlib.sha512(text).hexdigest()
