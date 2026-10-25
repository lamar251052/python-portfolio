# risk_score.py
# This program calculates a login risk score and classifies it.
score = 0

failed = int(input("Failed attempts in the last hour: "))
hour = int(input("Login hour (0-23): "))
new_device = input("New device (yes/no): ")

# the three rules are separate if statements
if failed >= 3:
    score = score + 40
if hour < 6:
    score = score + 30
if new_device == "yes":
    score = score + 30

# the level is a chain
if score >= 70:
    level = "HIGH"
elif score >= 30:
    level = "MEDIUM"
else:
    level = "LOW"

print(f"Risk score: {score} ({level})")