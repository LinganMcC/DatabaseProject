#!/usr/bin/env python3
"""
Generate INSERT statements for the RangeType table.
ALL_COMBINATIONS is imported by fill_archer_inserts so its order defines
the RangeID assigned by AUTO_INCREMENT.
Run:   python fill_rangetype_inserts.py
"""

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
    (80, 80, 5),  # 80m Not used but keep for database purpose
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
    # 72+
    (10, 80, 12),
    (20, 80, 12),
    (30, 80, 12),
    (40, 80, 12),
    (50, 80, 12),
    (60, 80, 12),
    (70, 80, 12),
    (80, 80, 12),
    (90, 80, 12),
    # 72*
    (10, 122, 12),
    (20, 122, 12),
    (30, 122, 12),
    (40, 122, 12),
    (50, 122, 12),
    (60, 122, 12),
    (70, 122, 12),
    (80, 122, 12),
    (90, 122, 12),
    # VI Outdoor exclusive
    (30, 60, 36),
    (30, 80, 36),
    (30, 122, 36),
]

if __name__ == "__main__":
    print(
        "INSERT INTO RangeType (DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES"
    )
    print(
        ",\n".join(
            f"  ({dist}, {face}, {ends})" for (dist, face, ends) in ALL_COMBINATIONS
        )
        + ";"
    )
