import SecureAlgorithm as secure

text = "Hello world"

ciphertext = secure.chained_encrypt(text)
print("Ciphertext:", ciphertext)
plaintext = secure.chained_decrypt(ciphertext)
print("Plaintext:", plaintext)


