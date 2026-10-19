# truth_research.py
# Source: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
#
# Predictions:
# bool("")      > False: an empty string has length zero, so it counts as empty.
# bool("0")     > True:  it is a string with one character in it, so it is not empty.
#                         The text "0" is not the number 0.
# bool(0)       > False: zero counts as False.
# bool(0.0)     > False: the float zero is also a zero.
# bool("False") > True:  it is a non-empty string; Python does not read the word inside.

print(bool(""))
print(bool("0"))
print(bool(0))
print(bool(0.0))
print(bool("False"))