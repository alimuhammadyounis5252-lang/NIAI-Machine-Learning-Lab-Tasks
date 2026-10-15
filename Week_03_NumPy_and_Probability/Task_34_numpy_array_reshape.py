# Week 3 - Task 34: NumPy Array Reshaping
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_array_reshape.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 34: NumPy Array Reshaping")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. Reshaping 1-D to 2-D Array
arr_12 = np.arange(1, 13)
print("Original 1-D Array (12 elements):\n", arr_12)

# Reshape into 4 rows of 3 columns
arr_4x3 = arr_12.reshape(4, 3)
print("\nReshaped to 4x3 (2-D):\n", arr_4x3)

# 2. Reshaping 1-D to 3-D Array
# Reshape into 2 arrays of 3 rows each, each row having 2 elements (2, 3, 2)
arr_2x3x2 = arr_12.reshape(2, 3, 2)
print("\nReshaped to 2x3x2 (3-D):\n", arr_2x3x2)

# 3. Using Unknown Dimension (-1)
# NumPy calculates the missing dimension automatically:
arr_auto = arr_12.reshape(2, 2, -1)
print("\nReshaped with -1 (2, 2, -1) -> automatically computed shape:", arr_auto.shape)

# 4. Flattening Arrays back to 1-D
# Flattening converts multidimensional array into 1D array
flattened_1 = arr_4x3.reshape(-1)
flattened_2 = arr_4x3.flatten()
print("\nFlattened using reshape(-1):", flattened_1)
print("Flattened using .flatten()   :", flattened_2)
