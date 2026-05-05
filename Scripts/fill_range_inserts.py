"""
Archery Score Recording Database — Range table
Generates and downloads range_inserts.sql with 28 INSERT statements.
Run in Google Colab: the file will be saved and automatically downloaded.

Table: Range(RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds)
28 rows — all legal combinations of distance, face size and ends count.
"""

import itertools

# ── Data pools ─────────────────────────────────────────────────────────────────
# All legal archery range parameters (per Archery Australia rules)
distances     = [20, 30, 40, 50, 60, 70, 90]   # valid distances in metres (80m not used)
target_faces  = [80, 122]                        # valid target face sizes in cm
ends_options  = [5, 6]                           # valid ends per range



# ── Pre-generated INSERT statements ───────────────────────────────────────────
insert_statements = []
insert_statements.append("-- INSERT statements for the Range table")
insert_statements.append("-- 28 rows")
insert_statements.append("")

sql_data = """\
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (1, 20, 80, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (2, 20, 80, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (3, 20, 122, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (4, 20, 122, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (5, 30, 80, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (6, 30, 80, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (7, 30, 122, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (8, 30, 122, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (9, 40, 80, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (10, 40, 80, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (11, 40, 122, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (12, 40, 122, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (13, 50, 80, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (14, 50, 80, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (15, 50, 122, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (16, 50, 122, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (17, 60, 80, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (18, 60, 80, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (19, 60, 122, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (20, 60, 122, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (21, 70, 80, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (22, 70, 80, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (23, 70, 122, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (24, 70, 122, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (25, 90, 80, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (26, 90, 80, 6);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (27, 90, 122, 5);
INSERT INTO Range (RangeID, DistanceToTargetM, TargetFaceCm, NumberOfEnds) VALUES (28, 90, 122, 6);"""

insert_statements.extend(sql_data.strip().splitlines())

# ── Write output ───────────────────────────────────────────────────────────────
output_path = "range_inserts.sql"
with open(output_path, "w") as f:
    f.write("\n".join(insert_statements))

count_written = sum(1 for s in insert_statements if s.startswith("INSERT"))
print(f"Successfully generated {count_written} INSERT statements at '{output_path}'")
print("\nFirst 3 sample statements:")
for stmt in insert_statements[3:6]:
    print(stmt)

# ── Google Colab download ──────────────────────────────────────────────────────
try:
    from google.colab import files  # type: ignore
    files.download(output_path)
    print("\nDownload triggered.")
except ImportError:
    print("\n(Not running in Colab — file saved locally.)")
