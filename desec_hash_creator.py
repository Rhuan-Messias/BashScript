import hashlib as h
import base64

given_hash = b"desec"
step1 = h.md5(given_hash).hexdigest().encode()
step2 = base64.b64encode(step1)
step3 = h.sha1(step2).hexdigest()
print(step3)
