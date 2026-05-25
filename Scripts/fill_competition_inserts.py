#!/usr/bin/env python3
"""
Generate random INSERT statements for the Competition table.
ID ranges are pulled from fill_archer_inserts so every FK is valid and
the count scales with the master archer count.
Run:   python fill_competition_inserts.py
"""

import random
from fill_archer_inserts import (
    NUM_CLUBS,
    NUM_COMPETITIONS,
    COMPETITION_BASE_ROUND_IDS,
    COMPETITION_CHAMPIONSHIP_IDS,
    COMPETITION_DATES,
)

# ClubID 1 is the "home club" — most competitions are hosted there so club-
# scoped queries have rich data without needing many clubs in the dataset.
HOME_CLUB_ID = 1
HOME_CLUB_CHANCE = 0.6


def pick_club_id():
    if NUM_CLUBS == 1 or random.random() < HOME_CLUB_CHANCE:
        return HOME_CLUB_ID
    return random.randint(2, NUM_CLUBS)

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


def random_name():
    return f"{random.choice(PREFIXES)} Archery {random.choice(SUFFIXES)}"


rows = []
for i in range(NUM_COMPETITIONS):
    round_id = COMPETITION_BASE_ROUND_IDS[i]
    club_id = pick_club_id()
    champ_id_value = COMPETITION_CHAMPIONSHIP_IDS[i]
    champ_id = "NULL" if champ_id_value is None else champ_id_value
    comp_date = COMPETITION_DATES[i]
    name = random_name().replace("'", "''")
    rows.append(f"({round_id}, {club_id}, {champ_id}, '{comp_date}', '{name}')")

print(
    "INSERT INTO Competition (BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES"
)
print(",\n".join(f"  {r}" for r in rows) + ";")
