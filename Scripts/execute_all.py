# Make sure when executing, the terminal directory is relative to this script and all
# other fill scripts. It won't work otherwise.

import subprocess
import sys

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

out_name = "output.sql"
out = open(out_name, "w")
assert out, "Failed to open file"
python = sys.executable

for file in order:
    print(f"Executing\t`py {file}`...")

    result = subprocess.run([python, file], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed: {result.stdout}\n")
        continue

    out.write(f"-- {file}:\n{result.stdout}\n\n")
    print(f"Finished\t`{python} {file}`...")

out.close()

print(f"Finished executing python scripts. Output saved to {out_name}")