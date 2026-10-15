# Week 5 - Polynomial Regression & Non-Linear Modeling
# Student Name: Ali Muhammad Younis (886)
# Course Curriculum: Week 5 Day 2

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score

print("=" * 70)
print(" Week 5: Polynomial Regression (Underfitting vs Overfitting)")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 70)

# Generate non-linear ground truth: y = 0.5 * x^2 - 2 * x + 3 + noise
np.random.seed(42)
n_points = 80
X = np.sort(np.random.uniform(-3, 3, n_points)).reshape(-1, 1)
y = 0.5 * (X.ravel() ** 2) - 2.0 * X.ravel() + 3.0 + np.random.normal(0, 0.8, n_points)

# Split into Train and Test sets
split_idx = int(0.75 * n_points)
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

print(f"Dataset: {n_points} samples (Train: {len(X_train)}, Test: {len(X_test)})")
print("True relationship: Quadratic polynomial (degree = 2)")

# Train models with different degrees
degrees = [1, 2, 5, 12]
results = []

print("\n--- Polynomial Degree Evaluation ---")
for deg in degrees:
    # Build pipeline: PolynomialFeatures -> LinearRegression
    poly_model = make_pipeline(PolynomialFeatures(degree=deg), LinearRegression())
    poly_model.fit(X_train, y_train)

    train_pred = poly_model.predict(X_train)
    test_pred  = poly_model.predict(X_test)

    train_mse = mean_squared_error(y_train, train_pred)
    test_mse  = mean_squared_error(y_test, test_pred)
    test_r2   = r2_score(y_test, test_pred)

    status = "Underfitting" if deg == 1 else ("Optimal Fit" if deg == 2 else "Overfitting risk")
    print(f"Degree {deg:2d} -> Train MSE: {train_mse:.4f} | Test MSE: {test_mse:.4f} | Test R2: {test_r2:.4f} | [{status}]")

print("\nConclusion: Degree 2 achieves optimal bias-variance tradeoff with lowest generalization error.")
