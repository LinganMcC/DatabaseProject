#!/usr/bin/env python3
"""
Generate random INSERT statements for the BaseRound table.
Count is pulled from fill_archer_inserts.NUM_BASE_ROUNDS so BaseRoundIDs
match the range used by Competition / RoundScore / EquivalentRound /
JunctionRoundRange scripts.
Run:   python fill_baseround_inserts.py
"""

# See Here: https://archeryaustralia.app.box.com/s/79h2zc3q0bu8ks172rdbdpzg9kpdo2f6
# Page 63-65
BASE_ROUND_NAMES = [
    # Blue
    "WA90/1440",
    "WA70/1440",
    "WA60/1440",
    "AA50/1440",
    "AA40/1440",
    # Green
    "Long Sydney",
    "Sydney",
    "Long Brisbane",
    "Brisbane",
    "Adelaide",
    "Short Adeliade",
    # Yellow
    "Hobart",
    "Pert",
    "48^Canberra WA60/900",
    "Junior Canberra",
    "49^Mini Canberra",
    "Grange",
    "Melbourne",
    "Darwin",
    "Geelong",
    "Newcastle",
    "Holt",
    "Samford",
    "Drake",
    # Bronze
    "Wollongong",
    "Townsville",
    "Launceston",
    # Grey NOT SUPPORTED
    # "WA70/720",
    # "WA60/720",
    # "WA50/720",
    # "WA50/720 50^WABB50/720",
    # "WA40/720",
    # "WA30/720",
    # "WA20/720",
    # "WA20/720",
    # "VI Outdoor^52",
    # "VI 30m Round^53",
]

print("INSERT INTO BaseRound (RoundName) VALUES")
print(",\n".join(f"  ('{r}')" for r in BASE_ROUND_NAMES) + ";")
