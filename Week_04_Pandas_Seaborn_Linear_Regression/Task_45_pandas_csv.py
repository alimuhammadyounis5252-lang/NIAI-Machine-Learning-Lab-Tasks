# Week 4 - Task 45: Pandas Reading and Handling CSV Files
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/pandas_csv.asp

import pandas as pd
import os

print("=" * 60)
print(" Week 4 - Task 45: Pandas CSV File Handling")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

csv_filename = "data_sample.csv"

# 1. Create a sample CSV file
sample_csv_content = """Duration,Pulse,Maxpulse,Calories
60,110,130,409.1
60,117,145,479.0
60,103,135,340.0
45,109,175,282.4
45,117,148,406.0
60,102,127,300.0
"""
with open(csv_filename, "w", encoding="utf-8") as f:
    f.write(sample_csv_content.strip())

# 2. Reading CSV using pd.read_csv()
df = pd.read_csv(csv_filename)

print("--- 1. Loaded CSV Content ---")
print(df)

# 3. Using to_string() to print entire DataFrame
print("\n--- 2. Full DataFrame as String using to_string() ---")
print(df.to_string())

# 4. Checking and Configuring display options
print(f"\nPandas default max_rows setting: {pd.options.display.max_rows}")

# Cleanup
if os.path.exists(csv_filename):
    os.remove(csv_filename)
    print("\nCleanup: Removed temporary CSV file.")
