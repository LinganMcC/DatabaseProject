#!/usr/bin/env python3
"""
Generate random INSERT statements for the Championship table.
Count is pulled from fill_archer_inserts.NUM_CHAMPIONSHIPS so the IDs
line up with the Competition.ChampionshipID range.
Run:   python fill_championship_inserts.py
"""
import random
from fill_archer_inserts import NUM_CHAMPIONSHIPS

YEAR_MIN = 2000
YEAR_MAX = 2025

TYPES   = ["Club", "State", "Regional", "National", "Open", "Youth", "Masters", "Indoor"]
STATES  = ["NSW", "VIC", "QLD", "WA", "SA", "TAS", "ACT", "NT"]
SEASONS = ["Summer", "Winter", "Spring", "Autumn"]


def random_name():
    style = random.randint(0, 3)
    if style == 0:
        return f"{random.choice(STATES)} {random.choice(TYPES)} Championship"
    elif style == 1:
        return f"Australian {random.choice(TYPES)} Archery Championship"
    elif style == 2:
        return f"{random.choice(SEASONS)} {random.choice(TYPES)} Archery Championship"
    else:
        return f"{random.choice(TYPES)} Archery Open"


rows = []
for _ in range(NUM_CHAMPIONSHIPS):
    name = random_name().replace("'", "''")
    year = random.randint(YEAR_MIN, YEAR_MAX)
    rows.append(f"('{name}', {year})")

print("INSERT INTO Championship (ChampionshipName, Year) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
