# Week 3 - Task 40: NumPy Random Techniques
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.w3schools.com/python/numpy_random.asp

import numpy as np

print("=" * 60)
print(" Week 3 - Task 40: NumPy Random Techniques")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generating Random Integers with randint
rand_int = np.random.randint(100)                      # Single int from 0 to 99
rand_ints_arr = np.random.randint(10, 50, size=(2, 4)) # 2x4 array between 10 and 50
print("1. Random Integer (0 to 99)           :", rand_int)
print("   Random Integer Matrix (10 to 50, 2x4):\n", rand_ints_arr)

# 2. Generating Floats with rand and randn
rand_floats = np.random.rand(3)                        # Uniform distribution [0, 1)
rand_normal = np.random.randn(2, 3)                    # Standard Normal distribution (mean=0, std=1)
print("\n2. Uniform Random Floats [0, 1) (rand) :", rand_floats)
print("   Standard Normal Matrix (randn):\n", rand_normal)

# 3. Random Choice from an Array with Custom Probabilities
items = np.array(['cat', 'dog', 'horse', 'bird'])
# 60% cat, 20% dog, 10% horse, 10% bird
prob_sample = np.random.choice(items, p=[0.6, 0.2, 0.1, 0.1], size=6)
print("\n3. Random Choice with Probability weights:")
print("   Sampled Animals:", prob_sample)

# 4. Shuffling and Permutation
arr = np.array([1, 2, 3, 4, 5])
permuted = np.random.permutation(arr)                  # Returns a new shuffled array
print("\n4. Original array before shuffle:", arr)
print("   Permuted copy                   :", permuted)
np.random.shuffle(arr)                                 # In-place shuffle
print("   Array after in-place shuffle    :", arr)
