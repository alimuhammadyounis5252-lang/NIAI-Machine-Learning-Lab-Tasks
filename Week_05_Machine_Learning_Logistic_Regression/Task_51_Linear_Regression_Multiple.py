# Week 5 - Task 51: Multivariate Linear Regression with Scikit-Learn
# Student Name: Ali Muhammad Younis (886)
# Reference: https://stackabuse.com/linear-regression-in-python-with-scikit-learn/

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

print("=" * 70)
print(" Week 5 - Task 51: Multivariate Linear Regression")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 70)

# 1. Dataset Generation: Real Estate Pricing based on Multiple Features
# Features: [SquareFootage, Bedrooms, Bathrooms, DistanceToCityCenter_km]
np.random.seed(42)
n_samples = 250

sq_footage = np.random.normal(1800, 400, n_samples).clip(800, 3500)
bedrooms = np.random.randint(1, 6, n_samples)
bathrooms = np.random.randint(1, 4, n_samples)
dist_city = np.random.uniform(2, 30, n_samples)

# True underlying function + noise:
# Price = 120 * sqft + 15000 * bed + 10000 * bath - 2500 * dist + 50000 + noise
price = (
    120.0 * sq_footage +
    15000.0 * bedrooms +
    10000.0 * bathrooms -
    2500.0 * dist_city +
    50000.0 +
    np.random.normal(0, 15000, n_samples)
)

df = pd.DataFrame({
    'SquareFootage': sq_footage,
    'Bedrooms': bedrooms,
    'Bathrooms': bathrooms,
    'DistanceToCity_km': dist_city,
    'Price': price
})

print("--- 1. Sample Dataset Head ---")
print(df.head(4).round(2))

# 2. Feature Matrix (X) and Target Vector (y)
X = df[['SquareFootage', 'Bedrooms', 'Bathrooms', 'DistanceToCity_km']]
y = df['Price']

# 3. Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
print(f"\nTraining set size: {X_train.shape[0]} | Testing set size: {X_test.shape[0]}")

# 4. Model Training with LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Extracting Coefficients and Intercept
print("\n--- 2. Learned Model Parameters ---")
print(f"Intercept (b): ${model.intercept_:,.2f}")
for feature, coef in zip(X.columns, model.coef_):
    print(f"Weight w [{feature:<18}]: {coef:+,.2f}")

# 6. Model Evaluation on Unseen Test Set
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n--- 3. Evaluation Metrics on Test Set ---")
print(f"Mean Absolute Error (MAE) : ${mae:,.2f}")
print(f"Mean Squared Error (MSE)  : {mse:,.2f}")
print(f"Root Mean Squared Error   : ${rmse:,.2f}")
print(f"R-squared Score (R2)      : {r2:.4f} (Explains {r2 * 100:.2f}% of price variance)")

# 7. Sample Predictions
sample_houses = pd.DataFrame({
    'SquareFootage': [1200, 2400, 3200],
    'Bedrooms': [2, 4, 5],
    'Bathrooms': [1, 3, 4],
    'DistanceToCity_km': [15.0, 5.0, 2.5]
})
pred_prices = model.predict(sample_houses)
print("\n--- 4. Predictions on New Properties ---")
for i, pred in enumerate(pred_prices, start=1):
    print(f"House #{i} Estimated Value: ${pred:,.2f}")
