#!/usr/bin/env python3
"""
Generate random INSERT statements for the EquivalentRound table.
Maps which actual round a class/equipment combination shoots as an
equivalent to a base round, with historical validity date ranges.
ValidTo is nullable (NULL = currently valid).
Run:   python fill_equivalentround_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.

IMPORTANT — set the ID ranges below to match what is already in your database.
"""
import random
from datetime import date, timedelta

# ── Configuration ──────────────────────────────────────────────────────────────
NUM_RECORDS       = 30
BASE_ROUND_ID_MIN = 1
BASE_ROUND_ID_MAX = 25
CLASS_ID_MIN      = 1
CLASS_ID_MAX      = 16
EQUIPMENT_ID_MIN  = 1
EQUIPMENT_ID_MAX  = 5
STILL_VALID_CHANCE = 0.5   # probability ValidTo is NULL (mapping still active)
# ───────────────────────────────────────────────────────────────────────────────

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

rows = []
for _ in range(NUM_RECORDS):
    base_round   = random.randint(BASE_ROUND_ID_MIN, BASE_ROUND_ID_MAX)
    # ActualRoundID must differ from BaseRoundID
    actual_round = random.choice(
        [r for r in range(BASE_ROUND_ID_MIN, BASE_ROUND_ID_MAX + 1) if r != base_round]
    )
    class_id     = random.randint(CLASS_ID_MIN, CLASS_ID_MAX)
    equip_id     = random.randint(EQUIPMENT_ID_MIN, EQUIPMENT_ID_MAX)
    valid_from   = random_date(date(2000, 1, 1), date(2020, 1, 1))
    if random.random() < STILL_VALID_CHANCE:
        valid_to = "NULL"
    else:
        valid_to = f"'{random_date(valid_from + timedelta(days=365), date(2025, 12, 31))}'"
    rows.append(f"({base_round}, {actual_round}, {class_id}, {equip_id}, '{valid_from}', {valid_to})")

print("INSERT INTO EquivalentRound (BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
