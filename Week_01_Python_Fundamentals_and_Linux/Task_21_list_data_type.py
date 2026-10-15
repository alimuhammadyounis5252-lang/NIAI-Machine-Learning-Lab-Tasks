# Week 1 - Task 21: List Data Type in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.programiz.com/python-programming/list

print("=== 1. Creating Lists and Accessing Elements ===")
numbers = [10, 25, 30, 45, 50, 65]
print("Original list:", numbers)
print("First element (index 0):", numbers[0])
print("Last element (index -1):", numbers[-1])

print("\n=== 2. List Slicing ===")
print("Elements from index 1 to 4:", numbers[1:4])
print("First 3 elements:", numbers[:3])
print("Elements in reverse order:", numbers[::-1])

print("\n=== 3. Modifying Lists (append, insert, extend) ===")
numbers.append(70)
print("After append(70):", numbers)
numbers.insert(2, 99)
print("After insert(2, 99):", numbers)
numbers.extend([100, 110])
print("After extend([100, 110]):", numbers)

print("\n=== 4. Removing Elements (remove, pop, clear) ===")
numbers.remove(99)
print("After remove(99):", numbers)
popped_val = numbers.pop()
print(f"Popped value: {popped_val}, remaining list: {numbers}")

print("\n=== 5. List Comprehension ===")
squares = [x ** 2 for x in range(1, 6)]
print("Squares from 1 to 5:", squares)
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Even squares up to 10:", even_squares)
