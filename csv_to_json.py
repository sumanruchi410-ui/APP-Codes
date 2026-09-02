import csv
import json

try:
    with open("input.csv", "r", newline="") as csv_file:
        data = list(csv.DictReader(csv_file))

    with open("output.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("CSV data successfully converted to JSON.")

except FileNotFoundError:
    print("Error: input.csv not found.")