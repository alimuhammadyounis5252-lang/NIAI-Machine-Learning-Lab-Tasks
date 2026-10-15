# Week 2 - File Handling & Context Management in Python
# Student Name: Ali Muhammad Younis (886)

import os

print("=" * 60)
print(" Week 2: File Handling & Operations")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

filename = "week2_demo_data.txt"

# 1. Writing to a file using 'with' statement (Context Manager)
print("\n1. Writing sample dataset to file...")
with open(filename, "w", encoding="utf-8") as f:
    f.write("ID,Model_Name,Accuracy,Loss\n")
    f.write("1,Linear Regression,0.85,0.15\n")
    f.write("2,Logistic Regression,0.89,0.11\n")
    f.write("3,Decision Tree,0.92,0.08\n")
print(f"Data written to {filename}")

# 2. Appending data to the file
print("\n2. Appending additional record to file...")
with open(filename, "a", encoding="utf-8") as f:
    f.write("4,Random Forest,0.95,0.05\n")

# 3. Reading line by line and stripping whitespace
print("\n3. Reading and parsing file contents:")
with open(filename, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        print(f"   Line {line_num}: {line.strip()}")

# 4. Cleanup
if os.path.exists(filename):
    os.remove(filename)
    print(f"\nCleanup: Removed temporary file {filename}")
