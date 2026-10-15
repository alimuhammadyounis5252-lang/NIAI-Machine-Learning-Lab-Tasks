# Week 4 - Task 48: Pandas Data Correlations
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/pandas_correlations.asp

import pandas as pd

print("=" * 60)
print(" Week 4 - Task 48: Pandas Data Correlation")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# A great aspect of the Pandas module is the corr() method.
# The corr() method calculates the relationship between each column in your data set.

exercise_data = {
    'Duration': [60, 60, 60, 45, 45, 60, 45, 60, 75, 90],
    'Pulse': [110, 117, 103, 109, 117, 102, 107, 104, 125, 130],
    'Maxpulse': [130, 145, 135, 175, 148, 127, 137, 134, 155, 160],
    'Calories': [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 310.5, 325.0, 520.0, 600.0]
}

df = pd.DataFrame(exercise_data)

# Calculate Correlation Matrix
correlation_matrix = df.corr()

print("--- 1. Pearson Correlation Matrix (df.corr()) ---")
print(correlation_matrix.round(4))

print("\n--- 2. Correlation Analysis & Findings ---")
print("1. Correlation between 'Duration' and 'Calories':", round(correlation_matrix.loc['Duration', 'Calories'], 4))
print("   -> Strong positive correlation: The longer the workout duration, the more calories burned.")

print("2. Correlation between 'Pulse' and 'Calories':", round(correlation_matrix.loc['Pulse', 'Calories'], 4))
print("   -> Moderate positive correlation: Higher average heart rate is associated with higher energy expenditure.")

print("3. Diagonal elements are always 1.0 (each feature has perfect correlation with itself).")
