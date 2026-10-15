# Week 4 - Task 42: Pandas Installation & Getting Started
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/pandas_getting_started.asp

import pandas as pd
import numpy as np

print("=" * 60)
print(" Week 4 - Task 42: Pandas Installation & Setup")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# Verification that Pandas is correctly integrated with NumPy
print("[OK] Pandas successfully imported.")
print(f"Installed Version: {pd.__version__}")

# Creating sample time series data
dates = pd.date_range("2026-01-01", periods=5)
sample_df = pd.DataFrame(np.random.randn(5, 3), index=dates, columns=['Feature_A', 'Feature_B', 'Feature_C'])

print("\nSample Generated Time Series DataFrame:")
print(sample_df)
