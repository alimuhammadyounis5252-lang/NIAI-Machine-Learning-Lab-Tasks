# Week 5 - Task 52 Part 2: Multiclass Logistic Regression on Handwritten Digits (MNIST / Digits)
# Student Name: Ali Muhammad Younis (886)
# Reference: https://towardsdatascience.com/logistic-regression-using-python-sklearn-numpy-mnist-handwriting-recognition-matplotlib-a6b31e2b166a

import matplotlib
matplotlib.use('Agg')  # Headless backend
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns

print("=" * 70)
print(" Week 5 - Task 52 Part 2: Multiclass Logistic Regression (Digits/MNIST)")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 70)

# 1. Load Digits Dataset (8x8 pixel images of handwritten digits 0 to 9)
digits = load_digits()
print(f"Dataset Shape: {digits.data.shape} ({digits.data.shape[0]} images, {digits.data.shape[1]} features each)")
print(f"Target Classes: {np.unique(digits.target)} (Digits 0 through 9)")

# 2. Train-Test Split (75% Train, 25% Test)
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.25, random_state=42
)
print(f"Train samples: {X_train.shape[0]} | Test samples: {X_test.shape[0]}")

# 3. Fit Multiclass Logistic Regression (Softmax / Multinomial)
# Increased max_iter to ensure convergence
logistic_reg = LogisticRegression(max_iter=2000, random_state=42)
logistic_reg.fit(X_train, y_train)

# 4. Predictions and Accuracy
y_pred = logistic_reg.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n--- Multiclass Model Performance ---")
print(f"Overall Accuracy: {accuracy * 100:.2f}%")

# 5. Detailed Classification Report
print("\nClassification Report (Precision, Recall, F1 for each digit):")
print(classification_report(y_test, y_pred, digits=4))

# 6. Confusion Matrix Heatmap
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(9, 7))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=True)
plt.title(f"Multiclass Logistic Regression Confusion Matrix\nAccuracy: {accuracy * 100:.2f}%")
plt.xlabel("Predicted Digit")
plt.ylabel("Actual Digit")
plt.tight_layout()
plt.savefig("mnist_confusion_matrix.png", dpi=100)
plt.close()

print("[OK] Confusion matrix heatmap saved as 'mnist_confusion_matrix.png'")
