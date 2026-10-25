# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# Bug 1 (syntax): there was no colon after the if line
if len(password) < MIN_LENGTH:
    print("- Too short.")
# Bug 2 (semantic): this was elif, so it never run when the password was too short.
# Now it is a separate if, so both messages can print.
if password == username:
    print("- Same as the username.")

# Bug 3 (semantic): the >= 16 check was after >= MIN_LENGTH, so "long" never happened.
# The biggest condition must be checked first.
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"
# Bug 4 (semantic): the print was indented inside the else
print(f"Length: {len(password)} ({strength})")