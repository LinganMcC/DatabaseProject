#!/usr/bin/env python3
"""
Generate random INSERT statements for the Competition table.
ID ranges are pulled from fill_archer_inserts so every FK is valid and
the count scales with the master archer count.
Run:   python fill_competition_inserts.py
"""

import random
from datetime import date, timedelta
from fill_archer_inserts import (
    NUM_BASE_ROUNDS,
    NUM_CLUBS,
    NUM_CHAMPIONSHIPS,
    NUM_COMPETITIONS,
)

CHAMPIONSHIP_CHANCE = 0.35
DATE_MIN = date(2010, 1, 1)
DATE_MAX = date(2025, 12, 31)

PREFIXES = [
    "Annual",
    "Open",
    "Club",
    "Regional",
    "State",
    "Invitational",
    "Summer",
    "Winter",
    "Spring",
    "Youth",
    "Masters",
    "Charity",
]
SUFFIXES = [
    "Championship",
    "Tournament",
    "Classic",
    "Open",
    "Cup",
    "Series",
    "Challenge",
    "Shoot",
    "Meet",
    "Event",
]


def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))


def random_name():
    return f"{random.choice(PREFIXES)} Archery {random.choice(SUFFIXES)}"


rows = []
for _ in range(NUM_COMPETITIONS):
    round_id = random.randint(1, NUM_BASE_ROUNDS)
    club_id = random.randint(1, NUM_CLUBS)
    champ_id = (
        random.randint(1, NUM_CHAMPIONSHIPS)
        if random.random() < CHAMPIONSHIP_CHANCE
        else "NULL"
    )
    comp_date = random_date(DATE_MIN, DATE_MAX)
    name = random_name().replace("'", "''")
    rows.append(f"({round_id}, {club_id}, {champ_id}, '{comp_date}', '{name}')")

print(
    "INSERT INTO Competition (BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES"
)
print(",\n".join(f"  {r}" for r in rows) + ";")
