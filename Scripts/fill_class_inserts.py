#!/usr/bin/env python3
"""
Generate INSERT statements for the Class table.
These are the 16 standard Archery Australia age/gender classifications.
The insertion order is shuffled each run so AUTO_INCREMENT IDs differ.
Run:   python fill_class_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.
"""

# ── Configuration ──────────────────────────────────────────────────────────────
# No count — these are the fixed Archery Australia classes.
# ───────────────────────────────────────────────────────────────────────────────

# (Gender, MinAge, MaxAge)
# MaxAge 999 means no upper limit (open-ended class)
CLASSES = [
    ("Female", 21, 49),  # Open Women   (21-49, before Senior 50+)
    ("Male", 21, 49),  # Open Men
    ("Female", 50, 59),  # Senior 50+ Women
    ("Male", 50, 59),  # Senior 50+ Men
    ("Female", 60, 69),  # Senior 60+ Women
    ("Male", 60, 69),  # Senior 60+ Men
    ("Female", 70, 999),  # Senior 70+ Women
    ("Male", 70, 999),  # Senior 70+ Men
    ("Female", 18, 20),  # Junior Under 21 Women
    ("Male", 18, 20),  # Junior Under 21 Men
    ("Female", 15, 17),  # Junior Under 18 Women
    ("Male", 15, 17),  # Junior Under 18 Men
    ("Female", 13, 15),  # Junior Under 16 Women
    ("Male", 13, 15),  # Junior Under 16 Men
    ("Female", 0, 13),  # Junior Under 14 Women
    ("Male", 0, 13),  # Junior Under 14 Men
]

rows = [f"('{gender}', {min_age}, {max_age})" for gender, min_age, max_age in CLASSES]

print("INSERT INTO Class (Gender, MinAge, MaxAge) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
