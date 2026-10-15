# Week 2 - Task 49: Descriptive Statistics - Mean, Median, and Mode
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/python_ml_mean_median_mode.asp

import numpy as np
from scipy import stats
import statistics

print("=" * 65)
print(" Week 2 - Task 49: Measures of Central Tendency (Mean, Median, Mode)")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 65)

# Sample dataset: Vehicle speeds measured by sensor
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
print(f"Dataset: {speed}")
print(f"Total Observations (N): {len(speed)}")

# 1. Mean (Average value)
# Mathematical definition: sum(X) / N
mean_manual = sum(speed) / len(speed)
mean_numpy = np.mean(speed)
mean_builtin = statistics.mean(speed)

print("\n--- 1. Mean (Average) ---")
print(f"Formula : sum(x) / N")
print(f"Manual  : {mean_manual:.4f}")
print(f"NumPy   : {mean_numpy:.4f}")
print(f"Stats   : {mean_builtin:.4f}")

# 2. Median (Middle value after sorting)
sorted_speed = sorted(speed)
print(f"\n--- 2. Median (Middle Value) ---")
print(f"Sorted data: {sorted_speed}")
median_numpy = np.median(speed)
median_builtin = statistics.median(speed)
print(f"NumPy Median    : {median_numpy}")
print(f"Built-in Median : {median_builtin}")

# 3. Mode (Most frequently occurring value)
print(f"\n--- 3. Mode (Most Frequent Value) ---")
mode_builtin = statistics.mode(speed)
mode_scipy = stats.mode(speed)
print(f"Built-in Mode : {mode_builtin}")
print(f"SciPy Mode    : Value={mode_scipy.mode}, Count={mode_scipy.count}")

print("\n" + "=" * 65)
print("Summary Comparison:")
print(f"  Mean   = {mean_numpy:.2f}")
print(f"  Median = {median_numpy:.2f}")
print(f"  Mode   = {mode_builtin}")
print("=" * 65)
