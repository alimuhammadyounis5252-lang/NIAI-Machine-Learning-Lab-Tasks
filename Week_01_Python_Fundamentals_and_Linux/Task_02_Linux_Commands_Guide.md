# Week 1 - Task 2: Linux Shell Scripting & Command Reference Guide

**Student Name:** Ali Muhammad Younis (886)  
**Course:** Artificial Intelligence, Machine Learning & Deep Learning  
**Week:** 1  
**Task Title:** Linux / Debian Command Line Practice & Fundamentals  

---

## 1. Introduction to Linux & Debian Shell
Linux is the operating system of choice for AI/ML engineers, data scientists, and cloud deployments. The shell (Bash/sh) allows developers to automate workflows, manage files, inspect system resources, and manage packages.

---

## 2. Comprehensive Command Reference

### A. Navigation & Directory Operations
1. `pwd` (Print Working Directory):
   - **Syntax:** `pwd`
   - **Usage:** Displays current absolute directory path.
   - **Example:**
     ```bash
     pwd
     # /home/user/workspace
     ```
2. `cd` (Change Directory):
   - **Syntax:** `cd [path]`
   - **Examples:**
     ```bash
     cd ..          # Move one directory up
     cd ~           # Navigate to home directory
     cd /var/log    # Move to absolute path
     ```
3. `ls` (List Directory Contents):
   - **Syntax:** `ls [options] [path]`
   - **Examples:**
     ```bash
     ls -l          # Long listing (permissions, owner, size, date)
     ls -la         # Include hidden files (dotfiles)
     ls -lh         # Human-readable file sizes
     ```
4. `mkdir` (Make Directory):
   - **Syntax:** `mkdir [options] dir_name`
   - **Examples:**
     ```bash
     mkdir my_project
     mkdir -p parent/child/grandchild   # Create nested directories
     ```
5. `rmdir` (Remove Empty Directory):
   - **Syntax:** `rmdir dir_name`
   - **Example:**
     ```bash
     rmdir old_folder
     ```
6. `rm` (Remove Files and Directories):
   - **Syntax:** `rm [options] file_name`
   - **Examples:**
     ```bash
     rm sample.txt
     rm -r my_folder/    # Recursively remove directory and its contents
     rm -rf temp_dir/    # Force recursive removal without confirmation
     ```

### B. File Manipulation & Management
7. `touch` (Create Empty File or Update Timestamp):
   - **Syntax:** `touch filename`
   - **Example:** `touch script.py data.csv`
8. `cp` (Copy Files and Directories):
   - **Syntax:** `cp [options] source destination`
   - **Examples:**
     ```bash
     cp file.txt backup.txt
     cp -r src_dir/ dest_dir/
     ```
9. `mv` (Move or Rename Files/Directories):
   - **Syntax:** `mv source destination`
   - **Examples:**
     ```bash
     mv old_name.txt new_name.txt   # Rename
     mv file.txt ./subfolder/       # Move
     ```
10. `file` (Determine File Type):
    - **Syntax:** `file filename`
    - **Example:** `file image.png` -> `image.png: PNG image data, 800 x 600, 8-bit/color RGB`

### C. File Viewing & Inspection
11. `cat` (Concatenate and Display File Content):
    - **Syntax:** `cat filename`
    - **Example:** `cat log.txt`
12. `more` & `less` (Paged File Viewing):
    - **Syntax:** `more filename` or `less filename`
    - **Usage:** Read large files page-by-page. In `less`, navigate with arrows and exit with `q`.
13. `head` (View Beginning of File):
    - **Syntax:** `head -n [number] filename`
    - **Example:** `head -n 10 dataset.csv` (Display first 10 rows)

### D. Redirection & Pipes
14. Redirection Operators (`>`, `>>`, `<`, `|`):
    - `>` : Overwrites stdout to a file. E.g.: `echo "Hello AI" > output.txt`
    - `>>` : Appends stdout to a file. E.g.: `echo "New Line" >> output.txt`
    - `<` : Reads stdin from a file. E.g.: `sort < input.txt`
    - `|` (Pipe) : Passes stdout of one command as stdin to another. E.g.: `ls -l | grep "py"`

### E. User Permissions & Superuser
15. `sudo` (Superuser Do):
    - **Syntax:** `sudo command`
    - **Usage:** Run commands with administrative / root privileges.
    - **Example:** `sudo apt update`
16. `chmod` (Change File Mode / Permissions):
    - **Syntax:** `chmod [permissions] file`
    - **Examples:**
      ```bash
      chmod +x script.sh       # Make executable
      chmod 755 run.py         # rwxr-xr-x
      chmod 644 document.txt   # rw-r--r--
      ```

### F. Process Management & System Control
17. `ps` (Process Status):
    - **Syntax:** `ps aux`
    - **Usage:** Display all running processes with PID, CPU %, Memory %.
18. `kill` (Terminate Process):
    - **Syntax:** `kill [PID]` or `kill -9 [PID]` (Force terminate)
19. `alias` (Create Command Shortcut):
    - **Syntax:** `alias name='command'`
    - **Example:** `alias ll='ls -la'`
20. `bash` and `sh` (Shell Interpreters):
    - **Syntax:** `bash script.sh` or `sh script.sh`
21. `nano` (Terminal Text Editor):
    - **Syntax:** `nano filename`
22. `man` (Manual Pages):
    - **Syntax:** `man [command]` (e.g., `man ls`)
23. `dpkg` & APT (Debian Package Management):
    - **Syntax:**
      ```bash
      sudo dpkg -i package.deb   # Install a local debian package
      sudo apt update            # Update repository index
      sudo apt upgrade           # Upgrade installed packages
      ```
24. `shutdown` & `restart` / `reboot`:
    - **Syntax:**
      ```bash
      sudo shutdown -h now       # Shutdown immediately
      sudo reboot                # Restart system
      ```

---

## 3. Practice Script
See `Task_02_linux_practice.sh` for an automated bash script demonstrating file creation, directory navigation, pipes, redirections, permissions, and process inspection.
