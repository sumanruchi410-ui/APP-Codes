import csv
import re
import json

# Read book records from books.csv
books = []

with open("books.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        books.append(row)

# Display all book details
print("All Books:")
for book in books:
    print(book)

# Take keyword from user
keyword = input("\nEnter the starting keyword to search: ")

# Regular expression: title should START with the keyword
pattern = re.compile("^" + re.escape(keyword), re.IGNORECASE)

# Display matching records
print("\nMatching Books:")

found = False

for book in books:
    if pattern.search(book["Title"]):
        print(book)
        found = True

if not found:
    print("No matching books found.")