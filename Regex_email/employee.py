import re

with open("employee.txt", "r") as f:
    data = f.read()

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, data)

print("Employee Email IDs:")

for email in emails:
    print(email)