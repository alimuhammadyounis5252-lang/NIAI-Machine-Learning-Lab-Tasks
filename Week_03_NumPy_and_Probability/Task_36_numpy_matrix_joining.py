# Week 3 - Task 36: NumPy Matrix & Array Joining
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_array_join.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 36: NumPy Array Joining / Concatenation")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print("Array 1:\n", arr1)
print("Array 2:\n", arr2)

# 1. Concatenation along Axis 0 (Rows)
concat_axis0 = np.concatenate((arr1, arr2), axis=0)
print("\n--- 1. np.concatenate(..., axis=0) [Vertical append] ---\n", concat_axis0)

# 2. Concatenation along Axis 1 (Columns)
concat_axis1 = np.concatenate((arr1, arr2), axis=1)
print("\n--- 2. np.concatenate(..., axis=1) [Horizontal append] ---\n", concat_axis1)

# 3. Stacking along a new axis (np.stack)
stacked = np.stack((arr1, arr2), axis=0)
print("\n--- 3. np.stack (New dimension created) Shape:", stacked.shape, "---\n", stacked)

# 4. Helper Stacking Functions
# hstack: Stacking along rows (horizontal)
# vstack: Stacking along columns (vertical)
# dstack: Stacking along height (depth)
print("\n--- 4. Helper Stacking Functions ---")
print("np.hstack:\n", np.hstack((arr1, arr2)))
print("np.vstack:\n", np.vstack((arr1, arr2)))
print("np.dstack shape:", np.dstack((arr1, arr2)).shape)
