import hashlib as h
import base64
import re

def escape_special_characters(word):
    # Define uma lista de caracteres especiais que precisam ser escapados
    special_characters = r'[@!$#%^&*()<>?/\|}{~:]'
    # Escapa cada caractere especial na palavra
    escaped_word = re.sub(f'([{special_characters}])', r'\\\1', word)
    return escaped_word

wordlist = "/usr/share/john/password.lst"
given_hash = "806825f0827b628e81620f0d83922fb2c52c7136"

with open(wordlist, "r", encoding="utf-8") as john_wordlist:
    for item in john_wordlist:
        # Escapa os caracteres especiais na palavra
        escaped_item = escape_special_characters(item.strip())
        step1 = h.md5(escaped_item.encode()).hexdigest().encode()
        step2 = base64.b64encode(step1)
        step3 = h.sha1(step2).hexdigest()

        if step3 == given_hash:
            print(f"Senha encontrada: {escaped_item}")
            break  # Encerra o loop quando a senha é encontrada
