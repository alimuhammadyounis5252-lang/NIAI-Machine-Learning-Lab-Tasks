# Week 4 - Univariate Linear Regression with Gradient Descent (From Scratch)
# Student Name: Ali Muhammad Younis (886)
# Course Curriculum: Week 4 Day 4 & Day 5

import numpy as np
import time
from sklearn.linear_model import LinearRegression

print("=" * 70)
print(" Week 4: Univariate Linear Regression with Gradient Descent")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 70)

# Generate synthetic dataset: y = 3.5 * x + 12.0 + noise
np.random.seed(42)
m = 100  # Number of training samples
X = np.linspace(1, 10, m)
y_true = 3.5 * X + 12.0 + np.random.normal(0, 1.5, m)

# -------------------------------------------------------------
# 1. Implementation WITHOUT Vectorization (Using standard loops)
# -------------------------------------------------------------
def gradient_descent_non_vectorized(X, y, lr=0.01, epochs=1000):
    m = len(X)
    w = 0.0
    b = 0.0
    loss_history = []

    start_time = time.time()
    for epoch in range(epochs):
        # 1. Compute Cost Function J(w, b)
        cost = 0.0
        for i in range(m):
            y_hat = w * X[i] + b
            cost += (y_hat - y[i]) ** 2
        cost = cost / (2 * m)
        loss_history.append(cost)

        # 2. Compute Gradients
        dj_dw = 0.0
        dj_db = 0.0
        for i in range(m):
            error = (w * X[i] + b) - y[i]
            dj_dw += error * X[i]
            dj_db += error
        dj_dw /= m
        dj_db /= m

        # 3. Update Parameters
        w -= lr * dj_dw
        b -= lr * dj_db

    elapsed = time.time() - start_time
    return w, b, loss_history, elapsed

# -------------------------------------------------------------
# 2. Implementation WITH Vectorization (NumPy Matrix Operations)
# -------------------------------------------------------------
def gradient_descent_vectorized(X, y, lr=0.01, epochs=1000):
    m = len(X)
    w = 0.0
    b = 0.0
    loss_history = []

    start_time = time.time()
    for epoch in range(epochs):
        # Vectorized prediction
        y_hat = w * X + b
        
        # Vectorized cost computation
        cost = np.sum((y_hat - y) ** 2) / (2 * m)
        loss_history.append(cost)

        # Vectorized gradient computation
        dj_dw = np.dot(y_hat - y, X) / m
        dj_db = np.sum(y_hat - y) / m

        # Vectorized parameter update
        w -= lr * dj_dw
        b -= lr * dj_db

    elapsed = time.time() - start_time
    return w, b, loss_history, elapsed

# Run Non-Vectorized
w_nv, b_nv, loss_nv, time_nv = gradient_descent_non_vectorized(X, y_true, lr=0.01, epochs=2000)

# Run Vectorized
w_vec, b_vec, loss_vec, time_vec = gradient_descent_vectorized(X, y_true, lr=0.01, epochs=2000)

# Compare with Scikit-Learn
sk_model = LinearRegression()
sk_model.fit(X.reshape(-1, 1), y_true)
w_sk = sk_model.coef_[0]
b_sk = sk_model.intercept_

print(f"\n--- Model Training Results (2000 Epochs, lr=0.01) ---")
print(f"1. Non-Vectorized : w = {w_nv:.4f}, b = {b_nv:.4f} | Time: {time_nv * 1000:.2f} ms | Final Cost: {loss_nv[-1]:.4f}")
print(f"2. Vectorized     : w = {w_vec:.4f}, b = {b_vec:.4f} | Time: {time_vec * 1000:.2f} ms | Final Cost: {loss_vec[-1]:.4f}")
print(f"3. Scikit-Learn   : w = {w_sk:.4f}, b = {b_sk:.4f}")

speedup = time_nv / time_vec if time_vec > 0 else 1.0
print(f"\nVectorization Speedup Factor: {speedup:.1f}x faster execution!")
