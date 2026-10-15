# Week 3 - Task 29: NumPy Array Indexing
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_array_indexing.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 29: NumPy Array Indexing")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. 1-D Array Indexing
arr_1d = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr_1d)
print("First element (index 0):", arr_1d[0])
print("Last element (index -1):", arr_1d[-1])
print("Sum of 2nd and 4th element:", arr_1d[1] + arr_1d[3])

# 2. 2-D Array Indexing (Row, Column)
arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("\n2D Array:\n", arr_2d)
print("Element at Row 0, Column 1:", arr_2d[0, 1])
print("Element at Row 2, Column 2:", arr_2d[2, 2])
print("Last element in 2nd row (Row 1, Col -1):", arr_2d[1, -1])

# 3. 3-D Array Indexing
arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print("\n3D Array shape:", arr_3d.shape)
print("Accessing element at [0, 1, 2]:", arr_3d[0, 1, 2])  # Should be 6
print("Accessing element at [1, 0, 1]:", arr_3d[1, 0, 1])  # Should be 8
