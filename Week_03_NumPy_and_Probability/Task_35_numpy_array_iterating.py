# Week 3 - Task 35: NumPy Array Iterating
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_array_iterating.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 35: NumPy Array Iterating")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. Standard Python Loop Iteration on 2-D Array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("--- Standard Nested Loop on 2-D Array ---")
for row in arr_2d:
    for val in row:
        print(val, end=" ")
print()

# 2. Advanced Iteration Using np.nditer()
# nditer is an efficient multidimensional iterator object
print("\n--- Iterating with np.nditer() ---")
for x in np.nditer(arr_2d):
    print(x, end=" ")
print()

# 3. Iterating Array With Different Data Types using op_dtypes and flags=['buffered']
print("\n--- Iterating as String Type with buffer flag ---")
for x in np.nditer(arr_2d, flags=['buffered'], op_dtypes=['S']):
    print(x, end=" ")
print()

# 4. Iterating with Step Size
arr_step = np.arange(1, 10).reshape(3, 3)
print("\n--- Iterating with Step Size (every 2nd item) ---")
for x in np.nditer(arr_step[:, ::2]):
    print(x, end=" ")
print()

# 5. Enumerated Iteration Using np.ndenumerate()
print("\n--- Enumerating with Coordinates using np.ndenumerate() ---")
for index, val in np.ndenumerate(arr_2d):
    print(f"Index {index} -> Value: {val}")
