#!/usr/bin/env python3
"""
Generate random INSERT statements for the Club table.
Run:   python fill_club_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.
"""
import random

# ── Configuration ──────────────────────────────────────────────────────────────
NUM_RECORDS = 30
# ───────────────────────────────────────────────────────────────────────────────

CITIES = [
    "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Canberra",
    "Hobart", "Darwin", "Newcastle", "Wollongong", "Geelong", "Townsville",
    "Cairns", "Toowoomba", "Ballarat", "Bendigo", "Albury", "Launceston",
    "Mackay", "Rockhampton", "Bunbury", "Mandurah", "Wagga Wagga",
    "Mildura", "Shepparton", "Hervey Bay", "Gladstone", "Tamworth",
    "Orange", "Dubbo", "Bathurst", "Grafton", "Lismore", "Armidale",
    "Cessnock", "Maitland", "Nowra", "Queanbeyan", "Warrnambool",
    "Frankston", "Ringwood", "Dandenong", "Broadmeadows", "Sunshine",
    "Parramatta", "Penrith", "Campbelltown", "Blacktown", "Liverpool",
]

SUFFIXES = [
    "Archers", "Archery Club", "Bowmen", "Field Archers",
    "Archery Association", "Target Archers", "Archery Society",
    "Archery Group", "Archery Inc", "Bowmen Club",
]

names = set()
while len(names) < NUM_RECORDS:
    names.add(f"{random.choice(CITIES)} {random.choice(SUFFIXES)}")

rows = [f"('{name}')" for name in sorted(names)]

print("INSERT INTO Club (Name) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
