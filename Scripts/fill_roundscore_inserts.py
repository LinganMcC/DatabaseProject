#!/usr/bin/env python3
"""
Generate random INSERT statements for the RoundScore table.
Run:   python fill_roundscore_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.

IMPORTANT — set the ID ranges below to match what is already in your database.
CompetitionID is nullable; set COMPETITION_CHANCE to control how often a
score is linked to a competition (vs. a practice/staged score).
"""
import random
from datetime import date, timedelta

# ── Configuration ──────────────────────────────────────────────────────────────
NUM_RECORDS         = 60
ARCHER_ID_MIN       = 1
ARCHER_ID_MAX       = 50
BASE_ROUND_ID_MIN   = 1
BASE_ROUND_ID_MAX   = 25
EQUIPMENT_ID_MIN    = 1
EQUIPMENT_ID_MAX    = 5
COMPETITION_ID_MIN  = 1
COMPETITION_ID_MAX  = 40
COMPETITION_CHANCE  = 0.6    # probability a score is tied to a competition
APPROVED_CHANCE     = 0.75   # probability an entered score is approved
DATE_MIN            = date(2010, 1, 1)
DATE_MAX            = date(2025, 12, 31)
# ───────────────────────────────────────────────────────────────────────────────

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_time():
    h = random.randint(7, 17)
    m = random.choice([0, 15, 30, 45])
    return f"{h:02d}:{m:02d}:00"

rows = []
for _ in range(NUM_RECORDS):
    comp_id    = (random.randint(COMPETITION_ID_MIN, COMPETITION_ID_MAX)
                  if random.random() < COMPETITION_CHANCE else "NULL")
    archer_id  = random.randint(ARCHER_ID_MIN, ARCHER_ID_MAX)
    round_id   = random.randint(BASE_ROUND_ID_MIN, BASE_ROUND_ID_MAX)
    approved   = 1 if random.random() < APPROVED_CHANCE else 0
    equip_id   = random.randint(EQUIPMENT_ID_MIN, EQUIPMENT_ID_MAX)
    score_date = random_date(DATE_MIN, DATE_MAX)
    score_time = random_time()
    rows.append(f"({comp_id}, {archer_id}, {round_id}, {approved}, {equip_id}, '{score_date}', '{score_time}')")

print("INSERT INTO RoundScore (CompetitionID, ArcherID, BaseRoundID, IsApproved, EquipmentID, `Date`, `Time`) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
