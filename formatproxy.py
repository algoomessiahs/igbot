import re

proper_pattern = r'(\S+:\S+@\S+:\S+)'

with open('proxies.txt', 'r+') as file:
    lines = file.readlines()

    formatted_proxies = []

    for line in lines:
        match = re.search(proper_pattern, line)
        if not match:
            parts = re.split(r'[:@]', line.strip())
            if len(parts) == 4:
                formatted_proxy = f"{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}\n"
                formatted_proxies.append(formatted_proxy)
            else:
                formatted_proxies.append(line)
        else:
            formatted_proxies.append(line)

    file.seek(0)
    file.writelines(formatted_proxies)
    file.truncate()

print("Proxies in proxies.txt have been formatted.")
