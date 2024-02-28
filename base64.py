#!/usr/share/python

import base64
text = input("type your text")
encode_text = base64.b64encode(text)
print(encode_text)
original_text = base64.b64decode(encode_text)
print(original_text)
