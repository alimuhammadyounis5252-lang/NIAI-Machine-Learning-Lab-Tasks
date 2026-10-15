# Week 5 - Day 5: End-to-End Machine Learning Code Practice
# Student Name: Ali Muhammad Younis (886)
# Course Curriculum: Week 5 Day 5

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, RidgeClassifier

print("=" * 70)
print(" Week 5: End-to-End ML Pipeline & Cross-Validation Practice")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 70)

# 1. Generate Synthetic Classification Dataset
X, y = make_classification(
    n_samples=500,
    n_features=10,
    n_informative=6,
    n_redundant=2,
    n_classes=2,
    random_state=42
)

print(f"Generated Dataset: 500 samples, 10 features, Binary target.")

# 2. Build ML Pipelines with StandardScaler
pipelines = {
    "Logistic Regression (L2, C=1.0)": Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(C=1.0, penalty='l2', solver='lbfgs'))
    ]),
    "Logistic Regression (L2, C=0.1)": Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(C=0.1, penalty='l2', solver='lbfgs'))
    ]),
    "Ridge Classifier (alpha=1.0)": Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RidgeClassifier(alpha=1.0))
    ])
}

# 3. 5-Fold Stratified Cross-Validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print("\n--- 5-Fold Cross-Validation Accuracy Comparison ---")
for model_name, pipe in pipelines.items():
    scores = cross_val_score(pipe, X, y, cv=cv, scoring='accuracy')
    print(f"{model_name:<35} | Mean Accuracy: {scores.mean() * 100:.2f}% (+/- {scores.std() * 100:.2f}%)")

print("\nCode Practice completed successfully.")
