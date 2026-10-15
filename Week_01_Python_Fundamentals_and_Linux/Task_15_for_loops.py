# Week 1 - Task 15: For Loops in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.geeksforgeeks.org/python-for-loops/

print("=== Exercise 1: Iterating over a List ===")
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

print("\n=== Exercise 2: Iterating over a String ===")
word = "Artificial Intelligence"
vowels_count = 0
for char in word:
    if char.lower() in 'aeiou':
        vowels_count += 1
print(f"Total vowels in '{word}': {vowels_count}")

print("\n=== Exercise 3: Using range() with Step ===")
print("Even numbers from 2 to 10:")
for num in range(2, 11, 2):
    print(num, end=" ")
print()

print("\n=== Exercise 4: Nested For Loops (Multiplication Table) ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j:2d}", end=" | ")
    print()

print("\n=== Exercise 5: For Loop with Else Block ===")
for n in range(1, 4):
    print(f"Processing item {n}")
else:
    print("Loop finished successfully without break!")
