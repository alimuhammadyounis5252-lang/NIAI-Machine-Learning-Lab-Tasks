# Week 1 - Task 19: Looping Techniques in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.geeksforgeeks.org/looping-techniques-python/

print("=== Technique 1: Using enumerate() to track indices ===")
models = ["Linear Regression", "Logistic Regression", "Decision Tree", "Random Forest"]
for idx, model in enumerate(models, start=1):
    print(f"Model #{idx}: {model}")

print("\n=== Technique 2: Using zip() to iterate two lists simultaneously ===")
features = ["Square Footage", "Bedrooms", "Bathrooms", "Location"]
importance = [0.45, 0.25, 0.15, 0.15]
for feat, imp in zip(features, importance):
    print(f"Feature: {feat:<16} | Importance: {imp * 100:.1f}%")

print("\n=== Technique 3: Using reversed() to iterate backwards ===")
sequence = [10, 20, 30, 40, 50]
print("Reversed sequence:", end=" ")
for item in reversed(sequence):
    print(item, end=" ")
print()

print("\n=== Technique 4: Using sorted() on collections ===")
scores = [88, 95, 72, 91, 64]
print("Scores in ascending order:", sorted(scores))
print("Scores in descending order:", sorted(scores, reverse=True))

print("\n=== Technique 5: Looping through Dictionary with items(), keys(), values() ===")
student_info = {"Name": "Ali Muhammad Younis", "Roll": "886", "Subject": "AI / ML / DL"}
for k, v in student_info.items():
    print(f"{k:>8}: {v}")
