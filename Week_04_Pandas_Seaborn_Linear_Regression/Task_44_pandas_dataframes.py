# Week 4 - Task 44: Pandas DataFrames
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/pandas_dataframes.asp

import pandas as pd

print("=" * 60)
print(" Week 4 - Task 44: Pandas DataFrames")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# A Pandas DataFrame is a 2-dimensional data structure like a 2-D array, or a table with rows and columns.

# 1. Creating DataFrame from a Dictionary of Lists
data = {
    "Calories": [420, 380, 390],
    "Duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print("--- 1. DataFrame with Custom Named Index ---")
print(df)

# 2. Locating Rows using loc (Named Index)
print("\n--- 2. Accessing Rows with .loc ---")
print("Row 'day1':\n", df.loc["day1"])
print("\nRows 'day1' and 'day2':\n", df.loc[["day1", "day2"]])

# 3. Locating Rows using iloc (Integer Index)
print("\n--- 3. Accessing Rows with .iloc ---")
print("First row (iloc[0]):\n", df.iloc[0])

# 4. Adding and Removing Columns
df["Burn_Rate"] = df["Calories"] / df["Duration"]
print("\n--- 4. DataFrame after Adding 'Burn_Rate' Column ---")
print(df)
