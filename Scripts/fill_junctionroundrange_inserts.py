#!/usr/bin/env python3
"""
Generate random INSERT statements for the JunctionRoundRange table.
Each BaseRound (1..NUM_BASE_ROUNDS) is assigned 1-3 ranges in sequence.
Run:   python fill_junctionroundrange_inserts.py
"""

import random
from fill_archer_inserts import NUM_BASE_ROUNDS, NUM_RANGES

MAX_RANGES_PER_ROUND = 3

rows = []
for base_round_id in range(1, NUM_BASE_ROUNDS + 1):
    num_ranges = random.randint(1, MAX_RANGES_PER_ROUND)
    range_ids = random.sample(range(1, NUM_RANGES + 1), num_ranges)
    for position, range_id in enumerate(range_ids, start=1):
        rows.append(f"({base_round_id}, {range_id}, {position})")

print("INSERT INTO JunctionRoundRange (BaseRoundID, RangeID, RangePosition) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
