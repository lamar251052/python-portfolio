#lamar
# log_analyzer.py
# Plan: every function works on the LOG text, line by line (splitlines).

ALERT_LIMIT = 3
LOG = """09:01 OK user=sara ip=192.0.2.5
09:02 FAILED user=admin ip=192.0.2.7
09:02 FAILED user=admin ip=192.0.2.7
09:03 FAILED user=root ip=192.0.2.7
09:04 OK user=omar ip=198.51.100.4
09:06 FAILED user=Sara ip=203.0.113.9
09:07 FAILED user=test ip=192.0.2.7
09:09 OK user=admin ip=192.0.2.5
09:12 FAILED user=guest ip=203.0.113.9
09:15 OK user=lina ip=198.51.100.8"""


def get_field(line, name):
    """Return the value after name= up to the next space or the end, or ''."""
    start = line.find(name + "=")
    if start == -1:
        return ""                      
    start = start + len(name + "=")           
    end = line.find(" ", start)
    if end == -1:                      
        end = len(line)
    return line[start:end]


def get_status(line):
    """Return the second word of the line: OK or FAILED."""
    if " FAILED " in line:
        return "FAILED"
    return "OK"


def count_status(status):
    """Return how many lines of LOG have this status."""
    count = 0
    for line in LOG.splitlines():
        if get_status(line) == status:
            count += 1
    return count


def show_summary():
    """Print the number of lines, failed and OK."""
    print(f"Lines: {len(LOG.splitlines())}")
    print(f"Failed: {count_status('FAILED')}")
    print(f"OK: {count_status('OK')}")


def search(keyword):
    """Print every line that has the keyword (any case) with its number."""
    matches = 0
    number = 0
    for line in LOG.splitlines():
        number += 1
        
        if keyword.lower() in line.lower():
            print(f"{number}: {line}")
            matches += 1
    print(f"Matches: {matches}")


def ip_report(ip):
    """Print time and user of each failure from ip, the total, and an alert."""
    total = 0
    for line in LOG.splitlines():
        if get_status(line) == "FAILED" and get_field(line, "ip") == ip:
            time = line[0:5]
            user = get_field(line, "user")
            print(time, user)
            total += 1
    print(f"Failed logins from {ip}: {total}")
    if total >= ALERT_LIMIT:
        print("ALERT: possible password guessing.")

def mask(word):
    """Return first and last letters with * between; only * if 2 letters or fewer."""
    if len(word) <= 2:
        return "*"
    return word[0] + "*" * (len(word) - 2) + word[-1]


def show_masked():
    """Print the whole LOG with every user name masked."""
    for line in LOG.splitlines():
        user = get_field(line, "user")
        
        print(line.replace("user=" + user, "user=" + mask(user)))


def show_menu():
    """Print the title and the five menu lines."""
    print("AUTH LOG ANALYZER")
    print("1. Summary")
    print("2. Search")
    print("3. IP report")
    print("4. Masked log")
    print("q. Quit")



show_menu()
while True:
    choice = input("Choice: ").strip().lower()
    if choice == "1":
        show_summary()
    elif choice == "2":
        search(input("Keyword: ").strip())
    elif choice == "3":
        ip_report(input("IP: ").strip())
    elif choice == "4":
        show_masked()
    elif choice == "q":
        print("Bye.")
        break
    else:
        print("Unknown choice.")