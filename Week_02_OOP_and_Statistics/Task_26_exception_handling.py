# Week 2 - Task 26: Exception Handling in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.programiz.com/python-programming/exception-handling

print("=" * 60)
print(" Week 2 - Task 26: Exception Handling (try, except, else, finally)")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. Handling ZeroDivisionError
print("\n--- 1. Handling ZeroDivisionError ---")
def safe_divide(numerator: float, denominator: float):
    try:
        result = numerator / denominator
    except ZeroDivisionError as e:
        print(f"Error caught: Cannot divide {numerator} by zero ({e})")
        return None
    else:
        print(f"Division successful: {numerator} / {denominator} = {result}")
        return result
    finally:
        print("Cleanup: safe_divide execution completed.")

safe_divide(100, 4)
safe_divide(50, 0)

# 2. Handling Multiple Exceptions (ValueError, TypeError)
print("\n--- 2. Handling Multiple Exceptions ---")
def parse_and_double(val):
    try:
        num = float(val)
        return num * 2
    except ValueError:
        print(f"ValueError: Could not convert '{val}' to float.")
    except TypeError:
        print(f"TypeError: Invalid type passed ({type(val)}).")

parse_and_double("42.5")
parse_and_double("not_a_number")
parse_and_double([1, 2, 3])

# 3. Handling FileNotFoundError
print("\n--- 3. Handling File I/O Exceptions ---")
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Handled missing file exception gracefully: {e.filename} was not found.")
