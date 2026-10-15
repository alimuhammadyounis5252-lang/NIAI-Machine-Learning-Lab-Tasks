# Week 3 - Task 33: NumPy Array Shape
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_array_shape.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 33: NumPy Array Shape")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# The shape of an array is the number of elements in each dimension.
arr_1d = np.array([1, 2, 3, 4])
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# Creating a 5-D array using ndmin
arr_5d = np.array([1, 2, 3, 4], ndmin=5)

print("1-D Array Shape :", arr_1d.shape, f"({arr_1d.shape[0]} elements)")
print("2-D Array Shape :", arr_2d.shape, f"({arr_2d.shape[0]} rows, {arr_2d.shape[1]} columns)")
print("3-D Array Shape :", arr_3d.shape, f"(Depth: {arr_3d.shape[0]}, Rows: {arr_3d.shape[1]}, Cols: {arr_3d.shape[2]})")
print("5-D Array Shape :", arr_5d.shape)
print("5-D Array ndim  :", arr_5d.ndim)
