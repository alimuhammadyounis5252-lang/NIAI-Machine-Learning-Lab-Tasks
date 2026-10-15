# Week 1 - Task 22: Tuple Data Type in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.programiz.com/python-programming/tuple

print("=== 1. Creating Tuples ===")
single_element_tuple = ("AI",)  # Trailing comma needed
course_tuple = ("Python", "Machine Learning", "Deep Learning", "Data Science")
print("Single element tuple:", single_element_tuple, "Type:", type(single_element_tuple))
print("Course tuple:", course_tuple)

print("\n=== 2. Indexing and Slicing Tuples ===")
print("First item:", course_tuple[0])
print("Middle items:", course_tuple[1:3])

print("\n=== 3. Tuple Immutability Proof ===")
try:
    course_tuple[0] = "Java"
except TypeError as e:
    print(f"Caught expected error when trying to mutate tuple: {e}")

print("\n=== 4. Tuple Unpacking ===")
student = ("Ali Muhammad Younis", 886, "A+")
name, roll, grade = student
print(f"Unpacked -> Name: {name}, Roll: {roll}, Grade: {grade}")

print("\n=== 5. Tuple Methods (count, index) ===")
grades = ('A', 'B', 'A', 'A', 'C', 'B', 'A')
print("Total 'A' grades:", grades.count('A'))
print("First index of 'C':", grades.index('C'))
