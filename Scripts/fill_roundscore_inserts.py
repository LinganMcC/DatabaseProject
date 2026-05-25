#!/usr/bin/env python3
"""
Generate random INSERT statements for the RoundScore table.
Count and ID ranges are pulled from fill_archer_inserts so every archer
gets ROUNDS_PER_ARCHER score rows and every FK lands inside an inserted
parent row.
Run:   python fill_roundscore_inserts.py
"""

import random
from datetime import date, timedelta
from fill_archer_inserts import (
    num_archers,
    NUM_EQUIPMENT,
    NUM_ROUND_SCORES,
    ROUNDSCORE_COMPETITION_IDS,
    ROUNDSCORE_BASE_ROUND_IDS,
)

APPROVED_CHANCE = 0.75  # probability an entered score is approved
DATE_MIN = date(2010, 1, 1)
DATE_MAX = date(2025, 12, 31)


def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))


def random_time():
    h = random.randint(7, 17)
    m = random.choice([0, 15, 30, 45])
    return f"{h:02d}:{m:02d}:00"


rows = []
# Round-robin archer IDs so every archer gets at least one score, then top up
# with random picks. This guarantees Archer-keyed queries return results.
for i in range(NUM_ROUND_SCORES):
    archer_id = (i % num_archers) + 1
    comp_id_value = ROUNDSCORE_COMPETITION_IDS[i]
    comp_id = "NULL" if comp_id_value is None else comp_id_value
    round_id = ROUNDSCORE_BASE_ROUND_IDS[i]
    approved = 1 if random.random() < APPROVED_CHANCE else 0
    equip_id = random.randint(1, NUM_EQUIPMENT)
    score_date = random_date(DATE_MIN, DATE_MAX)
    score_time = random_time()
    rows.append(
        f"({comp_id}, {archer_id}, {round_id}, {approved}, {equip_id}, '{score_date}', '{score_time}')"
    )

print(
    "INSERT INTO RoundScore (CompetitionID, ArcherID, BaseRoundID, IsApproved, EquipmentID, `Date`, `Time`) VALUES"
)
print(",\n".join(f"  {r}" for r in rows) + ";")
