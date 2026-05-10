#!/usr/bin/env python3
"""
Generate random INSERT statements for the JunctionRoundRange table.
Each BaseRound is assigned 1-4 ranges in sequence (RangePosition 1, 2, …).
Run:   python fill_junctionroundrange_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.

IMPORTANT — set the ID ranges below to match what is already in your database.
"""
import random

# ── Configuration ──────────────────────────────────────────────────────────────
BASE_ROUND_ID_MIN = 1
BASE_ROUND_ID_MAX = 25   # all BaseRoundIDs to assign ranges to
RANGE_ID_MIN      = 1
RANGE_ID_MAX      = 20   # RangeType IDs available
MAX_RANGES_PER_ROUND = 3  # most rounds use 1-3 distance legs
# ───────────────────────────────────────────────────────────────────────────────

rows = []
for base_round_id in range(BASE_ROUND_ID_MIN, BASE_ROUND_ID_MAX + 1):
    num_ranges  = random.randint(1, MAX_RANGES_PER_ROUND)
    range_ids   = random.sample(range(RANGE_ID_MIN, RANGE_ID_MAX + 1), num_ranges)
    for position, range_id in enumerate(range_ids, start=1):
        rows.append(f"({base_round_id}, {range_id}, {position})")

print("INSERT INTO JunctionRoundRange (BaseRoundID, RangeID, RangePosition) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
