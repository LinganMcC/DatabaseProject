# Runs every fill script (in dependency order) and concatenates their output
# into output.sql. Uses the same Python interpreter that runs this script,
# so it works on Windows (`py`/`python`) and macOS/Linux (`python3`) alike.
#
# Usage:  python3 execute_all.py [num_archers]
#   e.g.  python3 execute_all.py 300   → generate a dataset of 300 archers
#         python3 execute_all.py       → use the default in fill_archer_inserts
#
# The archer count is passed to every subprocess via the NUM_ARCHERS env var,
# which fill_archer_inserts.py reads. Every other fill script imports its
# scaling constants from fill_archer_inserts, so they all rescale together.

import os
import subprocess
import sys

order = [
    "fill_class_inserts.py",
    "fill_equipmenttype_inserts.py",
    "fill_rangetype_inserts.py",
    "fill_baseround_inserts.py",
    "fill_equivalentround_inserts.py",
    "fill_junctionroundrange_inserts.py",
    "fill_club_inserts.py",
    "fill_championship_inserts.py",
    "fill_competition_inserts.py",
    "fill_archer_inserts.py",
    "fill_roundscore_inserts.py",
    "fill_end_inserts.py",
    "fill_arrow_inserts.py",
]

script_dir = os.path.dirname(os.path.abspath(__file__))
out_name   = os.path.join(script_dir, "output.sql")
python     = sys.executable

env = os.environ.copy()
if len(sys.argv) > 1:
    try:
        num_archers = int(sys.argv[1])
    except ValueError:
        sys.exit(f"num_archers must be an integer, got: {sys.argv[1]!r}")
    if num_archers < 1:
        sys.exit(f"num_archers must be >= 1, got: {num_archers}")
    env["NUM_ARCHERS"] = str(num_archers)
    print(f"Generating dataset for {num_archers} archers...\n")

with open(out_name, "w") as out:
    for file in order:
        path = os.path.join(script_dir, file)
        print(f"Executing\t`{python} {file}`...")

        result = subprocess.run([python, path], capture_output=True, text=True, env=env)
        if result.returncode != 0:
            print(f"Failed: {result.stderr}\n")
            continue

        out.write(f"-- {file}:\n{result.stdout}\n\n")
        print(f"Finished\t`{python} {file}`...")

print(f"\nFinished executing python scripts. Output saved to {out_name}")
