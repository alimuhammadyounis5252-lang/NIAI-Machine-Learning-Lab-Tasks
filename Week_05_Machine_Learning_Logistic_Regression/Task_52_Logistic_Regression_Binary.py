# Week 5 - Task 52: Binary Logistic Regression & Classification Metrics
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score
)

print("=" * 70)
print(" Week 5 - Task 52: Binary Logistic Regression")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 70)

# 1. Sigmoid Function Definition
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

print("--- 1. Mathematical Verification of Sigmoid Function ---")
test_z = np.array([-5.0, 0.0, 5.0])
print(f"Sigmoid({test_z}) = {sigmoid(test_z).round(4)}")

# 2. Dataset Generation: Medical Disease Risk Prediction (Binary: 0=Healthy, 1=Risk)
np.random.seed(42)
n_samples = 300

age = np.random.normal(50, 12, n_samples).clip(20, 80)
cholesterol = np.random.normal(210, 35, n_samples)
bmi = np.random.normal(27, 4, n_samples)

# Probability log-odds
z = 0.04 * (age - 50) + 0.03 * (cholesterol - 200) + 0.15 * (bmi - 25)
probabilities = sigmoid(z)
labels = (probabilities > 0.5).astype(int)

X = pd.DataFrame({'Age': age, 'Cholesterol': cholesterol, 'BMI': bmi})
y = labels

print(f"\n--- 2. Dataset Summary ---")
print(f"Total Patients: {len(X)} | Healthy (0): {sum(y == 0)} | High Risk (1): {sum(y == 1)}")

# 3. Split and Feature Scaling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Logistic Regression Training
clf = LogisticRegression()
clf.fit(X_train_scaled, y_train)

# 5. Model Predictions and Probabilities
y_pred = clf.predict(X_test_scaled)
y_pred_proba = clf.predict_proba(X_test_scaled)[:, 1]

# 6. Evaluation Metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)
cm = confusion_matrix(y_test, y_pred)

print("\n--- 3. Classification Evaluation Metrics ---")
print(f"Accuracy  : {acc * 100:.2f}%")
print(f"Precision : {prec * 100:.2f}%")
print(f"Recall    : {rec * 100:.2f}%")
print(f"F1-Score  : {f1:.4f}")
print(f"ROC-AUC   : {roc_auc:.4f}")

print("\nConfusion Matrix:")
print("                 Predicted Healthy (0)  Predicted Risk (1)")
print(f"Actual Healthy(0):        {cm[0, 0]:<20}  {cm[0, 1]}")
print(f"Actual Risk   (1):        {cm[1, 0]:<20}  {cm[1, 1]}")

print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Healthy (0)", "Risk (1)"]))
