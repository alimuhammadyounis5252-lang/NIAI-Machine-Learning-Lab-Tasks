# Week 1 - Task 10: Convert Kilometers to Miles
# Student Name: Ali Muhammad Younis (886)

import sys

# Taking kilometers input from the user (with default fallback for automated runs)
if sys.stdin.isatty():
    kilometers = float(input("Enter value in kilometers: "))
else:
    print("Non-interactive mode: Using default 10.5 km")
    kilometers = 10.5

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers, miles))
