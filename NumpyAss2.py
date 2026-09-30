# Handle missing values in patient records using Pandas

import pandas as pd
import numpy as np

# Create DataFrame with some missing values
data = {
    "Name": ["Riya", "Aman", None, "Neha", "Raj"],
    "Age": [20, 22, 21, None, 24],
    "Weight": [55, None, 60, 58, 65],
    "Blood Pressure": [120, 130, None, 125, 135]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing numerical values using mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Weight"] = df["Weight"].fillna(df["Weight"].mean())
df["Blood Pressure"] = df["Blood Pressure"].fillna(df["Blood Pressure"].mean())

# Drop rows where Name is missing
df = df.dropna(subset=["Name"])

print("\nDataFrame after cleaning:")
print(df)