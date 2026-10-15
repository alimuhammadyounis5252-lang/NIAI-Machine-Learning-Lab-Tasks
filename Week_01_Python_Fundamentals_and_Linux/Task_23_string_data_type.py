# Week 1 - Task 23: String Data Type in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.programiz.com/python-programming/string

print("=== 1. String Creation and Multi-line Strings ===")
text = "Artificial Intelligence and Deep Learning"
multi_line = """Module 1: Fundamentals
Module 2: Machine Learning
Module 3: Deep Neural Networks"""
print("Text:", text)
print("Multi-line:\n", multi_line)

print("\n=== 2. String Indexing and Slicing ===")
print("First character:", text[0])
print("First word:", text[:10])
print("Step slicing [::2]:", text[:20:2])

print("\n=== 3. Common String Methods ===")
raw_str = "   Hello Python Developers!   "
print("Stripped:", f"'{raw_str.strip()}'")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replaced:", text.replace("Deep Learning", "Generative AI"))

print("\n=== 4. Splitting and Joining Strings ===")
words = text.split(" ")
print("Splitted list:", words)
joined_with_hyphen = "-".join(words)
print("Joined with hyphen:", joined_with_hyphen)

print("\n=== 5. String Formatting ===")
name = "Ali Muhammad Younis"
task_no = 23
print("Old style (%%): %s completed task %d" % (name, task_no))
print("str.format(): {} completed task {}".format(name, task_no))
print(f"f-string: {name} completed task {task_no}")
