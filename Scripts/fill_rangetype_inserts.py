#!/usr/bin/env python3
"""
Generate INSERT statements for the RangeType table.
These are the standard Archery Australia distance / target face / end
combinations.  The script randomly samples a subset each run so the
AUTO_INCREMENT IDs differ, but every row produced is a valid combination.
Run:   python fill_rangetype_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.
"""
import random

# ── Configuration ──────────────────────────────────────────────────────────────
NUM_RECORDS = 20   # how many combinations to include (max 28)
# ───────────────────────────────────────────────────────────────────────────────

# (DistanceToTargetM, TargetFaceCm, NumberOfEnds)
ALL_COMBINATIONS = [
    (18,  40, 10), (18,  40, 20), (18,  60, 10), (18,  60, 20),
    (20,  80,  6), (20,  80, 12), (20, 122,  6), (20, 122, 12),
    (25,  80,  6), (25, 122,  6),
    (30,  80,  6), (30, 122,  6),
    (40,  80,  6), (40, 122,  6),
    (50,  80,  6), (50, 122,  6),
    (60,  80,  6), (60, 122,  6),
    (70,  80,  6), (70, 122,  6),
    (90,  80,  6), (90, 122,  6),
    (50,  80,  5), (50, 122,  5),
    (60,  80,  5), (60, 122,  5),
    (70,  80,  5), (90, 122,  5),
]

selected = random.sample(ALL_COMBINATIONS, min(NUM_RECORDS, len(ALL_COMBINATIONS)))

rows = [f"({dist}, {face}, {ends})" for dist, face, ends in selected]

print("INSERT INTO RangeType (DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
