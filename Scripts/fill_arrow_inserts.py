#!/usr/bin/env python3
"""
Generate INSERT statements for the Arrow table.
Each End gets exactly ARROWS_PER_END arrows scored 0-10.
TOTAL_ENDS is pulled from fill_archer_inserts so the EndID range is
exact (matches what fill_end_inserts produced).
Run:   python fill_arrow_inserts.py
"""
import random
from fill_archer_inserts import TOTAL_ENDS, ARROWS_PER_END

# Weighted arrow scores — competitive archers cluster high.
SCORE_WEIGHTS = [2, 1, 1, 2, 3, 5, 10, 15, 20, 22, 19]  # indices 0-10


def random_score():
    return random.choices(range(11), weights=SCORE_WEIGHTS, k=1)[0]


rows = []
for end_id in range(1, TOTAL_ENDS + 1):
    for _ in range(ARROWS_PER_END):
        rows.append(f"({end_id}, {random_score()})")

print("INSERT INTO Arrow (EndID, Score) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
