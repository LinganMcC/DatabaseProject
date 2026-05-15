#!/usr/bin/env python3
"""
Generate INSERT statements for the RangeType table.
Count is pulled from fill_archer_inserts.NUM_RANGES so RangeIDs match
the range used by the JunctionRoundRange script.
Run:   python fill_rangetype_inserts.py
"""

from fill_archer_inserts import NUM_RANGES

# (DistanceToTargetM, TargetFaceCm, NumberOfEnds)
ALL_COMBINATIONS = [
    # 80cm Target face
    (10, 80, 5),  # 30+
    (20, 80, 5),
    (30, 80, 5),
    (40, 80, 5),
    (50, 80, 5),
    (60, 80, 5),
    (70, 80, 5),
    (80, 80, 5),
    (90, 80, 5),
    (10, 80, 6),  # 36+
    (20, 80, 6),
    (30, 80, 6),
    (40, 80, 6),
    (50, 80, 6),
    (60, 80, 6),
    (70, 80, 6),
    (80, 80, 6),
    (90, 80, 6),
    # 122cm Target face
    (10, 122, 5),  # 30*
    (20, 122, 5),
    (30, 122, 5),
    (40, 122, 5),
    (50, 122, 5),
    (60, 122, 5),
    (70, 122, 5),
    (80, 122, 5),
    (90, 122, 5),
    (10, 122, 6),  # 36*
    (20, 122, 6),
    (30, 122, 6),
    (40, 122, 6),
    (50, 122, 6),
    (60, 122, 6),
    (70, 122, 6),
    (80, 122, 6),
    (90, 122, 6),
    # 90+
    (20, 122, 18),
    (30, 122, 18),
    (40, 122, 18),
    (50, 122, 18),
    (60, 122, 18),
    # NOT SUPPORTED
    # # 72+
    # (10, 80, 72),
    # (20, 80, 72),
    # (30, 80, 72),
    # (40, 80, 72),
    # (50, 80, 72),
    # (60, 80, 72),
    # (70, 80, 72),
    # (80, 80, 72),
    # (90, 80, 72),
    # # 72*
    # (10, 122, 72),
    # (20, 122, 72),
    # (30, 122, 72),
    # (40, 122, 72),
    # (50, 122, 72),
    # (60, 122, 72),
    # (70, 122, 72),
    # (80, 122, 72),
    # (90, 122, 72),
    # # VI Outdoor exclusive
    # (30, 60, 36),
    # (30, 80, 36),
    # (30, 122, 36),
]

print("INSERT INTO RangeType (DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES")
print(
    ",\n".join(f"  ({dist}, {face}, {ends})" for (dist, face, ends) in ALL_COMBINATIONS)
    + ";"
)
