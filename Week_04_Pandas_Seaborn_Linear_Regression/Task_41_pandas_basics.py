# Week 4 - Task 41: Pandas Basics
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/pandas_tutorial.asp

import pandas as pd

print("=" * 60)
print(" Week 4 - Task 41: Pandas Basics")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. Checking Pandas Version
print("Pandas Version:", pd.__version__)

# 2. Basic Dataset Creation
dataset = {
    'Cars': ["BMW", "Volvo", "Ford", "Tesla"],
    'Passings': [3, 7, 2, 8]
}

my_var = pd.DataFrame(dataset)

print("\n--- Pandas DataFrame Representation ---")
print(my_var)
print("\nType of my_var:", type(my_var))
