# fix_the_parser.py
LINE = "09:02 FAILED user=Admin ip=192.0.2.7"


def get_time(line):
    """Return the time: the first 5 characters."""
     # semantic: the last number in a slice  is not counted, so I need 5 not 4
    return line[0:5]


def get_user(line):
    """Return the user name in lowercase."""
    start = line.find("user=") + 5
    end = line.find(" ", start)
    user = line[start:end]
    # semantic: lower() returns a new string and does not change the old one, so I save it in user
    user = user.lower()
    return user


def is_failed(line):
    """Return True if the line reports a failed login."""
    # semantic: the log writes FAILED in capital letters, so "failed" never matched
    return "FAILED" in line


def hide_first(user):
    """Return user with its first letter replaced by *."""
    # runtime: strings cannot be changed by index , build a new string instead
    return "*" + user[1:]


print(f"Time: {get_time(LINE)}")
print(f"User: {get_user(LINE)}")
print(f"Failed: {is_failed(LINE)}")
print(f"Hidden: {hide_first('admin')}")
# runtime: there is no .len() for text, the right way is len()
print(f"Length: {len(LINE)}")