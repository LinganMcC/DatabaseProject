#!/usr/bin/env python3
"""
Generate random INSERT statements for the Competition table.
Run:   python fill_competition_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.

IMPORTANT — set the ID ranges below to match what is already in your database.
ChampionshipID is nullable; set CHAMPIONSHIP_CHANCE to control how often a
competition is linked to a championship (0.0 = never, 1.0 = always).
"""
import random
from datetime import date, timedelta

# ── Configuration ──────────────────────────────────────────────────────────────
NUM_RECORDS           = 40
BASE_ROUND_ID_MIN     = 1
BASE_ROUND_ID_MAX     = 25
CLUB_ID_MIN           = 1
CLUB_ID_MAX           = 30
CHAMPIONSHIP_ID_MIN   = 1
CHAMPIONSHIP_ID_MAX   = 40
CHAMPIONSHIP_CHANCE   = 0.35   # probability a competition is part of a championship
DATE_MIN              = date(2010, 1, 1)
DATE_MAX              = date(2025, 12, 31)
# ───────────────────────────────────────────────────────────────────────────────

PREFIXES = ["Annual", "Open", "Club", "Regional", "State", "Invitational",
            "Summer", "Winter", "Spring", "Youth", "Masters", "Charity"]
SUFFIXES = ["Championship", "Tournament", "Classic", "Open", "Cup",
            "Series", "Challenge", "Shoot", "Meet", "Event"]

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_name():
    return f"{random.choice(PREFIXES)} Archery {random.choice(SUFFIXES)}"

rows = []
for _ in range(NUM_RECORDS):
    round_id  = random.randint(BASE_ROUND_ID_MIN, BASE_ROUND_ID_MAX)
    club_id   = random.randint(CLUB_ID_MIN, CLUB_ID_MAX)
    champ_id  = (random.randint(CHAMPIONSHIP_ID_MIN, CHAMPIONSHIP_ID_MAX)
                 if random.random() < CHAMPIONSHIP_CHANCE else "NULL")
    comp_date = random_date(DATE_MIN, DATE_MAX)
    name      = random_name().replace("'", "''")
    rows.append(f"({round_id}, {club_id}, {champ_id}, '{comp_date}', '{name}')")

print("INSERT INTO Competition (BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
