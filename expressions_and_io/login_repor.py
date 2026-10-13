# login_report.py
# This program prints a short login report for a user.

MAX_LOGIN_ATTEMPTS = 5

username = input("Username: ")
failed_attempts = int(input("Failed attempts: "))

attempts_left = MAX_LOGIN_ATTEMPTS - failed_attempts

print("=" * 30)
print("LOGIN REPORT")
print("=" * 30)
print(f"User:\t\t{username}")
print(f"Failed:\t\t{failed_attempts}")
print(f"Attempts left:\t{attempts_left}")