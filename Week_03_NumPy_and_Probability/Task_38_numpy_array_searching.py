# Week 3 - Task 38: NumPy Array Searching
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_array_search.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 38: NumPy Array Searching")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

arr = np.array([1, 2, 3, 4, 5, 4, 4, 8, 9, 10])
print("Array:", arr)

# 1. Searching for Specific Values using np.where()
indices_of_4 = np.where(arr == 4)
print("\n--- 1. Search for value 4 ---")
print("Indices where value is 4:", indices_of_4[0])

# 2. Searching with Conditional Conditions (Even numbers)
even_indices = np.where(arr % 2 == 0)
print("\n--- 2. Search for Even Numbers (arr % 2 == 0) ---")
print("Indices of even numbers :", even_indices[0])
print("Values of even numbers  :", arr[even_indices])

# 3. Using np.searchsorted() (Binary search on sorted array)
# Finds the index where the specified value would be inserted to maintain order
sorted_arr = np.array([10, 20, 30, 40, 50])
print("\n--- 3. Binary Search with np.searchsorted() ---")
print("Sorted Array:", sorted_arr)
idx_35 = np.searchsorted(sorted_arr, 35)
print("Index to insert 35 to maintain sort order:", idx_35)

# Searching multiple values at once
indices_multi = np.searchsorted(sorted_arr, [15, 25, 45])
print("Indices to insert [15, 25, 45]:", indices_multi)
