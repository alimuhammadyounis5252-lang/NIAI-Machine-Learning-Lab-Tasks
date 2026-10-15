# Week 1 - Task 25: Dictionary Data Type in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.programiz.com/python-programming/dictionary

print("=== 1. Creating and Accessing Dictionaries ===")
student = {
    "name": "Ali Muhammad Younis",
    "roll_no": 886,
    "course": "AI & Machine Learning",
    "city": "Lahore"
}
print("Student record:", student)
print("Access using key ['name']:", student["name"])
print("Safe access using .get('city'):", student.get("city"))
print("Safe access with default value:", student.get("gpa", 4.0))

print("\n=== 2. Adding, Updating, and Removing Items ===")
student["grade"] = "A+"
student["city"] = "Islamabad"  # update existing
print("After update and adding grade:", student)
removed_grade = student.pop("grade")
print(f"Popped 'grade' ({removed_grade}). Current dict: {student}")

print("\n=== 3. Inspecting Keys, Values, and Items ===")
print("Keys  :", list(student.keys()))
print("Values:", list(student.values()))
print("Items :", list(student.items()))

print("\n=== 4. Dictionary Comprehension ===")
numbers = [1, 2, 3, 4, 5]
cube_dict = {x: x ** 3 for x in numbers}
print("Dictionary of cubes:", cube_dict)
