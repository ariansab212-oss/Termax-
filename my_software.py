import os
db_file = "passwords_db.txt"
master_pin = "secure99"
print("====================================")
print("   ADVANCED SECURE PASSWORD MANAGER ")
print("====================================")
print("1. Save a new password")
print("2. View ENCRYPTED passwords")
print("3. View DECRYPTED (Original) passwords")
print("4. Exit")
print("====================================")
choice = input("Select an option (1-4): ")
if choice == "1":
    account = input("Enter Account Name: ")
    password = input("Enter Password: ")
    encrypted_pass = "".join(chr(ord(char) + 3) for char in password)
    with open(db_file, "a") as f:
        f.write(f"{account} : {encrypted_pass}\n")
    print("\n[✔] Password saved and encrypted successfully!")
elif choice == "2":
    if os.path.exists(db_file):
        print("\n--- Saved Accounts (Encrypted Data) ---")
        with open(db_file, "r") as f:
            print(f.read())
    else:
        print("\n[X] No passwords saved yet.")
elif choice == "3":
    pin = input("Enter Master PIN to reveal secrets: ")
    if pin == master_pin:
        if os.path.exists(db_file):
            print("\n--- Decrypted (Original) Passwords ---")
            with open(db_file, "r") as f:
                for line in f:
                    if ":" in line:
                        acc, sec = line.strip().split(" : ")
                        dec = "".join(chr(ord(c) - 3) for c in sec)
                        print(f"{acc} : {dec}")
        else:
            print("\n[X] No passwords saved yet.")
    else:
        print("\n[X] Wrong Master PIN! Access Denied.")
elif choice == "4":
    print("\nGoodbye!")
else:
    print("\n[X] Invalid option selected.")
