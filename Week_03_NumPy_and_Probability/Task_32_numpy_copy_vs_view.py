# Week 3 - Task 32: NumPy Array Copy vs View
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_copy_vs_view.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 32: NumPy Array Copy vs View")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# The main difference between a copy and a view of an array:
# - A COPY owns the data and any changes made to the copy will not affect original array.
# - A VIEW does not own the data and any changes made to the view will affect original array.

orig_arr = np.array([10, 20, 30, 40, 50])

# 1. Creating a Copy
copied_arr = orig_arr.copy()
copied_arr[0] = 999

print("--- 1. Testing Copy ---")
print("Original Array:", orig_arr)
print("Copied Array  :", copied_arr)
print("Observation   : Modifying copied array did NOT affect the original array.")

# 2. Creating a View
view_arr = orig_arr.view()
view_arr[0] = 777

print("\n--- 2. Testing View ---")
print("Original Array:", orig_arr)
print("View Array    :", view_arr)
print("Observation   : Modifying view DIRECTLY affected the original array!")

# 3. Checking Ownership Using .base Attribute
# Every NumPy array has the attribute 'base' that returns None if the array owns the data.
print("\n--- 3. Checking Ownership (.base) ---")
print("copied_arr.base is None?", copied_arr.base is None, "-> (Owns its own data)")
print("view_arr.base is None?  ?", view_arr.base is None, "-> (Does NOT own data, refers to original)")
print("view_arr.base refers to orig_arr?", view_arr.base is orig_arr)
