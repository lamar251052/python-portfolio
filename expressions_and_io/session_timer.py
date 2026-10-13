# session_timer.py
# This program converts a session length in seconds to minutes and seconds.

total_seconds = int(input("Session length in seconds: "))

minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"Session length: {minutes} minutes and {seconds} seconds")

# Test outputs:
# Input 905 > Session length: 15 minutes and 5 seconds
# Input 60  > Session length: 1 minutes and 0 seconds
# Input 59  > Session length: 0 minutes and 59 seconds