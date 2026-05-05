"""
Archery Score Recording Database — Class table
Generates and downloads class_inserts.sql with 16 INSERT statements.
Run in Google Colab: the file will be saved and automatically downloaded.
"""

# ── Class definitions (all 16 Archery Australia age/gender classes) ────────────
# (Gender, MinAge, MaxAge)  — None stored as NULL in SQL
classes = [
    ("Female", 21, None),   # Female Open
    ("Male",   21, None),   # Male Open
    ("Female", 50, None),   # 50+ Female
    ("Male",   50, None),   # 50+ Male
    ("Female", 60, None),   # 60+ Female
    ("Male",   60, None),   # 60+ Male
    ("Female", 70, None),   # 70+ Female
    ("Male",   70, None),   # 70+ Male
    ("Female",  0, 20),     # Under 21 Female
    ("Male",    0, 20),     # Under 21 Male
    ("Female",  0, 17),     # Under 18 Female
    ("Male",    0, 17),     # Under 18 Male
    ("Female",  0, 15),     # Under 16 Female
    ("Male",    0, 15),     # Under 16 Male
    ("Female",  0, 13),     # Under 14 Female
    ("Male",    0, 13),     # Under 14 Male
]

# ── Build INSERT statements ────────────────────────────────────────────────────
insert_statements = []
insert_statements.append("-- INSERT statements for the Class table")
insert_statements.append("-- 16 rows (all Archery Australia age/gender classes)")
insert_statements.append("")

for class_id, (gender, min_age, max_age) in enumerate(classes, start=1):
    max_val = max_age if max_age is not None else "NULL"
    insert_statements.append(
        f"INSERT INTO Class (ClassID, Gender, MinAge, MaxAge) "
        f"VALUES ({class_id}, '{gender}', {min_age}, {max_val});"
    )

# ── Write output ───────────────────────────────────────────────────────────────
output_path = "class_inserts.sql"
with open(output_path, "w") as f:
    f.write("\n".join(insert_statements))

print(f"Successfully generated {len(classes)} INSERT statements at '{output_path}'")
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
