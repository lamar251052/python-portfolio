# fix_the_stats.py
# Count failed logins and the average session length.
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Bug 1: failed = 0 was inside the loop, so it reset to 0 every time.
# moved it before the loop.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# Bug 2: the print was inside the loop, so it repeated 3 times.
# I moved it outside the loop so it prints once.
# Bug 3: // gives a whole number (30). I used / to get 30.0.
print(f"Average session: {total / count} minutes")

# Bug 4: range(1, 4) stops at 3. range stops before the last number,
# so I changed it to range(1, 5) to get Level 4.
for level in range(1, 5):
    print(f"Level {level}")

    # All four bugs are logic errors.