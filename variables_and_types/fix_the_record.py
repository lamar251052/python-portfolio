# fix_the_record.py
# This program prints a short record about a network device.
device_name = "edge-router"
# Fixed: syntax error (a name cannot start with a digit)
second_ip = "192.0.2.1"
# Fixed: syntax error (class is a reserved keyword)
device_type = "router"
# Fixed: runtime error (int() cannot convert the text "twenty-two" bc it's a string )
port = int("22")
# Fixed: runtime error ( the variable is device_name, not device_nam)
print("Device:", device_name)
print("Backup IP:", second_ip)
print("Type:", device_type)
print("Port:", port)