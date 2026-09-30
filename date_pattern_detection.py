import re

# Take input from user
text = input("Enter the text: ")

# Regular expression for DD-MM-YYYY, DD/MM/YYYY, DD.MM.YYYY
pattern = r'\b\d{2}[-/.]\d{2}[-/.]\d{4}\b'

# Find all dates
dates = re.findall(pattern, text)

# Display the dates
print("Dates found:", dates)