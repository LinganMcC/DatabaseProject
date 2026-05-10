#!/usr/bin/env python3
"""
Generate random INSERT statements for the End table.
Each RoundScore gets a sequence of ends (Position 1, 2, …).
Run:   python fill_end_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.

IMPORTANT — set the ID ranges below to match what is already in your database.
"""
import random

# ── Configuration ──────────────────────────────────────────────────────────────
SCORE_ID_MIN       = 1
SCORE_ID_MAX       = 60    # all ScoreIDs to create ends for
ENDS_PER_SCORE_MIN = 6     # shortest rounds have 6 ends
ENDS_PER_SCORE_MAX = 24    # longest rounds have 24 ends
# ───────────────────────────────────────────────────────────────────────────────

rows = []
for score_id in range(SCORE_ID_MIN, SCORE_ID_MAX + 1):
    num_ends = random.randint(ENDS_PER_SCORE_MIN, ENDS_PER_SCORE_MAX)
    for position in range(1, num_ends + 1):
        rows.append(f"({score_id}, {position})")

print("INSERT INTO End (ScoreID, Position) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
