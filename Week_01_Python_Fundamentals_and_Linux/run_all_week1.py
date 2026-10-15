"""
Week 1 Test Runner
Runs all Week 1 tasks and verifies outputs.
Student: Ali Muhammad Younis (886)
"""

import subprocess
import os
import sys

def main():
    week_dir = os.path.dirname(os.path.abspath(__file__))
    scripts = sorted([
        f for f in os.listdir(week_dir)
        if f.endswith('.py') and f.startswith('Task_') and not f.startswith('run_all')
    ])

    print("=" * 70)
    print("           WEEK 1 TASK EXECUTION AND VERIFICATION")
    print("           Student: Ali Muhammad Younis (886)")
    print("=" * 70)

    passed = 0
    failed = 0

    for script in scripts:
        print(f"\n---> Running: {script}")
        script_path = os.path.join(week_dir, script)
        res = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"[PASSED] {script}")
            # print output preview
            lines = res.stdout.strip().splitlines()
            for l in lines[:3]:
                print(f"       {l}")
            if len(lines) > 3:
                print(f"       ... ({len(lines)} lines total)")
            passed += 1
        else:
            print(f"[FAILED] {script}")
            print(res.stderr)
            failed += 1

    print("\n" + "=" * 70)
    print(f"Week 1 Summary: {passed} Passed, {failed} Failed out of {len(scripts)} tasks.")
    print("=" * 70)

if __name__ == "__main__":
    main()
