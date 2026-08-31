secret_message = "HELLO WORLD"
encrypted_message = ""
for char in secret_message:
    if char.isalpha():
        shifted = ord(char) + 3
        if shifted > ord("Z"):
            shifted -= 26
        encrypted_message += chr(shifted)
    else:
        encrypted_message += char
print("--- Data Encryption System ---")
print(f"Original Text: {secret_message}")
print(f"Encrypted Text (Secret): {encrypted_message}")
