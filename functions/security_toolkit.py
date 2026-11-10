# security_toolkit.py
# A menu program with port, password and PIN checks.

MIN_LENGTH = 8


def border(width):
    """Print + then width + 2 dashes, then +."""
    print("+" + "-" * (width + 2) + "+")


def show_box(text):
    """Print the text inside a box."""
    border(len(text))
    print("| " + text + " |")
    border(len(text))


def show_menu():
    """Print the title and the menu lines."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")


def port_range(port):
    """Return invalid, system, user or dynamic for a port number."""
    if port < 0 or port > 65535:
        return "invalid"
    elif port <= 1023:
        return "system"
    elif port <= 49151:
        return "user"
    else:
        return "dynamic"


def check_port():
    """Ask for a port and show its range in a box."""
    port = int(input("Port: "))
    show_box(f"Port {port}: {port_range(port)}")


def password_problem(password, username):
    """Return the first problem of the password, or an empty string."""
    if len(password) < MIN_LENGTH:
        return "too short"
    if password == username:
        return "same as the username"
    return ""


def check_password():
    """Ask for username and password and show the result in a box."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)
    if problem != "":
        show_box("Rejected: " + problem)
    else:
        show_box("Password accepted")


def days_to_guess(digits, per_second):
    """Return the whole days needed to try every PIN."""
    return 10 ** digits // per_second // 86400


def check_pin():
    """Ask for PIN digits and guesses per second, show the days in a box."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))
    days = days_to_guess(digits, per_second)
    show_box(f"{digits} digits: {days} days")


show_menu()
checks = 0

while True:
    choice = input("Choice (1, 2, 3, or q): ")
    if choice == "1":
        check_port()
        checks += 1
    elif choice == "2":
        check_password()
        checks += 1
    elif choice == "3":
        check_pin()
        checks += 1
    elif choice == "q":
        break
    else:
        print("Unknown choice.")

show_box(f"Checks done: {checks}")
