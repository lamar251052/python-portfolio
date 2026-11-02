# pin_space_table.py
# How long to try every PIN if the attacker does 10 guesses per second

GUESSES_PER_SECOND = 10

for digits in range(4, 9):  
    combinations = 10 ** digits
    seconds = combinations // GUESSES_PER_SECOND
    minutes = seconds // 60
    days = seconds // 86400  # 60 * 60 * 24
    print(f"{digits} digits: {combinations} PINs, {minutes} minutes, {days} days")