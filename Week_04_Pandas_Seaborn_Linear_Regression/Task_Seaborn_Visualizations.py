# Week 4 - Seaborn & Exploratory Data Visualization
# Student Name: Ali Muhammad Younis (886)
# Course Curriculum: Week 4 Day 2

import matplotlib
matplotlib.use('Agg')  # Headless backend for automated execution
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

print("=" * 65)
print(" Week 4: Exploratory Data Visualization with Seaborn")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 65)

# Generate synthetic dataset for visualization
np.random.seed(42)
n_samples = 150
data = pd.DataFrame({
    'Feature_X': np.random.normal(loc=50, scale=10, size=n_samples),
    'Feature_Y': np.random.normal(loc=30, scale=5, size=n_samples),
    'Category': np.random.choice(['Class A', 'Class B', 'Class C'], size=n_samples),
    'Value': np.random.exponential(scale=15, size=n_samples)
})

# 1. Distribution Plots (histplot, kdeplot)
plt.figure(figsize=(8, 4))
sns.histplot(data=data, x='Feature_X', kde=True, color='royalblue')
plt.title("Distribution Plot of Feature_X with KDE")
plt.xlabel("Feature X Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("seaborn_distribution_plot.png", dpi=100)
plt.close()
print("1. [OK] Distribution plot saved: seaborn_distribution_plot.png")

# 2. Categorical Data Plots (Boxplot and Violinplot)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(ax=axes[0], data=data, x='Category', y='Value', palette='Set2')
axes[0].set_title("Boxplot by Category")

sns.violinplot(ax=axes[1], data=data, x='Category', y='Feature_X', palette='Pastel1')
axes[1].set_title("Violinplot by Category")
plt.tight_layout()
plt.savefig("seaborn_categorical_plots.png", dpi=100)
plt.close()
print("2. [OK] Categorical plots saved: seaborn_categorical_plots.png")

# 3. Matrix Plot: Heatmap of Correlation Matrix
corr = data[['Feature_X', 'Feature_Y', 'Value']].corr()
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.savefig("seaborn_heatmap.png", dpi=100)
plt.close()
print("3. [OK] Heatmap plot saved: seaborn_heatmap.png")

print("\nSeaborn Visualization suite executed successfully.")
