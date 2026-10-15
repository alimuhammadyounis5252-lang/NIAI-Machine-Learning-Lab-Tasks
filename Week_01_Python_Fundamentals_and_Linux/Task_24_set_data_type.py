# Week 1 - Task 24: Set Data Type in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.programiz.com/python-programming/set

print("=== 1. Creating Sets (Unordered, Unique Elements) ===")
nums_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
unique_set = set(nums_with_duplicates)
print("Original list with duplicates:", nums_with_duplicates)
print("Unique set:", unique_set)

print("\n=== 2. Adding and Removing Set Elements ===")
unique_set.add(6)
print("After add(6):", unique_set)
unique_set.discard(2)
print("After discard(2):", unique_set)

print("\n=== 3. Set Operations (Union, Intersection, Difference) ===")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Set A:", set_a)
print("Set B:", set_b)

print("Union (A | B):", set_a | set_b)
print("Intersection (A & B):", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference (A ^ B):", set_a ^ set_b)

print("\n=== 4. Subset and Superset Testing ===")
subset_test = {1, 2}
print("{1, 2} is subset of Set A?", subset_test.issubset(set_a))
print("Set A is superset of {1, 2}?", set_a.issuperset(subset_test))
