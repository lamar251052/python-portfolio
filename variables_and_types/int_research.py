# int_research.py
# I test which strings int() can change into a number.

# My predictions:
# " 22 " will work, because Python ignores the spaces.
# "+22" will work, because a plus sign is allowed.
# "0022" will work, because zeros at the start are ok.
# "2_2" will work, because one underscore between digits is ok.

print(int(" 22 "))
print(int("+22"))
print(int("0022"))
print(int("2_2"))

# All four worked and printed 22.
# Page I used: https://docs.python.org/3/library/functions.html#int