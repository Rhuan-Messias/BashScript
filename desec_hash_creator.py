import hashlib as h
import base64

wordlist =  "/usr/share/john/password.lst"
given_hash = b"desec"

with open(wordlist, "r", encoding="utf-8") as john_wordlist:
    for item in john_wordlist:
        step1 = h.md5(given_hash).hexdigest().encode()
        step2 = base64.b64encode(step1)
        step3 = h.sha1(step2).hexdigest()

        if step3 == given_hash:
            print(f"{step3} : {item}")
        else:
            pass
