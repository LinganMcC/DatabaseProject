#!/usr/bin/env python3
"""
Generate random INSERT statements for the BaseRound table.
Produces a realistic mix of WA, national, and local Australian rounds.
Run:   python fill_baseround_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.
"""
import random

# ── Configuration ──────────────────────────────────────────────────────────────
NUM_RECORDS = 25
# ───────────────────────────────────────────────────────────────────────────────

WA_ROUNDS = [
    "WA1440", "WA900", "WA70", "WA60", "WA50+/30",
    "WA25", "WA18", "WA3D", "WA Field",
    "Olympic Round", "WA720",
]

AUSTRALIAN_ROUNDS = [
    "Sydney Round", "Melbourne Round", "Adelaide Round",
    "Brisbane Round", "Perth Round", "Canberra Round",
    "Hobart Round", "Darwin Round", "National Round",
    "State Round", "Club Round", "Short Metropolitan",
    "Long Metropolitan", "Short Junior", "Long Junior",
    "Half WA1440", "Statewide Round", "Regional Round",
    "Frostbite Round", "Clout Round",
]

INDOOR_ROUNDS = [
    "18m Indoor Round", "25m Indoor Round",
    "WA18 Indoor", "WA25 Indoor",
]

pool = WA_ROUNDS + AUSTRALIAN_ROUNDS + INDOOR_ROUNDS
random.shuffle(pool)
selected = list(dict.fromkeys(pool))[:NUM_RECORDS]

rows = [f"('{name}')" for name in selected]

print("INSERT INTO BaseRound (RoundName) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
