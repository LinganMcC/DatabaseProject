#!/usr/bin/env python3
"""
Generate random INSERT statements for the Archer table.
Run:   python fill_archer_inserts.py
Output is printed to the console — copy/paste into phpMyAdmin.

IMPORTANT — set the ID ranges below to match what is already in your database.
"""
import random
from datetime import date, timedelta

# ── Configuration ──────────────────────────────────────────────────────────────
NUM_RECORDS      = 50
CLUB_ID_MIN      = 1    # lowest ClubID in your Club table
CLUB_ID_MAX      = 30   # highest ClubID in your Club table
EQUIPMENT_ID_MIN = 1    # lowest EquipmentID in your EquipmentType table
EQUIPMENT_ID_MAX = 5    # highest EquipmentID in your EquipmentType table
# ───────────────────────────────────────────────────────────────────────────────

MALE_FIRST   = ["James","William","Oliver","Noah","Jack","Henry","Lucas","Ethan",
                 "Mason","Logan","Liam","Alexander","Benjamin","Samuel","Daniel",
                 "Matthew","Thomas","Ryan","Nathan","Dylan"]
FEMALE_FIRST = ["Charlotte","Olivia","Amelia","Isla","Mia","Ava","Grace","Zoe",
                 "Chloe","Sophie","Emily","Hannah","Emma","Lily","Isabella",
                 "Ella","Sophia","Aria","Madison","Abigail"]
LAST_NAMES   = ["Smith","Jones","Williams","Brown","Wilson","Taylor","Johnson",
                 "White","Martin","Anderson","Thompson","Davis","Harris","Clark",
                 "Lewis","Robinson","Walker","Hall","Young","Allen","King","Scott",
                 "Green","Baker","Adams","Nelson","Carter","Mitchell","Perez","Roberts"]

def random_dob(min_age=10, max_age=75):
    today    = date.today()
    max_date = today - timedelta(days=min_age * 365)
    min_date = today - timedelta(days=max_age * 365)
    delta    = (max_date - min_date).days
    return min_date + timedelta(days=random.randint(0, delta))

rows = []
for _ in range(NUM_RECORDS):
    gender = random.choice(["Male", "Female"])
    first  = random.choice(MALE_FIRST if gender == "Male" else FEMALE_FIRST)
    last   = random.choice(LAST_NAMES)
    dob    = random_dob()
    equip  = random.randint(EQUIPMENT_ID_MIN, EQUIPMENT_ID_MAX)
    club   = random.randint(CLUB_ID_MIN, CLUB_ID_MAX)
    rows.append(f"('{first}', '{last}', '{gender}', '{dob}', {equip}, {club})")

print("INSERT INTO Archer (FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES")
print(",\n".join(f"  {r}" for r in rows) + ";")
