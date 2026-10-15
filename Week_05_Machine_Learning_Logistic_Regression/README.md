# Week 5 Tasks: Machine Learning I - Multivariate Linear, Polynomial & Logistic Regression

**Student Name:** Ali Muhammad Younis (886)  
**Course:** Artificial Intelligence, Machine Learning & Deep Learning  
**Week:** 5  

---

## Overview
This folder contains the complete, tested solutions for all Week 5 curriculum requirements and Annexure-I tasks (Task 51 and Task 52 covering Multivariate Linear Regression, Polynomial Regression, Binary Logistic Regression, and Multiclass Digits/MNIST classification with cross-validation).

---

## Directory Contents & Task Mapping

| Task # | File Name | Description |
|---|---|---|
| **Task 51** | `Task_51_Linear_Regression_Multiple.py` | Multivariate Linear Regression with Scikit-Learn: real estate pricing dataset, train/test split, learned weights/intercept, MSE, RMSE, MAE, R² score, and sample predictions. |
| **Polynomial** | `Task_Polynomial_Regression.py` | Non-linear regression using `PolynomialFeatures`: modeling non-linear curves, comparing degrees (1, 2, 5, 12), and analyzing bias-variance tradeoff / underfitting vs overfitting. |
| **Task 52 (Binary)** | `Task_52_Logistic_Regression_Binary.py` | Binary Logistic Regression from scratch & scikit-learn: Sigmoid function mathematical verification, Log-loss, confusion matrix, Accuracy, Precision, Recall, F1-Score, and ROC-AUC. |
| **Task 52 (Multi)** | `Task_52_Logistic_Regression_Multiclass_MNIST.py` | Multiclass Handwritten Digit Recognition on 8x8 images (MNIST / Digits dataset) using Softmax Logistic Regression, classification report, and confusion matrix heatmap (`mnist_confusion_matrix.png`). |
| **Code Practice** | `Task_ML_Code_Practice_End_to_End.py` | End-to-end Machine Learning pipeline integrating standard scaling, 5-Fold Stratified Cross-Validation, and hyperparameter comparison (Logistic vs Ridge). |
| **Runner** | `run_all_week5.py` | Automated test runner verifying all Week 5 Python scripts. |

---

## How to Run
Run any individual script:
```bash
python Task_51_Linear_Regression_Multiple.py
```
Or run all scripts automatically:
```bash
python run_all_week5.py
```
