# fix_the_rules.py
# This program checks a connection against three rules.
role = input("Role: ")
# runtime: input() returns text, and comparing text with a number crashes. Convert to int.
port = int(input("Port: "))
# semantic: "role = "admin"" assigns instead of comparing. Use == to get True/False.
is_admin = role == "admin"
# syntax: the operator is <=, not =<
is_system_port = port <= 1023
# semantic: "or 443" is always truthy. Compare port with each value.
is_web_port = port == 80 or port == 443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")