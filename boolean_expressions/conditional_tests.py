# conditional_tests.py
# Ten conditional tests: prediction first, then the real result.
user = "analyst"
role = "viewer"
failed = 3
port = 22

print("Is user == \"analyst\"? I predict True.")
print(user == "analyst")

print("\nIs role != \"viewer\"? I predict False.")
print(role != "viewer")

print("\nIs failed > 3? I predict False.")
print(failed > 3)

print("\nIs port < 100? I predict True.")
print(port < 100)

print("\nIs failed >= 3? I predict True.")
print(failed >= 3)

print("\nIs port <= 21? I predict False.")
print(port <= 21)

print("\nIs failed >= 3 and port == 22? I predict True.")
print(failed >= 3 and port == 22)

print("\nIs user == \"admin\" or role == \"admin\"? I predict False.")
print(user == "admin" or role == "admin")

print("\nIs not (failed > 5)? I predict True.")
print(not (failed > 5))

print("\nIs role == \"viewer\" and port > 100? I predict False.")
print(role == "viewer" and port > 100)