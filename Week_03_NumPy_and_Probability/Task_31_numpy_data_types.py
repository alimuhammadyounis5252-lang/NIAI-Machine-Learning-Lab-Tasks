# Week 3 - Task 31: NumPy Data Types and Type Casting
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_data_types.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 31: NumPy Data Types")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. Checking Data Types of Arrays
arr_int = np.array([1, 2, 3, 4])
arr_float = np.array([1.5, 2.8, 3.14])
arr_str = np.array(["Python", "NumPy", "PyTorch"])
arr_bool = np.array([True, False, True])

print(f"Integer Array dtype : {arr_int.dtype}")
print(f"Float Array dtype   : {arr_float.dtype}")
print(f"String Array dtype  : {arr_str.dtype}")
print(f"Boolean Array dtype : {arr_bool.dtype}")

# 2. Creating Arrays with Explicit Data Types
arr_i4 = np.array([1, 2, 3, 4], dtype='i4')  # 4-byte integer (int32)
arr_f8 = np.array([1, 2, 3, 4], dtype='f8')  # 8-byte float (float64)
print(f"\nExplicit int32 array: {arr_i4} (dtype: {arr_i4.dtype})")
print(f"Explicit float64 array: {arr_f8} (dtype: {arr_f8.dtype})")

# 3. Converting Data Types Using astype()
original_floats = np.array([1.1, 2.8, 3.9, 4.2])
converted_ints = original_floats.astype('i')
converted_bools = original_floats.astype(bool)

print("\n--- Type Casting with astype() ---")
print("Original Floats :", original_floats, original_floats.dtype)
print("Casted to Int   :", converted_ints, converted_ints.dtype)
print("Casted to Bool  :", converted_bools, converted_bools.dtype)
