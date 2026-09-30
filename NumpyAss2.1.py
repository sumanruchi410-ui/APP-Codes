# Pandas DataFrame with user input and missing values

import pandas as pd

n = int(input("Enter number of patients: "))

names = []
ages = []
weights = []
bp = []

for i in range(n):
    print("\nPatient", i + 1)

    names.append(input("Enter Name: "))

    age = input("Enter Age: ")
    ages.append(float(age) if age else None)

    weight = input("Enter Weight: ")
    weights.append(float(weight) if weight else None)

    pressure = input("Enter Blood Pressure: ")
    bp.append(float(pressure) if pressure else None)

data = {
    "Name": names,
    "Age": ages,
    "Weight": weights,
    "Blood Pressure": bp
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df)

# Fill missing numerical values using mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Weight"] = df["Weight"].fillna(df["Weight"].mean())
df["Blood Pressure"] = df["Blood Pressure"].fillna(df["Blood Pressure"].mean())

# Drop rows where Name is missing
df = df.dropna(subset=["Name"])

print("\nDataFrame after cleaning:")
print(df)