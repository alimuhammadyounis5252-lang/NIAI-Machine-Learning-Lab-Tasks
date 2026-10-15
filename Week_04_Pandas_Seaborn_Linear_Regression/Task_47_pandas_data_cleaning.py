# Week 4 - Task 47: Pandas Data Cleaning Techniques
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/pandas_cleaning.asp

import pandas as pd
import numpy as np

print("=" * 60)
print(" Week 4 - Task 47: Pandas Data Cleaning Techniques")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# Create a dirty dataset with NaN values, wrong formats, and duplicates
raw_dirty_data = {
    "Duration": [60, 60, 60, 45, 45, 60, 60], # duplicate row 1 and row 6
    "Date": ['2026/12/01', '2026/12/02', '2026/12/03', '20261204', '2026/12/05', '2026/12/01', '2026/12/07'],
    "Pulse": [110, 117, 103, 109, 117, 110, np.nan],
    "Calories": [409.1, 479.0, np.nan, 282.4, 406.0, 409.1, 300.0]
}

df = pd.DataFrame(raw_dirty_data)
print("--- 1. Raw Dirty DataFrame ---")
print(df)

# 1. Checking Missing / Null Values
print("\nMissing values per column:\n", df.isnull().sum())

# 2. Imputing Missing Values with Mean
calories_mean = df["Calories"].mean()
df["Calories"] = df["Calories"].fillna(calories_mean)
print(f"\nImputed missing Calories with mean ({calories_mean:.1f}):")
print(df[["Duration", "Calories"]])

# 3. Filling remaining NaNs or dropping specific missing rows
df["Pulse"] = df["Pulse"].fillna(df["Pulse"].median())

# 4. Standardizing Date Format
df["Date"] = pd.to_datetime(df["Date"], errors='coerce', format='mixed')
print("\n--- 2. Date column after datetime parsing ---")
print(df[["Date", "Pulse", "Calories"]])

# 5. Removing Duplicates
print("\nChecking duplicates before cleaning:", df.duplicated().sum())
df = df.drop_duplicates()
print("Total rows remaining after drop_duplicates():", len(df))

print("\n--- 3. Cleaned and Sanitized DataFrame ---")
print(df.to_string())
