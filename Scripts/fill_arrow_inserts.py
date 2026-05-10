#!/usr/bin/env python3
"""
Generate random INSERT statements for the Arrow table.
Each End gets exactly 6 arrows scored 0-10.
Arrow scores use a weighted distribution (realistic archery bell curve,
skewed toward higher scores for competitive archers).
Run:   python fill_arrow_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.

IMPORTANT — set the ID ranges below to match what is already in your database.
"""
import random

# ── Configuration ──────────────────────────────────────────────────────────────
END_ID_MIN       = 1
END_ID_MAX       = 800     # set to the highest EndID in your End table
ARROWS_PER_END   = 6
# ───────────────────────────────────────────────────────────────────────────────

# Weighted arrow scores — higher scores appear more often for active competitors.
# Weights: 0=miss, 1-5=low, 6-8=mid, 9-10=high
SCORE_WEIGHTS = [2, 1, 1, 2, 3, 5, 10, 15, 20, 22, 19]  # indices 0-10

def random_score():
    return random.choices(range(11), weights=SCORE_WEIGHTS, k=1)[0]

rows = []
for end_id in range(END_ID_MIN, END_ID_MAX + 1):
    for _ in range(ARROWS_PER_END):
        rows.append(f"({end_id}, {random_score()})")

print("INSERT INTO Arrow (EndID, Score) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
