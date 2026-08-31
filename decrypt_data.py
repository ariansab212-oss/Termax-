encrypted_message = "KHOOR ZRUOG"
decrypted_message = ""
for char in encrypted_message:
    if char.isalpha():
        shifted = ord(char) - 3
        if shifted < ord("A"):
            shifted += 26
        decrypted_message += chr(shifted)
    else:
        decrypted_message += char
print("--- Data Decryption System ---")
print(f"Encrypted Text: {encrypted_message}")
print(f"Decrypted (Original) Text: {decrypted_message}")
