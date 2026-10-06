# type_check.py
# This program prints the type of several values and converts values between types.

# Predictions (written before running):
# 8080             int
# "8080"           str
# 99.5             float
# "198.51.100.7"   str
# 1_000            int

print(8080, type(8080))
print("8080", type("8080"))
print(99.5, type(99.5))
print("198.51.100.7", type("198.51.100.7"))
print(1_000, type(1_000))
print()
# Conversions: 
print(int("443"), type(int("443")))
print(str(8080), type(str(8080)))
print(float("2.5"), type(float("2.5")))

