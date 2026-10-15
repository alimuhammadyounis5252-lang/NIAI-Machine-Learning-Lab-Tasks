# Week 1 - Task 18: Continue Statement in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.geeksforgeeks.org/python-continue-statement/

print("=== Exercise 1: Skipping Odd Numbers with Continue ===")
print("Even numbers between 1 and 10:")
for num in range(1, 11):
    if num % 2 != 0:
        continue  # Skip odd numbers
    print(num, end=" ")
print()

print("\n=== Exercise 2: Filtering Characters in a String ===")
text = "Machine Learning 2026!"
print(f"Original text: '{text}'")
filtered = ""
for ch in text:
    if ch.isdigit() or ch in "!@#$%^&*()":
        continue  # Skip digits and punctuation
    filtered += ch
print(f"Filtered alphabetic text: '{filtered}'")

print("\n=== Exercise 3: Continue in While Loop ===")
val = 0
while val < 8:
    val += 1
    if val == 4 or val == 6:
        print(f"Skipping {val}...")
        continue
    print(f"Processed value: {val}")
