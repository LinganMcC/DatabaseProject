#!/usr/bin/env python3
"""
Generate random INSERT statements for the EquivalentRound table.
ID ranges are pulled from fill_archer_inserts so every FK lands inside
a row that actually exists.
Run:   python fill_equivalentround_inserts.py
"""

import random
from datetime import date, timedelta
from fill_archer_inserts import (
    NUM_BASE_ROUNDS,
    NUM_CLASSES,
    NUM_EQUIPMENT,
    NUM_EQUIVALENT_ROUNDS,
)

STILL_VALID_CHANCE = 0.5  # probability ValidTo is NULL (mapping still active)


def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))


rows = []
for _ in range(NUM_EQUIVALENT_ROUNDS):
    base_round = random.randint(1, NUM_BASE_ROUNDS)
    actual_round = random.choice(
        [r for r in range(1, NUM_BASE_ROUNDS + 1) if r != base_round]
    )
    class_id = random.randint(1, NUM_CLASSES)
    equip_id = random.randint(1, NUM_EQUIPMENT)
    valid_from = random_date(date(2000, 1, 1), date(2020, 1, 1))
    if random.random() < STILL_VALID_CHANCE:
        valid_to = "NULL"
    else:
        valid_to = (
            f"'{random_date(valid_from + timedelta(days=365), date(2025, 12, 31))}'"
        )
    rows.append(
        f"({base_round}, {actual_round}, {class_id}, {equip_id}, '{valid_from}', {valid_to})"
    )

print(
    "INSERT INTO EquivalentRound (BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES"
)
print(",\n".join(f"  {r}" for r in rows) + ";")
