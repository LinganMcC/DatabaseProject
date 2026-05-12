#!/usr/bin/env python3
"""
Generate INSERT statements for the EquipmentType table.
These are the 5 standard Archery Australia bow divisions — the values
are canonical, and the script assigns explicit EquipmentID values
to ensure consistency across different database instances.
Run:   python fill_equipmenttype_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.
"""
import random

# ── Configuration ──────────────────────────────────────────────────────────────
# Fixed EquipmentID assignments for the 5 standard Archery Australia divisions.
# Keeping IDs consistent ensures foreign key references remain valid.
# ───────────────────────────────────────────────────────────────────────────────

EQUIPMENT = [
    (1,  "Recurve",          "REC"),
    (2,  "Compound",         "COM"),
    (3,  "Recurve Barebow",  "RBB"),
    (4,  "Compound Barebow", "CBB"),
    (5,  "Longbow",          "LBW"),
]

random.shuffle(EQUIPMENT)

rows = [f"({id}, '{name}', '{code}')" for id, name, code in EQUIPMENT]

print("INSERT INTO EquipmentType (EquipmentID, Name, DivisionCode) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")