# Week 4 - Task 46: Pandas Data Analyzing
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/pandas_analyzing.asp

import pandas as pd
import numpy as np

print("=" * 60)
print(" Week 4 - Task 46: Pandas Data Analyzing")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# Create a realistic data table
data = {
    "Patient_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Age": [25, 47, 34, 62, 51, 39, 29, 58],
    "Blood_Pressure": [120, 140, 125, 155, 130, 118, 110, 145],
    "Cholesterol": [180, 240, 200, 260, 220, 195, 175, 230],
    "Diagnosis": ["Normal", "High", "Normal", "High", "Borderline", "Normal", "Normal", "High"]
}

df = pd.DataFrame(data)

# 1. Viewing Top and Bottom Rows with head() and tail()
print("--- 1. Viewing Top 3 Rows (head) ---")
print(df.head(3))

print("\n--- 2. Viewing Last 3 Rows (tail) ---")
print(df.tail(3))

# 2. Structural Information with info()
print("\n--- 3. Dataset Info (Columns, Non-Null counts, Dtypes) ---")
df.info()

# 3. Statistical Summary with describe()
print("\n--- 4. Statistical Summary (describe) ---")
print(df.describe())

# 4. Frequency distribution with value_counts()
print("\n--- 5. Category Counts (value_counts for Diagnosis) ---")
print(df["Diagnosis"].value_counts())

# 5. Applying Custom Function with apply()
df["Age_Group"] = df["Age"].apply(lambda a: "Senior" if a >= 50 else ("Middle" if a >= 35 else "Young"))
print("\n--- 6. DataFrame with Custom Computed Column via apply() ---")
print(df[["Patient_ID", "Age", "Age_Group", "Diagnosis"]])
