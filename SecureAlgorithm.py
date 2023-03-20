import base64
import random
import string

def generate_random_dict1():
    keys = list(string.ascii_lowercase)
    values = list(string.ascii_lowercase)
    
    return dict(zip(keys, values))
def generate_random_dict2():
    keys2 = list(string.ascii_uppercase)
    values2 = list(string.ascii_uppercase)
    
    return dict(zip(keys2, values2))
def merge_dicts(dict1, dict2):
    merged_dict = dict(dict1)
    merged_dict.update(dict2)
    return merged_dict

rand1= merge_dicts(generate_random_dict1(), generate_random_dict2())
rand2= merge_dicts(generate_random_dict1(), generate_random_dict2())
def encrypt1(plaintext):
    key = rand1
    ciphertext = ""
    for char in plaintext:
        if char in key:
            ciphertext += key[char]
        else:
            ciphertext += char
    return ciphertext
def decrypt1(ciphertext):
    key = rand1
    plaintext = ""
    for char in ciphertext:
        if char in key.values():
            for k, v in key.items():
                if v == char:
                    plaintext += k
        else:
            plaintext += char
    return plaintext


def encrypt2(plaintext):
    key1 = "nuok"
    ciphertext = ''
    for i in range(len(plaintext)):
        # Perform XOR operation between each character in plaintext and the corresponding character in the key
        ciphertext += chr(ord(plaintext[i]) ^ ord(key1[i % len(key1)]))
    return ciphertext

# Define a function to decrypt the ciphertext using XOR
def decrypt2(ciphertext):
    key1 = "nuok"
    plaintext = ''
    for i in range(len(ciphertext)):
        # Perform XOR operation between each character in ciphertext and the corresponding character in the key
        plaintext += chr(ord(ciphertext[i]) ^ ord(key1[i % len(key1)]))
    return plaintext

def encrypt3(plaintext):
    key = rand2
    ciphertext = ""
    for char in plaintext:
        # If the character is a letter, encrypt it using the key
        if char.isalpha():
            encrypted_char = key[char.lower()]
            ciphertext += encrypted_char
        # Otherwise, just append the character to the ciphertext
        else:
            ciphertext += char
    return ciphertext

def decrypt3(ciphertext):
    key = rand2
    plaintext = ""
    for char in ciphertext:
        # If the character is a letter, decrypt it using the key
        if char.isalpha():
            decrypted_char = key[char]
            plaintext += decrypted_char
        # Otherwise, just append the character to the plaintext
        else:
            plaintext += char
    return plaintext

def encrypt4(plaintext):
    key2 = 10
    try:
        key3 = int(key2)
    except ValueError:
        return "Error: Key must be a valid integer."

    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.isupper():
                ciphertext += chr((ord(c) + key3 - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(c) + key3 - 97) % 26 + 97)
        else:
            ciphertext += c
    return ciphertext

def decrypt4(ciphertext):
    key2 = 10
    try:
        key3 = int(key2)
    except ValueError:
        return "Error: Key must be a valid integer."

    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                plaintext += chr((ord(c) - key3 - 65) % 26 + 65)
            else:
                plaintext += chr((ord(c) - key3 - 97) % 26 + 97)
        else:
            plaintext += c
    return plaintext

def encrypt5(msg):
  key3 = "b3b00yc0er"
  enc = []
  for i in range(len(msg)):
    list_key = key3[i % len(key3)]
    list_enc = chr((ord(msg[i]) +
             ord(list_key)) % 256)
    enc.append(list_enc)
  return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decrypt5(code):
  key3 = "b3b00yc0er"
  dec = []
  enc = base64.urlsafe_b64decode(code).decode()
  for i in range(len(enc)):
   list_key = key3[i % len(key3)]
   list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)
   dec.append(list_dec)
  return "".join(dec)


def chained_encrypt(plaintext):
    encrypt1_text = encrypt1(plaintext)
    encrypt2_text = encrypt2(encrypt1_text)
    encrypt3_text = encrypt3(encrypt2_text)
    encrypt4_text = encrypt4(encrypt3_text)
    encrypt5_text = encrypt5(encrypt4_text)
    return (encrypt5_text)

def chained_decrypt(ciphertext):
    decrypt5_text = decrypt5(ciphertext)
    decrypt4_text = decrypt4(decrypt5_text)
    decrypt3_text = decrypt3(decrypt4_text)
    decrypt2_text = decrypt2(decrypt3_text)
    decrypt1_text = decrypt1(decrypt2_text)
    return (decrypt1_text)
    
