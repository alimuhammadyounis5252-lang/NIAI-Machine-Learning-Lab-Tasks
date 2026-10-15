"""
Week 1 - Task 1: Environment & Tool Verification Script
Student Name: Ali Muhammad Younis (886)
Course: Artificial Intelligence, Machine Learning & Deep Learning

This script automatically verifies:
- Python version and execution environment
- Availability of required scientific and AI libraries (NumPy, SciPy, Pandas, Matplotlib, Scikit-Learn)
- Availability and versions of PyTorch and TensorFlow
"""

import sys
import platform

def verify_system_and_tools():
    print("=" * 60)
    print("       AI ENVIRONMENT & TOOLS VERIFICATION REPORT")
    print("       Student: Ali Muhammad Younis (886)")
    print("=" * 60)
    print(f"Operating System : {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"Python Executable: {sys.executable}")
    print(f"Python Version   : {sys.version.split()[0]}")
    print("-" * 60)

    packages_to_check = [
        ("numpy", "NumPy"),
        ("pandas", "Pandas"),
        ("scipy", "SciPy"),
        ("matplotlib", "Matplotlib"),
        ("sklearn", "Scikit-Learn"),
        ("torch", "PyTorch"),
        ("tensorflow", "TensorFlow"),
    ]

    print("Package Status & Versions:")
    for mod_name, display_name in packages_to_check:
        try:
            mod = __import__(mod_name)
            ver = getattr(mod, "__version__", "Installed (Version unknown)")
            print(f"  [OK] {display_name:<15}: {ver}")
        except ImportError:
            print(f"  [--] {display_name:<15}: Not installed in current environment")

    print("=" * 60)
    print("Verification completed successfully.")
    print("=" * 60)

if __name__ == "__main__":
    verify_system_and_tools()
