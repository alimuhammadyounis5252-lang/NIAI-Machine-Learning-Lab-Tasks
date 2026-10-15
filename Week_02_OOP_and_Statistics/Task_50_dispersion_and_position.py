# Week 2 - Task 50: Measures of Dispersion, Position, and Data Types
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/python_ml_standard_deviation.asp

import numpy as np
from scipy import stats

print("=" * 70)
print(" Week 2 - Task 50: Measures of Dispersion, Shape & Position")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 70)

# Dataset: Test scores of machine learning candidates
scores = np.array([32, 111, 138, 28, 59, 77, 97, 85, 90, 68, 75, 82, 88])
print(f"Data: {scores}")
print(f"Number of items: {len(scores)}")

# 1. Measures of Dispersion
variance_val = np.var(scores)
std_val = np.std(scores)
range_val = np.ptp(scores)  # Peak-to-peak (max - min)
iqr_val = stats.iqr(scores)

print("\n--- 1. Measures of Dispersion ---")
print(f"Variance (sigma^2)      : {variance_val:.4f}")
print(f"Standard Deviation (sigma): {std_val:.4f}")
print(f"Range (Max - Min)      : {range_val:.4f}")
print(f"Interquartile Range(IQR): {iqr_val:.4f}")

# 2. Measures of Shape (Skewness and Kurtosis)
skew_val = stats.skew(scores)
kurt_val = stats.kurtosis(scores)

print("\n--- 2. Shape of Distribution ---")
print(f"Skewness : {skew_val:.4f} ({'Right-skewed' if skew_val > 0 else 'Left-skewed'})")
print(f"Kurtosis : {kurt_val:.4f} ({'Leptokurtic' if kurt_val > 0 else 'Platykurtic'})")

# 3. Measures of Position (Percentiles, Quartiles, Z-Scores)
p25 = np.percentile(scores, 25)
p50 = np.percentile(scores, 50)  # Median
p75 = np.percentile(scores, 75)
p90 = np.percentile(scores, 90)

print("\n--- 3. Measures of Position ---")
print(f"25th Percentile (Q1) : {p25}")
print(f"50th Percentile (Q2) : {p50} (Median)")
print(f"75th Percentile (Q3) : {p75}")
print(f"90th Percentile      : {p90}")

# Z-scores: (x - mean) / std
z_scores = stats.zscore(scores)
print("\n--- 4. Z-Scores (Standardized Distance from Mean) ---")
for orig, z in zip(scores[:5], z_scores[:5]):
    print(f"  Score: {orig:3d}  -->  Z-Score: {z:+.4f}")

# 4. Summary of Data Types (Curriculum requirement)
print("\n--- 5. Data Classification Reference ---")
data_types_summary = {
    "Quantitative (Numerical)": [
        "Continuous (e.g., Temperature, Loss, Learning Rate)",
        "Discrete (e.g., Number of Epochs, Cluster count)"
    ],
    "Qualitative (Categorical)": [
        "Nominal (e.g., Optimizer: Adam, SGD, RMSprop)",
        "Ordinal (e.g., Education: High School < BS < MS < PhD)",
        "Binary (e.g., Classification output: 0 or 1)"
    ]
}
for category, subcategories in data_types_summary.items():
    print(f"* {category}:")
    for sub in subcategories:
        print(f"    - {sub}")
