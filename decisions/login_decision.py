# login_decision.py
# This program decides if a login is allowed.

MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

username = input("Username: ")
failed = int(input("Failed attempts so far: "))
password = input("Password: ")

if failed >= MAX_FAILED:
    print("Account locked.")
elif username != KNOWN_USER:
    print("Unknown user.")
elif password == STORED_PASSWORD:
    print("Access granted.")
else:
    print("Access denied. Attempts left:", MAX_FAILED - failed - 1)