#!/usr/bin/env python3
"""
Generate INSERT statements for the End table.
Each RoundScore gets ENDS_PER_SCORE[i] ends (positions 1..n).
The end-count list is seeded in fill_archer_inserts so fill_arrow_inserts
can reproduce the exact same EndID range.
Run:   python fill_end_inserts.py
"""
from fill_archer_inserts import ENDS_PER_SCORE

rows = []
for score_idx, num_ends in enumerate(ENDS_PER_SCORE, start=1):
    for position in range(1, num_ends + 1):
        rows.append(f"({score_idx}, {position})")

print("INSERT INTO End (ScoreID, Position) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
