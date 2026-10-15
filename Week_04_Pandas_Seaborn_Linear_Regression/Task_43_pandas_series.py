# Week 4 - Task 43: Pandas Series
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/pandas_series.asp

import pandas as pd

print("=" * 60)
print(" Week 4 - Task 43: Pandas Series")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# A Pandas Series is like a column in a table - a 1-D array holding data of any type.

# 1. Creating Series from a List
data_list = [10, 20, 30, 40]
series_default = pd.Series(data_list)
print("--- 1. Series with Default Numeric Index ---")
print(series_default)
print("First element (index 0):", series_default[0])

# 2. Creating Series with Custom Index Labels
series_custom = pd.Series(data_list, index=["x", "y", "z", "w"])
print("\n--- 2. Series with Custom String Index ---")
print(series_custom)
print("Accessing label 'y':", series_custom["y"])

# 3. Creating Series from a Python Dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
series_dict = pd.Series(calories)
print("\n--- 3. Series Created from Dictionary ---")
print(series_dict)

# 4. Creating Series selecting only specific dictionary keys
selected_series = pd.Series(calories, index=["day1", "day2"])
print("\n--- 4. Filtered Series with Specified Index Keys ---")
print(selected_series)
