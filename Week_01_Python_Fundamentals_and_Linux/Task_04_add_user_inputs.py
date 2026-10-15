# Week 1 - Task 4: Add Two Numbers from User Input
# Student Name: Ali Muhammad Younis (886)

import sys

# Store input numbers (with default fallback for non-interactive testing)
if sys.stdin.isatty():
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
else:
    print("Non-interactive mode detected. Using sample inputs 5.2 and 3.8:")
    num1 = '5.2'
    num2 = '3.8'

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
