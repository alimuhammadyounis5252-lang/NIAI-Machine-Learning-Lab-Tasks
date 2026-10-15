# Week 4 - Advanced Pandas: Merge, Join, GroupBy & Binning
# Student Name: Ali Muhammad Younis (886)
# Course Curriculum: Week 4 Day 1

import pandas as pd
import numpy as np

print("=" * 65)
print(" Week 4: Advanced Pandas (Merge, Join, GroupBy, Binning)")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 65)

# 1. Merging & Joining (Inner, Left, Right, Outer Joins)
df_students = pd.DataFrame({
    'StudentID': [101, 102, 103, 104],
    'Name': ['Ali', 'Usman', 'Fatima', 'Zainab'],
    'Major': ['AI', 'Data Science', 'AI', 'Robotics']
})

df_grades = pd.DataFrame({
    'StudentID': [101, 102, 103, 105],
    'Course': ['ML-101', 'ML-101', 'ML-101', 'ML-101'],
    'Score': [94, 88, 92, 75]
})

print("Students Table:\n", df_students)
print("\nGrades Table:\n", df_grades)

# Inner Join
inner_merged = pd.merge(df_students, df_grades, on='StudentID', how='inner')
print("\n--- 1a. Inner Join (Only matching IDs in both) ---\n", inner_merged)

# Left Join
left_merged = pd.merge(df_students, df_grades, on='StudentID', how='left')
print("\n--- 1b. Left Join (All students preserved) ---\n", left_merged)

# Outer Join
outer_merged = pd.merge(df_students, df_grades, on='StudentID', how='outer')
print("\n--- 1c. Full Outer Join (All records from both) ---\n", outer_merged)

# 2. GroupBy Aggregation
sales_data = pd.DataFrame({
    'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home', 'Home'],
    'Store': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Revenue': [12000, 15000, 8000, 9500, 6000, 7200]
})

dept_summary = sales_data.groupby('Department')['Revenue'].agg(['count', 'sum', 'mean'])
print("\n--- 2. GroupBy Aggregation Summary ---\n", dept_summary)

# 3. Discretization and Binning (pd.cut and pd.qcut)
ages = pd.Series([18, 22, 25, 27, 35, 42, 50, 61, 70, 82])

# pd.cut: Equal width bins
age_bins = [0, 25, 45, 65, 100]
age_labels = ['Youth', 'Young Adult', 'Middle Aged', 'Senior']
binned_cut = pd.cut(ages, bins=age_bins, labels=age_labels)

# pd.qcut: Quantile-based equal frequency bins
binned_qcut = pd.qcut(ages, q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

binning_demo = pd.DataFrame({
    'Age': ages,
    'Category (pd.cut)': binned_cut,
    'Quartile (pd.qcut)': binned_qcut
})
print("\n--- 3. Discretization and Binning Table ---\n", binning_demo)
