import os
db_file = "passwords_db.txt"
print("====================================")
print("     ZMA SECURE PASSWORD MANAGER    ")
print("====================================")
print("1. Save a new password")
print("2. View saved passwords")
print("3. Exit")
print("====================================")
choice = input("Select an option (1-3): ")
if choice == "1":
    account = input("Enter Account Name (e.g. Facebook): ")
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
    print("\nGoodbye!")
else:
    print("\n[X] Invalid option selected.")
