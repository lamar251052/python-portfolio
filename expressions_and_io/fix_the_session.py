# fix_the_session.py
# This program reports a user's session time.

username = input("Username: ")
# runtime: input() returns a string, so total_seconds / 60 raised a TypeError. Fixed with int().
total_seconds = int(input("Session length in seconds: "))

# semantic: "/" gives a float but we need whole minutes. Fixed with "//".
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)
# semantic: without the "f" the line printed {username} literally. Fixed by adding f.
print(f"User: {username}")
# runtime: "str" + int raised a TypeError. Fixed by converting minutes with str().
print("Session: " + str(minutes) + " min " + str(seconds) + " s")
print("=" * 30)