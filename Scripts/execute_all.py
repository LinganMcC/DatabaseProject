#!/usr/bin/env python3
"""Executes all fill_NAME_inserts.py passing in relavent archer count
Make sure when executing, the terminal directory is relative to this script and all
other fill scripts. It won't work otherwise."""

import subprocess
import sys

# Order of execution
order = [
    "./fill_class_inserts.py",
    "./fill_equipmenttype_inserts.py",
    "./fill_rangetype_inserts.py",
    "./fill_baseround_inserts.py",
    "./fill_equivalentround_inserts.py",
    "./fill_junctionroundrange_inserts.py",
    "./fill_club_inserts.py",
    "./fill_championship_inserts.py",
    "./fill_competition_inserts.py",
    "./fill_archer_inserts.py",
    "./fill_roundscore_inserts.py",
    "./fill_end_inserts.py",
    "./fill_arrow_inserts.py",
]

# Output file and python platform specific executable
out_name = "output.sql"
out = open(out_name, "w")
assert out, "Failed to open file"
python = sys.executable

# Read archer count infomation
DEFAULT_ARCHER_COUNT = 50
num_archers = str(DEFAULT_ARCHER_COUNT)
if len(sys.argv) > 1:
    num_archers = sys.argv[1]

if not num_archers.isnumeric:
    print(
        (
            "First argument must define the number of archers (numeric). Default is ",
            f"{DEFAULT_ARCHER_COUNT} if not provided",
        )
    )
    exit(-1)

print(f"Archer count: {num_archers}")

# Iterate over all fill files in order and execute to. Output stdout to file for easy
# copy and paste
for file in order:
    print(f"Executing\t`py {file}`...")

    # Run subprocess, making sure to capture stdout in text form
    result = subprocess.run([python, file, num_archers], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed: {result.stdout}\n")
        continue

    out.write(f"-- {file}:\n{result.stdout}\n\n")
    print(f"Finished\t`{python} {file}`...")

out.close()

print(f"Finished executing python scripts. Output saved to {out_name}")
