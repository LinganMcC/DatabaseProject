"""
Archery Score Recording Database — EquipmentType table
Generates and downloads equipmenttype_inserts.sql with 5 INSERT statements.
Run in Google Colab: the file will be saved and automatically downloaded.
"""

# ── Equipment data (all 5 legal divisions) ─────────────────────────────────────
equipment_types = [
    ("Recurve",          "RC"),
    ("Compound",         "C"),
    ("Recurve Barebow",  "RB"),
    ("Compound Barebow", "CB"),
    ("Longbow",          "L"),
]

def escape_sql(value):
    return str(value).replace("'", "''")

# ── Build INSERT statements ────────────────────────────────────────────────────
insert_statements = []
insert_statements.append("-- INSERT statements for the EquipmentType table")
insert_statements.append("-- 5 rows (all legal equipment divisions)")
insert_statements.append("")

for equipment_id, (name, code) in enumerate(equipment_types, start=1):
    insert_statements.append(
        f"INSERT INTO EquipmentType (EquipmentID, Name, DivisionCode) "
        f"VALUES ({equipment_id}, '{escape_sql(name)}', '{code}');"
    )


# ── Write output ───────────────────────────────────────────────────────────────
output_path = "equipmenttype_inserts.sql"
with open(output_path, "w") as f:
    f.write("\n".join(insert_statements))

print(f"Successfully generated {len([s for s in insert_statements if s.startswith('INSERT')])} INSERT statements at '{output_path}'")
print("\nAll statements:")
for stmt in insert_statements[3:]:
    print(stmt)

# ── Google Colab download ──────────────────────────────────────────────────────
try:
    from google.colab import files  # type: ignore
    files.download(output_path)
    print("\nDownload triggered.")
except ImportError:
    print("\n(Not running in Colab — file saved locally.)")
