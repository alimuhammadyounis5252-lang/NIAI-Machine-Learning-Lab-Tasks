# Week 3 - NumPy Broadcasting, Universal Functions & Array I/O
# Student Name: Ali Muhammad Younis (886)
# Course Curriculum: Week 3 Day 3 & Day 4

import numpy as np
import os

print("=" * 65)
print(" Week 3: NumPy Broadcasting, Universal Functions & I/O")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 65)

# 1. Broadcasting Rules Demonstration
# Rule: Two dimensions are compatible when:
# 1. They are equal, or
# 2. One of them is 1.
matrix_3x3 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
vector_1x3 = np.array([1, 2, 3])

broadcasted_sum = matrix_3x3 + vector_1x3
print("\n--- 1. Broadcasting ---")
print("Matrix (3x3):\n", matrix_3x3)
print("Vector (1x3):", vector_1x3)
print("Matrix + Vector (Broadcasted result):\n", broadcasted_sum)

# 2. Universal Functions (ufuncs)
raw_features = np.array([1.0, 4.0, 9.0, 16.0, 25.0])

sqrt_vals = np.sqrt(raw_features)
exp_vals  = np.exp(np.array([0.0, 1.0, 2.0]))
log_vals  = np.log(np.array([1.0, np.e, np.e**2]))

print("\n--- 2. Universal Functions (ufuncs) ---")
print("np.sqrt:", sqrt_vals)
print("np.exp :", np.round(exp_vals, 4))
print("np.log :", log_vals)

# 3. Matrix Multiplications (Dot Product)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

matrix_prod = np.dot(A, B)      # or A @ B
element_prod = A * B

print("\n--- 3. Matrix Multiplication vs Element-wise ---")
print("Element-wise multiplication (A * B):\n", element_prod)
print("Matrix Dot Product (A @ B):\n", matrix_prod)

# 4. Data Loading and Saving (.npy and .csv)
npy_filename = "features_cache.npy"
csv_filename = "features_matrix.csv"

np.save(npy_filename, matrix_3x3)
np.savetxt(csv_filename, matrix_3x3, delimiter=",", fmt="%d")

loaded_npy = np.load(npy_filename)
loaded_csv = np.loadtxt(csv_filename, delimiter=",")

print("\n--- 4. Array I/O Verification ---")
print("Loaded from .npy binary file:\n", loaded_npy)
print("Loaded from .csv text file:\n", loaded_csv)

# Clean up
if os.path.exists(npy_filename): os.remove(npy_filename)
if os.path.exists(csv_filename): os.remove(csv_filename)
print("Cleanup: Temporary binary/csv files removed.")
