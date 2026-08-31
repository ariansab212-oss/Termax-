correct_password = "termax_secure_123"
print("--- Termux Security System ---")
user_input = input("Please enter login password: ")
if user_input == correct_password:
    print("Access Granted! Welcome to system.")
else:
    print("Access Denied! Wrong password.")
