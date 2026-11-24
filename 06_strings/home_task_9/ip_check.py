#lamar
# ip_check.py 
# split the address by dots and check each part one by one.


def is_valid_part(part):
    """Return True if part has only digits and its value is 255 or less."""
    
    if not part.isdigit():
        return False
    
    return int(part) <= 255


def ip_problem(address):
    """Return the FIRST problem in the address, or an empty string."""
    
    if address.count(".") != 3:
        return "Invalid: it needs exactly 3 dots."

    
    for part in address.split("."):
        if part == "":
            return "Invalid: a part is empty."
        if not is_valid_part(part):
            return f"Invalid: {part} is not a number from 0 to 255."

    
    return ""



address = input("IPv4 address: ").strip()
problem = ip_problem(address)

if problem == "":
    print(f"{address} is valid.")
else:
    print(problem)