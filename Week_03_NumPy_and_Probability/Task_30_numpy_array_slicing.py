# Week 3 - Task 30: NumPy Array Slicing
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_array_slicing.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 30: NumPy Array Slicing")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. 1-D Array Slicing [start:end:step]
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original 1D Array:", arr)
print("Slice [1:5]       :", arr[1:5])
print("Slice [4:]        :", arr[4:])
print("Slice [:4]        :", arr[:4])
print("Negative slice [-3:-1]:", arr[-3:-1])
print("Step slice [::2] (Every alternate):", arr[::2])
print("Reversed array [::-1]             :", arr[::-1])

# 2. 2-D Array Slicing [row_range, col_range]
matrix = np.array([
    [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33],
    [40, 41, 42, 43]
])
print("\nOriginal 2D Matrix:\n", matrix)

# Slice 2x2 submatrix from top-left
print("\nTop-Left 2x2 Submatrix [0:2, 0:2]:\n", matrix[0:2, 0:2])

# Slice all rows, column index 1
print("\nExtract Column 1 across all rows [:, 1]:\n", matrix[:, 1])

# Slice rows 1 to 3 and columns 1 to 3
print("\nCentral Submatrix [1:3, 1:3]:\n", matrix[1:3, 1:3])
