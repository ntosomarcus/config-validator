import json
import ipaddress

# to load json file
with open("config.json") as file:
    devices = json.load(file)

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def check_duplicates(devices): #function for checking the duplicates
    seen = set()
    duplicates = []

    for device in devices:
        ip = device["ip"]
        if ip in seen:
            duplicates.append(ip)
        else:
            seen.add(ip)

    return duplicates

errors = [] #list to contain the errors in the json file

for device in devices:
    if "hostname" not in device or "ip" not in device:
        errors.append(f"Missing fields in {device}")
        continue

    if not is_valid_ip(device["ip"]):
        errors.append(f"Invalid IP: {device['ip']}")

duplicates = check_duplicates(devices)

for dup in duplicates:
  errors.append(f"Duplicate IP found: {dup}")


#prints out the results
if not errors:
    print("Config is valid ✅")
else:
    print("Errors found:")
    for error in errors:
        print("-", error)
