#!/usr/bin/env python3
"""
Generate random INSERT statements for the Archer table.
Run:   python fill_archer_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.

This file is the MASTER configuration for every other fill script.
Change NUM_ARCHERS below and every other script will scale to match.
"""

import os
import random
from datetime import date, timedelta
import sys

from fill_junctionroundrange_inserts import JUNCTION_ROUND_DEF
from fill_rangetype_inserts import ALL_COMBINATIONS

# ════════════════════════════════════════════════════════════════════════════════
# MASTER CONFIGURATION — change num_archers to rescale the entire dataset.
# All other fill scripts import these values so their ID ranges stay aligned.
# ════════════════════════════════════════════════════════════════════════════════
num_archers = 50
if len(sys.argv) > 1:
    num_archers = int(sys.argv[1])

# Fixed reference data (do not depend on archer count). These mirror what the
# corresponding fill scripts emit, so IDs picked at random here always land on
# a real row.
NUM_EQUIPMENT = 5  # Archery Australia bow divisions
NUM_CLASSES = 16  # Standard age/gender classes
NUM_BASE_ROUNDS = max(rid for (rid, _, _) in JUNCTION_ROUND_DEF)
NUM_RANGES = len(ALL_COMBINATIONS)

# Derived counts (scale with NUM_ARCHERS so every FK has a target).
# NUM_CLUBS is intentionally small so that ClubID 1 (the "home club") ends up
# hosting most competitions — see HOME_CLUB_CHANCE in fill_competition_inserts.
NUM_CLUBS = max(4, num_archers // 12)
NUM_CHAMPIONSHIPS = max(3, num_archers // 6)
NUM_COMPETITIONS = max(8, num_archers // 2)
NUM_EQUIVALENT_ROUNDS = max(20, NUM_BASE_ROUNDS + NUM_CLASSES // 2)

# Round-scores are the "rounds shot" — keep this proportional to archers
# so every archer ends up with several score rows.
ROUNDS_PER_ARCHER = 8
NUM_ROUND_SCORES = num_archers * ROUNDS_PER_ARCHER

ARROWS_PER_END = 6
COMPETITION_CHANCE = 0.6  # probability a RoundScore is tied to a competition
CHAMPIONSHIP_CHANCE = 0.35  # probability a competition belongs to a championship

# Championship years and the competition-date window are aligned (2010-2025) so
# any competition linked to a championship can be dated inside that year. If
# you widen one, widen the other.
YEAR_MIN = 2010
YEAR_MAX = 2025
COMPETITION_DATE_MIN = date(YEAR_MIN, 1, 1)
COMPETITION_DATE_MAX = date(YEAR_MAX, 12, 31)

# Anchor year — the first ANCHOR_CHAMPIONSHIP_COUNT championships are pinned to
# this year so the default "yearly championship results" query (which filters
# ch.Year = ANCHOR_YEAR) always returns multiple championships' worth of data,
# regardless of num_archers. The remaining championships get random years.
ANCHOR_YEAR = 2017
ANCHOR_CHAMPIONSHIP_COUNT = 2

# RangeID -> NumberOfEnds. Range script inserts in list order starting at ID 1.
ENDS_PER_RANGE = {
    rid + 1: ends for rid, (_, _, ends) in enumerate(ALL_COMBINATIONS)
}

# BaseRoundID -> total ends required (sum across the round's ranges).
# This is what TotalPossibleArrows / 6 evaluates to in the Competitions query.
ENDS_PER_ROUND = {}
for base_round_id, range_id, _pos in JUNCTION_ROUND_DEF:
    ENDS_PER_ROUND[base_round_id] = (
        ENDS_PER_ROUND.get(base_round_id, 0) + ENDS_PER_RANGE[range_id]
    )

# Shared RNG seed so every script makes the same choices about which competition
# / round each RoundScore belongs to. End and Arrow counts fall out of those
# choices, so TotalArrowsShot exactly equals TotalPossibleArrows.
SEED = 42
_shared_rng = random.Random(SEED)

# Pre-decide each championship's Year (shared with fill_championship_inserts so
# competitions can be dated inside the right year). The first
# ANCHOR_CHAMPIONSHIP_COUNT are pinned to ANCHOR_YEAR so the default
# championship-results query always finds data.
_anchor = min(ANCHOR_CHAMPIONSHIP_COUNT, NUM_CHAMPIONSHIPS)
CHAMPIONSHIP_YEARS = [ANCHOR_YEAR] * _anchor + [
    _shared_rng.randint(YEAR_MIN, YEAR_MAX) for _ in range(NUM_CHAMPIONSHIPS - _anchor)
]


def _random_date_in_year(year: int) -> date:
    start = date(year, 1, 1)
    end = date(year, 12, 31)
    return start + timedelta(days=_shared_rng.randint(0, (end - start).days))


def _random_date(start: date, end: date) -> date:
    return start + timedelta(days=_shared_rng.randint(0, (end - start).days))


# Pre-decide each competition's BaseRoundID, ChampionshipID, and Date. Linking
# the championship to the date here means fill_competition_inserts just reads
# them out — the championship-year filter in Competitions.sql then returns
# rows whose dates actually fall in that year.
COMPETITION_BASE_ROUND_IDS = [
    _shared_rng.randint(1, NUM_BASE_ROUNDS) for _ in range(NUM_COMPETITIONS)
]
COMPETITION_CHAMPIONSHIP_IDS = []
COMPETITION_DATES = []
for _ in range(NUM_COMPETITIONS):
    if _shared_rng.random() < CHAMPIONSHIP_CHANCE:
        champ_id = _shared_rng.randint(1, NUM_CHAMPIONSHIPS)
        COMPETITION_CHAMPIONSHIP_IDS.append(champ_id)
        COMPETITION_DATES.append(_random_date_in_year(CHAMPIONSHIP_YEARS[champ_id - 1]))
    else:
        COMPETITION_CHAMPIONSHIP_IDS.append(None)
        COMPETITION_DATES.append(_random_date(COMPETITION_DATE_MIN, COMPETITION_DATE_MAX))

# Pre-decide each RoundScore's CompetitionID (or None) and BaseRoundID. When
# linked to a competition, the score's round MUST match the competition's
# round — otherwise the per-archer arrow total can't equal the round's
# possible-arrow count. Each (Competition, Archer) pair gets at most one
# RoundScore so the GROUP BY in the competition-results query doesn't
# aggregate two scores from the same archer into the same row.
ROUNDSCORE_COMPETITION_IDS = []
ROUNDSCORE_BASE_ROUND_IDS = []
_taken_comp_archer = set()
for i in range(NUM_ROUND_SCORES):
    archer_id = (i % num_archers) + 1  # mirrors fill_roundscore_inserts.py
    if _shared_rng.random() < COMPETITION_CHANCE:
        comp_id = _shared_rng.randint(1, NUM_COMPETITIONS)
        if (comp_id, archer_id) in _taken_comp_archer:
            comp_id = None
    else:
        comp_id = None

    if comp_id is None:
        ROUNDSCORE_COMPETITION_IDS.append(None)
        ROUNDSCORE_BASE_ROUND_IDS.append(_shared_rng.randint(1, NUM_BASE_ROUNDS))
    else:
        _taken_comp_archer.add((comp_id, archer_id))
        ROUNDSCORE_COMPETITION_IDS.append(comp_id)
        ROUNDSCORE_BASE_ROUND_IDS.append(COMPETITION_BASE_ROUND_IDS[comp_id - 1])

# End count per RoundScore is now fully determined by its BaseRoundID.
ENDS_PER_SCORE = [ENDS_PER_ROUND[r] for r in ROUNDSCORE_BASE_ROUND_IDS]
TOTAL_ENDS = sum(ENDS_PER_SCORE)
# ════════════════════════════════════════════════════════════════════════════════

MALE_FIRST = [
    "James",
    "William",
    "Oliver",
    "Noah",
    "Jack",
    "Henry",
    "Lucas",
    "Ethan",
    "Mason",
    "Logan",
    "Liam",
    "Alexander",
    "Benjamin",
    "Samuel",
    "Daniel",
    "Matthew",
    "Thomas",
    "Ryan",
    "Nathan",
    "Dylan",
]
FEMALE_FIRST = [
    "Charlotte",
    "Olivia",
    "Amelia",
    "Isla",
    "Mia",
    "Ava",
    "Grace",
    "Zoe",
    "Chloe",
    "Sophie",
    "Emily",
    "Hannah",
    "Emma",
    "Lily",
    "Isabella",
    "Ella",
    "Sophia",
    "Aria",
    "Madison",
    "Abigail",
]
LAST_NAMES = [
    "Smith",
    "Jones",
    "Williams",
    "Brown",
    "Wilson",
    "Taylor",
    "Johnson",
    "White",
    "Martin",
    "Anderson",
    "Thompson",
    "Davis",
    "Harris",
    "Clark",
    "Lewis",
    "Robinson",
    "Walker",
    "Hall",
    "Young",
    "Allen",
    "King",
    "Scott",
    "Green",
    "Baker",
    "Adams",
    "Nelson",
    "Carter",
    "Mitchell",
    "Perez",
    "Roberts",
]


def random_dob(min_age=10, max_age=75):
    today = date.today()
    max_date = today - timedelta(days=min_age * 365)
    min_date = today - timedelta(days=max_age * 365)
    delta = (max_date - min_date).days
    return min_date + timedelta(days=random.randint(0, delta))


def _build_rows():
    rows = []
    for _ in range(num_archers):
        gender = random.choice(["Male", "Female"])
        first = random.choice(MALE_FIRST if gender == "Male" else FEMALE_FIRST)
        last = random.choice(LAST_NAMES)
        dob = random_dob()
        equip = random.randint(1, NUM_EQUIPMENT)
        club = random.randint(1, NUM_CLUBS)
        rows.append(f"('{first}', '{last}', '{gender}', '{dob}', {equip}, {club})")
    return rows


if __name__ == "__main__":
    rows = _build_rows()
    print(
        "INSERT INTO Archer (FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES"
    )
    print(",\n".join(f"  {r}" for r in rows) + ";")
