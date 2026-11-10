# fix_the_functions.py


# Bug 1 (runtime): print_header() was called before it was defined (NameError)
def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)


def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        total = failed * minutes
        # Bug 2 (semantic): it always returned 0, now it returns total
        return total
    return 0


def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"


# Bug 1 fix (runtime): the call is now after the definition
print_header()
# Bug 3 (runtime): the parameter name is username, not user (TypeError)
print(login_line(username="sara", failed=4))
# Bug 4 (semantic): there was no print, so nothing was shown
print(login_line("omar", 1))