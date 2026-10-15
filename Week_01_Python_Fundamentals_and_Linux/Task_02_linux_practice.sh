#!/bin/bash
# ==============================================================================
# Week 1 - Task 2: Linux Shell Scripting Practice Script
# Student Name: Ali Muhammad Younis (886)
# Course: Artificial Intelligence, Machine Learning & Deep Learning
# ==============================================================================

echo "=========================================================="
echo " Starting Linux Command Line Fundamentals Practice Script "
echo " Student: Ali Muhammad Younis (886)                      "
echo "=========================================================="

# 1. Print Working Directory
echo "[1] Current Working Directory:"
pwd

# 2. Directory creation and navigation
echo -e "\n[2] Creating test directories..."
mkdir -p demo_linux_dir/sub_folder
cd demo_linux_dir
pwd

# 3. File creation using touch
echo -e "\n[3] Creating files using touch..."
touch notes.txt info.log data.csv

# 4. Redirection (> and >>)
echo -e "\n[4] Writing text to file using redirection (> and >>)..."
echo "Line 1: Artificial Intelligence Course" > notes.txt
echo "Line 2: Machine Learning Fundamentals" >> notes.txt
echo "Line 3: Deep Learning with PyTorch and TensorFlow" >> notes.txt

# 5. Viewing file content using cat and head
echo -e "\n[5] Displaying file contents using cat:"
cat notes.txt

echo -e "\n[6] Displaying top 2 lines using head:"
head -n 2 notes.txt

# 6. File copying and moving
echo -e "\n[7] Copying and moving files (cp, mv):"
cp notes.txt backup_notes.txt
mv info.log sub_folder/moved_info.log
ls -l

# 7. File checking
echo -e "\n[8] Checking file types with 'file' command:"
file notes.txt

# 8. Permissions (chmod)
echo -e "\n[9] Modifying file permissions with chmod:"
chmod 644 notes.txt
chmod +x backup_notes.txt
ls -l notes.txt backup_notes.txt

# 9. Piping and Filtering (|)
echo -e "\n[10] Filtering contents with pipe (|) and grep:"
cat notes.txt | grep "Machine"

# 10. Process Status (ps)
echo -e "\n[11] Viewing process status (top 5 processes):"
ps aux | head -n 5

# Cleanup demo files
cd ..
rm -rf demo_linux_dir

echo -e "\n=========================================================="
echo " Linux Command Practice Completed Successfully!          "
echo "=========================================================="
