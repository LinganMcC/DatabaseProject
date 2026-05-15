#!/usr/bin/env python3
"""Executes all fill_NAME_inserts.py passing in relavent archer count

How to use:
Set current working directory to the Scripts folder, check by using pwd in terminal, it
should be in the Scripts folder.

NOTE: The default __ARCHER_NUM_COUNT__ will be 50, can change by passing in a
commandline argument

Then execute using the following command:
py ./execute_all.py
or
py ./execute_all.py __ARCHER_NUM_COUNT__

If py doesn't work, make sure python is installed, otherwise it might be python3 or smth
"""

import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
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

    if not Path(order[0]).exists():
        print(
            f"ERROR: Cannot run script. Make sure that Scripts is the CWD. Can check by "
            "typing pwd and seeing if the Scripts is the root"
        )
        exit(-1)

    # Read archer count infomation
    DEFAULT_ARCHER_COUNT = 50
    num_archers = str(DEFAULT_ARCHER_COUNT)
    if len(sys.argv) > 1:
        num_archers = sys.argv[1]

    if not num_archers.isnumeric:
        print(
            "First argument must define the number of archers (numeric). Default is ",
            f"{DEFAULT_ARCHER_COUNT} if not provided",
        )
        exit(-1)

    print(f"Archer count: {num_archers}")

    # Output file and python platform specific executable
    out_name = "output.sql"
    out = open(out_name, "w")
    assert out, "Failed to open file"
    python = sys.executable

    # Iterate over all fill files in order and execute to. Output stdout to file for easy
    # copy and paste
    for file in order:
        print(f"Executing\t`py {file}`")
        if not Path(file).exists():
            print(
                f"Failed to find path {file}. Make sure that Scripts is the CWD. Can ",
                "check by typing pwd and seeing if the Scripts is the root",
            )
            exit(-1)

        # Run subprocess, making sure to capture stdout in text form
        result = subprocess.run(
            [python, file, num_archers], capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"Failed: {result.stdout}\n")
            continue

        out.write(f"-- {file}:\n{result.stdout}\n\n")
        print(f"Finished")

    out.close()

    print(f"Finished executing python scripts. Output saved to {out_name}")
