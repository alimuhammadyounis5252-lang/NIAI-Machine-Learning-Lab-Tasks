# Week 2 - Task 20: User-Defined Functions, Scope, and Functional Programming
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.geeksforgeeks.org/functions-in-python/

print("=" * 60)
print(" Week 2 - Task 20: Python Functions & Scope")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. Basic Function with Docstring and Return Value
def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculates the area of a rectangle given width and height."""
    return width * height

print(f"1. Area of rectangle (5.0 x 3.0): {calculate_rectangle_area(5.0, 3.0)}")

# 2. Positional, Keyword, and Default Arguments
def greet_student(name: str, course: str = "AI / ML / DL", cohort: int = 2026):
    return f"Welcome {name} to {course} (Cohort {cohort})!"

print("2a. Default args:", greet_student("Ali Muhammad Younis"))
print("2b. Keyword args:", greet_student(cohort=2027, name="Ahmed", course="Deep Learning"))

# 3. Arbitrary Arguments: *args and **kwargs
def calculate_statistics(*args, **kwargs):
    total = sum(args)
    count = len(args)
    mean_val = total / count if count > 0 else 0
    scale = kwargs.get("scale", 1.0)
    scaled_mean = mean_val * scale
    return {"count": count, "sum": total, "mean": mean_val, "scaled_mean": scaled_mean}

stat_result = calculate_statistics(10, 20, 30, 40, 50, scale=1.5)
print(f"3. *args & **kwargs result: {stat_result}")

# 4. Variable Scope: Local, Global, and Nonlocal
global_counter = 100

def outer_scope_demo():
    outer_var = "I am in outer scope"
    
    def inner_scope_demo():
        nonlocal outer_var
        outer_var = "Modified by inner scope via nonlocal"
        global global_counter
        global_counter += 1
        print("   Inner sees:", outer_var)
        
    inner_scope_demo()
    print("   Outer after modification:", outer_var)

print("4. Variable Scope Demo:")
outer_scope_demo()
print(f"   Global counter after modification: {global_counter}")

# 5. Lambda Expressions, Map, and Filter
raw_scores = [45, 62, 85, 92, 38, 77, 98]

# Lambda for grading pass/fail
is_pass = lambda score: score >= 50
passed_scores = list(filter(is_pass, raw_scores))
print(f"\n5a. Filtered passing scores (>=50): {passed_scores}")

# Map to apply a 5% bonus curve
curve_fn = lambda score: round(min(score * 1.05, 100), 1)
curved_scores = list(map(curve_fn, raw_scores))
print(f"5b. Curved scores with map(): {curved_scores}")
