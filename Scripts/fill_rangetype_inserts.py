#!/usr/bin/env python3
"""
Generate INSERT statements for the RangeType table.
Count is pulled from fill_archer_inserts.NUM_RANGES so RangeIDs match
the range used by the JunctionRoundRange script.
Run:   python fill_rangetype_inserts.py
"""

import random
from fill_archer_inserts import NUM_RANGES

# (DistanceToTargetM, TargetFaceCm, NumberOfEnds)
ALL_COMBINATIONS = [
    (18, 40, 10),
    (18, 40, 20),
    (18, 60, 10),
    (18, 60, 20),
    (20, 80, 6),
    (20, 80, 12),
    (20, 122, 6),
    (20, 122, 12),
    (25, 80, 6),
    (25, 122, 6),
    (30, 80, 6),
    (30, 122, 6),
    (40, 80, 6),
    (40, 122, 6),
    (50, 80, 6),
    (50, 122, 6),
    (60, 80, 6),
    (60, 122, 6),
    (70, 80, 6),
    (70, 122, 6),
    (90, 80, 6),
    (90, 122, 6),
    (50, 80, 5),
    (50, 122, 5),
    (60, 80, 5),
    (60, 122, 5),
    (70, 80, 5),
    (90, 122, 5),
]

selected = random.sample(ALL_COMBINATIONS, min(NUM_RANGES, len(ALL_COMBINATIONS)))

rows = [f"({dist}, {face}, {ends})" for dist, face, ends in selected]

print("INSERT INTO RangeType (DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
