#!/usr/share/python

import hashlib
text = input("Type the Text to hash")
hashlib.md5(text).hexdigest()
