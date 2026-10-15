# Week 3 - Task 37: NumPy Array Splitting
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_array_split.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 37: NumPy Array Splitting")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# Splitting breaks one array into multiple subarrays.
# array_split() adjusts from the end if the array has fewer elements than required.

# 1. Splitting 1-D Array
arr_1d = np.array([1, 2, 3, 4, 5, 6])
print("Original 1-D Array:", arr_1d)

splits_3 = np.array_split(arr_1d, 3)
print("\n--- 1. Splitting into 3 parts ---")
for idx, sub in enumerate(splits_3, start=1):
    print(f"Part {idx}: {sub}")

splits_4 = np.array_split(arr_1d, 4)
print("\n--- 2. Splitting into 4 parts (Uneven) ---")
for idx, sub in enumerate(splits_4, start=1):
    print(f"Part {idx}: {sub}")

# 2. Splitting 2-D Array
matrix_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
print("\nOriginal 2-D Matrix:\n", matrix_2d)

# Split rows (axis=0)
row_splits = np.array_split(matrix_2d, 2, axis=0)
print("\n--- 3. Split 2-D Matrix along Rows (axis=0) ---")
print("Sub-matrix 1:\n", row_splits[0])
print("Sub-matrix 2:\n", row_splits[1])

# Split columns using hsplit
col_splits = np.hsplit(matrix_2d, 3)
print("\n--- 4. Split 2-D Matrix along Columns (np.hsplit) ---")
for idx, col in enumerate(col_splits, start=1):
    print(f"Column Part {idx}:\n{col}")
