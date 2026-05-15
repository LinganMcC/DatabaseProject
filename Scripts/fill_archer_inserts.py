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

# ════════════════════════════════════════════════════════════════════════════════
# MASTER CONFIGURATION — change num_archers to rescale the entire dataset.
# All other fill scripts import these values so their ID ranges stay aligned.
# ════════════════════════════════════════════════════════════════════════════════
num_archers = 50
if len(sys.argv) > 1:
    num_archers = int(sys.argv[1])

# Fixed reference data (do not depend on archer count).
NUM_EQUIPMENT = 5  # Archery Australia bow divisions
NUM_CLASSES = 16  # Standard age/gender classes
NUM_BASE_ROUNDS = 25  # Variety of round types
NUM_RANGES = 20  # Distance/face/end combinations

# Derived counts (scale with NUM_ARCHERS so every FK has a target).
NUM_CLUBS = max(5, num_archers // 5)
NUM_CHAMPIONSHIPS = max(3, num_archers // 6)
NUM_COMPETITIONS = max(8, num_archers // 2)
NUM_EQUIVALENT_ROUNDS = max(20, NUM_BASE_ROUNDS + NUM_CLASSES // 2)

# Round-scores are the "rounds shot" — keep this proportional to archers
# so every archer ends up with several score rows.
ROUNDS_PER_ARCHER = 8
NUM_ROUND_SCORES = num_archers * ROUNDS_PER_ARCHER

# Ends per round score (used by both fill_end_inserts and fill_arrow_inserts).
ENDS_PER_SCORE_MIN = 6
ENDS_PER_SCORE_MAX = 12
ARROWS_PER_END = 6

# Shared RNG seed so the end script and arrow script agree on how many
# ends each RoundScore has — that way arrow's EndID range is exact.
SEED = 42
_end_rng = random.Random(SEED)
ENDS_PER_SCORE = [
    _end_rng.randint(ENDS_PER_SCORE_MIN, ENDS_PER_SCORE_MAX)
    for _ in range(NUM_ROUND_SCORES)
]
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
