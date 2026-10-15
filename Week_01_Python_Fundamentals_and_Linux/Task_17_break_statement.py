# Week 1 - Task 17: Break Statement in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.geeksforgeeks.org/python-break-statement/

print("=== Exercise 1: Break in a For Loop ===")
target = "cherry"
fruits = ["apple", "banana", "cherry", "date", "fig"]

for fruit in fruits:
    print(f"Checking fruit: {fruit}")
    if fruit == target:
        print(f"Found {target}! Exiting loop immediately with break.")
        break

print("\n=== Exercise 2: Break in an Infinite While Loop ===")
number = 1
while True:
    if number % 7 == 0 and number % 5 == 0:
        print(f"First positive integer divisible by both 7 and 5 is: {number}")
        break
    number += 1

print("\n=== Exercise 3: Break in Nested Loops ===")
for i in range(1, 4):
    print(f"Outer loop i = {i}")
    for j in range(1, 5):
        if j == 3:
            print("  Inner loop hit j == 3 -> breaking inner loop")
            break
        print(f"  Inner loop j = {j}")
