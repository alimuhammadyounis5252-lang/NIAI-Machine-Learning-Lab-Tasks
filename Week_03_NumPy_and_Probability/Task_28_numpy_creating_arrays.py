# Week 3 - Task 28: Creating NumPy Arrays
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_creating_arrays.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 28: Creating NumPy Arrays")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. 0-D, 1-D, 2-D, and 3-D Arrays
arr_0d = np.array(42)
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(f"0-D Array: {arr_0d} | ndim: {arr_0d.ndim}")
print(f"1-D Array: {arr_1d} | ndim: {arr_1d.ndim}")
print(f"2-D Array:\n{arr_2d} | ndim: {arr_2d.ndim}")
print(f"3-D Array:\n{arr_3d} | ndim: {arr_3d.ndim}")

# 2. Built-in NumPy Array Initialization Routines
zeros_arr = np.zeros((2, 3))
ones_arr = np.ones((3, 2))
range_arr = np.arange(10, 30, 5)
linspace_arr = np.linspace(0, 1, 5)  # 5 evenly spaced values between 0 and 1
identity_mat = np.eye(3)             # 3x3 Identity matrix
full_arr = np.full((2, 2), 7)        # Constant filled array

print("\n--- Built-in Initialization Routines ---")
print("np.zeros((2, 3)):\n", zeros_arr)
print("np.ones((3, 2)):\n", ones_arr)
print("np.arange(10, 30, 5):", range_arr)
print("np.linspace(0, 1, 5):", linspace_arr)
print("np.eye(3) [Identity Matrix]:\n", identity_mat)
print("np.full((2, 2), 7):\n", full_arr)
