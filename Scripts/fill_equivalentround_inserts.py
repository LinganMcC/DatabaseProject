# #!/usr/bin/env python3

# Date constants for ValidFrom and ValidTo
V_FROM = "2024-01-01"
V_TO = None

# Devisions
F_O = 1  # Open Women   (21-49, before Senior 50+)
M_O = 2  # Open Men
F_50 = 3  # Senior 50+ Women
M_50 = 4  # Senior 50+ Men
S_60 = 5  # Senior 60+ Women
M_60 = 6  # Senior 60+ Men
F_70 = 7  # Senior 70+ Women
M_70 = 8  # Senior 70+ Men
F_21 = 9  # Junior Under 21 Women
M_21 = 10  # Junior Under 21 Men
F_18 = 11  # Junior Under 18 Women
M_18 = 12  # Junior Under 18 Men
F_16 = 13  # Junior Under 16 Women
M_16 = 14  # Junior Under 16 Men
F_14 = 15  # Junior Under 14 Women
M_14 = 16  # Junior Under 14 Men

# Equipment
REC = 1
COM = 2
RBB = 3
CBB = 4
LBW = 5

# fmt: off
EQUIVALENT_ROUND_DEF = [
    # (BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo)

    # --- WA90/1440 (ID: 1) ---
    (1, 1, M_O, REC, V_FROM, V_TO), (1, 1, M_O, COM, V_FROM, V_TO),
    (1, 1, M_21, REC, V_FROM, V_TO), (1, 1, M_21, COM, V_FROM, V_TO),

    # --- WA70/1440 (ID: 2) ---
    (2, 2, M_O, RBB, V_FROM, V_TO), (2, 2, M_O, CBB, V_FROM, V_TO),
    (2, 2, F_O, REC, V_FROM, V_TO), (2, 2, F_O, COM, V_FROM, V_TO),
    (2, 2, M_50, REC, V_FROM, V_TO), (2, 2, M_50, COM, V_FROM, V_TO),
    (2, 2, M_21, RBB, V_FROM, V_TO), (2, 2, M_21, CBB, V_FROM, V_TO),
    (2, 2, F_21, REC, V_FROM, V_TO), (2, 2, F_21, COM, V_FROM, V_TO),
    (2, 2, M_18, REC, V_FROM, V_TO), (2, 2, M_18, COM, V_FROM, V_TO),

    # --- WA60/1440 (ID: 3) ---
    (3, 3, M_O, LBW, V_FROM, V_TO),
    (3, 3, F_O, RBB, V_FROM, V_TO), (3, 3, F_O, CBB, V_FROM, V_TO),
    (3, 3, M_50, RBB, V_FROM, V_TO), (3, 3, M_50, CBB, V_FROM, V_TO),
    (3, 3, F_50, REC, V_FROM, V_TO), (3, 3, F_50, COM, V_FROM, V_TO), (3, 3, F_50, RBB, V_FROM, V_TO), (3, 3, F_50, CBB, V_FROM, V_TO),
    (3, 3, M_60, REC, V_FROM, V_TO), (3, 3, M_60, COM, V_FROM, V_TO), (3, 3, M_60, RBB, V_FROM, V_TO), (3, 3, M_60, CBB, V_FROM, V_TO),
    (3, 3, M_70, REC, V_FROM, V_TO), (3, 3, M_70, COM, V_FROM, V_TO), (3, 3, M_70, RBB, V_FROM, V_TO), (3, 3, M_70, CBB, V_FROM, V_TO),
    (3, 3, M_21, LBW, V_FROM, V_TO),
    (3, 3, F_21, RBB, V_FROM, V_TO), (3, 3, F_21, CBB, V_FROM, V_TO),
    (3, 3, M_18, REC, V_FROM, V_TO), (3, 3, M_18, COM, V_FROM, V_TO), (3, 3, M_18, RBB, V_FROM, V_TO), (3, 3, M_18, CBB, V_FROM, V_TO),
    (3, 3, F_18, REC, V_FROM, V_TO), (3, 3, F_18, COM, V_FROM, V_TO),

    # --- AA50/1440 (ID: 4) ---
    (4, 4, F_O, LBW, V_FROM, V_TO),
    (4, 4, M_50, LBW, V_FROM, V_TO),
    (4, 4, F_50, LBW, V_FROM, V_TO),
    (4, 4, M_60, LBW, V_FROM, V_TO), (4, 4, M_70, LBW, V_FROM, V_TO),
    (4, 4, S_60, REC, V_FROM, V_TO), (4, 4, S_60, COM, V_FROM, V_TO), (4, 4, S_60, RBB, V_FROM, V_TO), (4, 4, S_60, CBB, V_FROM, V_TO), (4, 4, S_60, LBW, V_FROM, V_TO),
    (4, 4, F_70, REC, V_FROM, V_TO), (4, 4, F_70, COM, V_FROM, V_TO), (4, 4, F_70, RBB, V_FROM, V_TO), (4, 4, F_70, CBB, V_FROM, V_TO), (4, 4, F_70, LBW, V_FROM, V_TO),
    (4, 4, F_21, LBW, V_FROM, V_TO),
    (4, 4, M_18, LBW, V_FROM, V_TO),
    (4, 4, F_18, RBB, V_FROM, V_TO), (4, 4, F_18, CBB, V_FROM, V_TO), (4, 4, F_18, LBW, V_FROM, V_TO),
    (4, 4, F_16, REC, V_FROM, V_TO), (4, 4, F_16, COM, V_FROM, V_TO),
    (4, 4, M_16, REC, V_FROM, V_TO), (4, 4, M_16, COM, V_FROM, V_TO),

    # --- AA40/1440 (ID: 5) ---
    (5, 5, F_16, RBB, V_FROM, V_TO), (5, 5, F_16, CBB, V_FROM, V_TO), (5, 5, F_16, LBW, V_FROM, V_TO),
    (5, 5, M_16, RBB, V_FROM, V_TO), (5, 5, M_16, CBB, V_FROM, V_TO), (5, 5, M_16, LBW, V_FROM, V_TO),
    (5, 5, F_14, REC, V_FROM, V_TO), (5, 5, F_14, COM, V_FROM, V_TO), (5, 5, F_14, RBB, V_FROM, V_TO), (5, 5, F_14, CBB, V_FROM, V_TO), (5, 5, F_14, LBW, V_FROM, V_TO),
    (5, 5, M_14, REC, V_FROM, V_TO), (5, 5, M_14, COM, V_FROM, V_TO), (5, 5, M_14, RBB, V_FROM, V_TO), (5, 5, M_14, CBB, V_FROM, V_TO), (5, 5, M_14, LBW, V_FROM, V_TO),

    # --- Canberra WA 60/900 (ID: 14) ---
    (14, 14, M_O, REC, V_FROM, V_TO), (14, 14, M_O, COM, V_FROM, V_TO), (14, 14, M_O, RBB, V_FROM, V_TO), (14, 14, M_O, CBB, V_FROM, V_TO), (14, 14, M_O, LBW, V_FROM, V_TO),
    (14, 14, F_O, REC, V_FROM, V_TO), (14, 14, F_O, COM, V_FROM, V_TO), (14, 14, F_O, RBB, V_FROM, V_TO), (14, 14, F_O, CBB, V_FROM, V_TO),
    (14, 14, M_50, REC, V_FROM, V_TO), (14, 14, M_50, COM, V_FROM, V_TO), (14, 14, M_50, RBB, V_FROM, V_TO), (14, 14, M_50, CBB, V_FROM, V_TO),
    (14, 14, F_50, REC, V_FROM, V_TO), (14, 14, F_50, COM, V_FROM, V_TO), (14, 14, F_50, RBB, V_FROM, V_TO), (14, 14, F_50, CBB, V_FROM, V_TO),
    (14, 14, M_60, REC, V_FROM, V_TO), (14, 14, M_60, COM, V_FROM, V_TO), (14, 14, M_60, RBB, V_FROM, V_TO), (14, 14, M_60, CBB, V_FROM, V_TO),
    (14, 14, M_70, REC, V_FROM, V_TO), (14, 14, M_70, COM, V_FROM, V_TO), (14, 14, M_70, RBB, V_FROM, V_TO), (14, 14, M_70, CBB, V_FROM, V_TO),
    (14, 14, M_21, REC, V_FROM, V_TO), (14, 14, M_21, COM, V_FROM, V_TO), (14, 14, M_21, RBB, V_FROM, V_TO), (14, 14, M_21, CBB, V_FROM, V_TO), (14, 14, M_21, LBW, V_FROM, V_TO),
    (14, 14, F_21, REC, V_FROM, V_TO), (14, 14, F_21, COM, V_FROM, V_TO), (14, 14, F_21, RBB, V_FROM, V_TO), (14, 14, F_21, CBB, V_FROM, V_TO),
    (14, 14, M_18, REC, V_FROM, V_TO), (14, 14, M_18, COM, V_FROM, V_TO), (14, 14, M_18, RBB, V_FROM, V_TO), (14, 14, M_18, CBB, V_FROM, V_TO),
    (14, 14, F_18, REC, V_FROM, V_TO), (14, 14, F_18, COM, V_FROM, V_TO),

    # --- Short Canberra (ID: 15) ---
    (15, 15, F_O, LBW, V_FROM, V_TO),
    (15, 15, M_50, LBW, V_FROM, V_TO),
    (15, 15, F_50, LBW, V_FROM, V_TO),
    (15, 15, M_60, LBW, V_FROM, V_TO), (15, 15, M_70, LBW, V_FROM, V_TO),
    (15, 15, S_60, REC, V_FROM, V_TO), (15, 15, S_60, COM, V_FROM, V_TO), (15, 15, S_60, RBB, V_FROM, V_TO), (15, 15, S_60, CBB, V_FROM, V_TO), (15, 15, S_60, LBW, V_FROM, V_TO),
    (15, 15, F_70, REC, V_FROM, V_TO), (15, 15, F_70, COM, V_FROM, V_TO), (15, 15, F_70, RBB, V_FROM, V_TO), (15, 15, F_70, CBB, V_FROM, V_TO), (15, 15, F_70, LBW, V_FROM, V_TO),
    (15, 15, F_21, LBW, V_FROM, V_TO),
    (15, 15, M_18, LBW, V_FROM, V_TO),
    (15, 15, F_18, RBB, V_FROM, V_TO), (15, 15, F_18, CBB, V_FROM, V_TO), (15, 15, F_18, LBW, V_FROM, V_TO),
    (15, 15, F_16, REC, V_FROM, V_TO), (15, 15, F_16, COM, V_FROM, V_TO),
    (15, 15, M_16, REC, V_FROM, V_TO), (15, 15, M_16, COM, V_FROM, V_TO),

    # --- Junior Canberra (ID: 16) ---
    (16, 16, F_16, RBB, V_FROM, V_TO), (16, 16, F_16, CBB, V_FROM, V_TO), (16, 16, F_16, LBW, V_FROM, V_TO),
    (16, 16, M_16, RBB, V_FROM, V_TO), (16, 16, M_16, CBB, V_FROM, V_TO), (16, 16, M_16, LBW, V_FROM, V_TO),
    (16, 16, F_14, REC, V_FROM, V_TO), (16, 16, F_14, COM, V_FROM, V_TO), (16, 16, F_14, RBB, V_FROM, V_TO), (16, 16, F_14, CBB, V_FROM, V_TO), (16, 16, F_14, LBW, V_FROM, V_TO),
    (16, 16, M_14, REC, V_FROM, V_TO), (16, 16, M_14, COM, V_FROM, V_TO), (16, 16, M_14, RBB, V_FROM, V_TO), (16, 16, M_14, CBB, V_FROM, V_TO), (16, 16, M_14, LBW, V_FROM, V_TO)
]
# fmt: on

print(
    "INSERT INTO EquivalentRound (BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES"
)
print(
    ",\n".join(
        f"  ({base}, {actaul}, {clss}, {eqmt}, '{valfr}', {f"'{valto}'" if valto else "NULL"})"
        for (base, actaul, clss, eqmt, valfr, valto) in EQUIVALENT_ROUND_DEF
    )
    + ";"
)
