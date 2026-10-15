# Week 1 - Task 16: While Loops in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.geeksforgeeks.org/python-while-loops/

print("=== Exercise 1: Basic Counting with While Loop ===")
count = 1
while count <= 5:
    print(f"Counter: {count}")
    count += 1

print("\n=== Exercise 2: Sum of First N Numbers ===")
n = 10
total = 0
current = 1
while current <= n:
    total += current
    current += 1
print(f"Sum of numbers from 1 to {n} is: {total}")

print("\n=== Exercise 3: While Loop with Else Clause ===")
x = 3
while x > 0:
    print(f"Countdown: {x}")
    x -= 1
else:
    print("Blastoff! (While loop terminated naturally)")

print("\n=== Exercise 4: Sentinel / Flag Controlled Loop ===")
numbers = [12, 45, 68, -1, 99, 100]
index = 0
print("Reading stream until negative sentinel (-1) is encountered:")
while index < len(numbers) and numbers[index] >= 0:
    print(f"Valid reading: {numbers[index]}")
    index += 1
