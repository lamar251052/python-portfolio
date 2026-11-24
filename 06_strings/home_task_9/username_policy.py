#lamar
# username_policy.py
# Rules: 3 to 12 characters, starts with a letter, only letters/digits/_

MIN_LENGTH = 3
MAX_LENGTH = 12


def clean(username):
    """Return the username stripped and in lowercase."""
    return username.strip().lower()


def bad_character(username):
    """Return the first character that is not a letter, digit or _, or ''."""
    for ch in username:
        
        if not (ch.isalpha() or ch.isdigit() or ch == "_"):
            return ch
    return ""


def policy_problem(username):
    """Return the FIRST problem (length, first letter, bad character), or ''."""
    
    if len(username) < MIN_LENGTH or len(username) > MAX_LENGTH:
        return f"length must be {MIN_LENGTH} to {MAX_LENGTH}"

    if not username[0].isalpha():
        return "it must start with a letter"

    bad = bad_character(username)
    if bad != "":
        return f"the character {bad} is not allowed"

    return ""



username = clean(input("New username: "))
problem = policy_problem(username)

if problem == "":
    print(f"Accepted [{username}].")
else:
    print(f"Rejected [{username}]: {problem}.")