#!/usr/bin/env python3
"""
Generate INSERT statements for the EquipmentType table.
These are the 5 standard Archery Australia bow divisions — the values
are canonical, but the script shuffles the insertion order each run
so AUTO_INCREMENT IDs differ between runs.
Run:   python fill_equipmenttype_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.
"""
import random

# ── Configuration ──────────────────────────────────────────────────────────────
# No count — these are the fixed Archery Australia divisions.
# ───────────────────────────────────────────────────────────────────────────────

EQUIPMENT = [
    ("Recurve",          "REC"),
    ("Compound",         "COM"),
    ("Recurve Barebow",  "RBB"),
    ("Compound Barebow", "CBB"),
    ("Longbow",          "LBW"),
]

random.shuffle(EQUIPMENT)

rows = [f"('{name}', '{code}')" for name, code in EQUIPMENT]

print("INSERT INTO EquipmentType (Name, DivisionCode) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")