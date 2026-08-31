attempts = 0
correct_password = "secure_termax_99"
print("--- SYSTEM ACCES MONITOR ---")
while attempts < 3:
    user_input = input("Enter system security PIN: ")
    if user_input == correct_password:
        print("Access Granted! Logging in...")
        break
    else:
        attempts += 1
        print(f"Wrong PIN! Attempts left: {3 - attempts}")
if attempts == 3:
    print("ALERT: 3 failed attempts! System locked for security.")
