# Week 3 - Task 39: NumPy Array Sorting
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_array_sort.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 39: NumPy Array Sorting")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. Sorting 1-D Numeric Array
num_arr = np.array([3, 7, 2, 0, 15, 9, 1])
print("Original 1-D Array :", num_arr)
sorted_num = np.sort(num_arr)
print("Sorted Array       :", sorted_num)

# 2. Sorting Alphabetical (String) Array
str_arr = np.array(['banana', 'cherry', 'apple', 'date', 'mango'])
print("\nOriginal Strings :", str_arr)
print("Sorted Strings   :", np.sort(str_arr))

# 3. Sorting Boolean Array
bool_arr = np.array([True, False, True, False, False, True])
print("\nSorted Booleans (False first, True second):", np.sort(bool_arr))

# 4. Sorting 2-D Array (Along rows/columns)
matrix = np.array([[3, 2, 4], [5, 0, 1]])
print("\nOriginal 2-D Matrix:\n", matrix)
print("Sorted along axis=1 (Within each row):\n", np.sort(matrix, axis=1))
print("Sorted along axis=0 (Within each column):\n", np.sort(matrix, axis=0))

# 5. Using np.argsort() to obtain sorted indices
indices = np.argsort(num_arr)
print("\n--- Indices that would sort num_arr (np.argsort) ---")
print("Sorted Indices:", indices)
print("Reconstructed array using indices:", num_arr[indices])
