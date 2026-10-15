# Week 3 - Descriptive Statistics & Probability Distributions
# Student Name: Ali Muhammad Younis (886)
# Course Curriculum: Week 3 Day 1 & Day 2

import numpy as np
from scipy import stats

print("=" * 65)
print(" Week 3: Correlation & Probability Distributions")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 65)

# 1. Correlation Coefficient (Pearson & Spearman)
# Study Hours vs Exam Score
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
exam_scores   = np.array([52, 55, 61, 68, 72, 79, 85, 88, 93, 98], dtype=float)

pearson_corr, p_val = stats.pearsonr(hours_studied, exam_scores)
spearman_corr, _    = stats.spearmanr(hours_studied, exam_scores)

print("\n--- 1. Correlation Analysis ---")
print(f"Pearson Correlation Coefficient (r) : {pearson_corr:.4f}")
print(f"P-value                            : {p_val:.4e}")
print(f"Spearman Rank Correlation (rho)     : {spearman_corr:.4f}")
print("Interpretation: Strong positive linear correlation between study hours and exam scores.")

# 2. Probability: Marginal, Joint, and Conditional Probability
# Contingency Table: Machine Failure vs Maintenance Level
#                Regular Maint (M1)   Poor Maint (M0)
# Failed (F1)           10                   40          = 50
# No Failure (F0)       190                  160         = 350
# Total                 200                  200         = 400

total_observations = 400
p_failure = 50 / total_observations               # Marginal P(F1)
p_poor_maint = 200 / total_observations           # Marginal P(M0)
p_failure_and_poor = 40 / total_observations      # Joint P(F1 and M0)
p_failure_given_poor = p_failure_and_poor / p_poor_maint  # Conditional P(F1 | M0)

print("\n--- 2. Probability Framework ---")
print(f"Marginal P(Failure)           : {p_failure:.4f} (12.5%)")
print(f"Joint P(Failure & Poor Maint) : {p_failure_and_poor:.4f} (10.0%)")
print(f"Conditional P(Failure | Poor) : {p_failure_given_poor:.4f} (20.0%)")

# 3. Bayes' Theorem Implementation
# P(Disease | Positive) = [P(Positive | Disease) * P(Disease)] / P(Positive)
p_disease = 0.01          # Prior
sensitivity = 0.95        # P(Pos | Disease)
specificity = 0.90        # P(Neg | No Disease) -> P(Pos | No Disease) = 0.10
p_pos_no_disease = 1.0 - specificity

# Total Probability of Positive
p_positive = (sensitivity * p_disease) + (p_pos_no_disease * (1 - p_disease))
# Posterior Probability
p_disease_given_positive = (sensitivity * p_disease) / p_positive

print("\n--- 3. Bayes' Theorem (Medical Test Scenario) ---")
print(f"Prior Probability P(Disease)          : {p_disease:.4f}")
print(f"Posterior Probability P(Disease | Pos): {p_disease_given_positive:.4f} ({p_disease_given_positive * 100:.2f}%)")

# 4. Probability Distributions
print("\n--- 4. Probability Distributions ---")
# Binomial Distribution: 10 coin flips, probability of getting exactly 6 heads
p_binom = stats.binom.pmf(k=6, n=10, p=0.5)
print(f"Binomial PMF (6 heads in 10 flips)   : {p_binom:.4f}")

# Normal Distribution: Mean=100, Std=15 (IQ scores)
# Probability of score <= 115 (within 1 standard deviation above mean)
p_norm_cdf = stats.norm.cdf(115, loc=100, scale=15)
print(f"Normal Distribution CDF (Score <= 115): {p_norm_cdf:.4f} ({p_norm_cdf * 100:.1f}%)")
