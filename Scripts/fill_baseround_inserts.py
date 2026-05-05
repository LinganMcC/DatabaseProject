"""
Archery Score Recording Database — Baseround table
Generates and downloads baseround_inserts.sql with 500 INSERT statements.
Run in Google Colab: the file will be saved and automatically downloaded.

Table: BaseRound(BaseRoundID, RoundName)
"""

import random

# ── Data pools ─────────────────────────────────────────────────────────────────
round_names_pool = [
    "WA90/1440", "WA70/1440", "WA60/1440", "AA50/1440", "AA40/1440",
    "WA720 Recurve", "WA720 Compound", "WA900",
    "Long Sydney", "Sydney", "Short Sydney",
    "Long Brisbane", "Brisbane", "Short Brisbane",
    "Adelaide", "Short Adelaide", "Long Adelaide",
    "Long Hobart", "Hobart", "Short Hobart",
    "Long Perth", "Perth", "Short Perth",
    "Darwin", "Canberra", "Long Melbourne", "Melbourne", "Short Melbourne",
    "Townsville", "Cairns", "WA 18 (Indoor)", "WA 25 (Indoor)",
    "Bray I", "Bray II", "Double Clout", "Single Clout",
    "Windsor", "Short Windsor", "Long Windsor", "Albion", "York",
    "Hereford", "St Nicholas", "National", "Western", "Eastern",
    "New Western", "New National", "Junior WA 70", "Junior WA 60",
]

def escape_sql(value):
    return str(value).replace("'", "''")

# ── Pre-generated INSERT statements ───────────────────────────────────────────
insert_statements = []
insert_statements.append("-- INSERT statements for the Baseround table")
insert_statements.append("-- 500 rows")
insert_statements.append("")

sql_data = """\
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (1, 'Western Variant 1');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (2, 'Long Perth Variant 2');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (3, 'Melbourne Variant 3');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (4, 'Darwin Variant 4');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (5, 'WA720 Compound Variant 5');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (6, 'Sydney Variant 6');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (7, 'Short Melbourne Variant 7');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (8, 'Hereford Variant 8');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (9, 'Short Windsor Variant 9');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (10, 'Long Adelaide Variant 10');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (11, 'Long Adelaide Variant 11');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (12, 'Double Clout Variant 12');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (13, 'Short Melbourne Variant 13');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (14, 'Windsor Variant 14');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (15, 'Darwin Variant 15');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (16, 'Albion Variant 16');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (17, 'Long Hobart Variant 17');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (18, 'National Variant 18');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (19, 'Long Melbourne Variant 19');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (20, 'Junior WA 70 Variant 20');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (21, 'Short Brisbane Variant 21');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (22, 'Melbourne Variant 22');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (23, 'Single Clout Variant 23');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (24, 'Single Clout Variant 24');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (25, 'WA 18 (Indoor) Variant 25');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (26, 'Long Brisbane Variant 26');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (27, 'Darwin Variant 27');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (28, 'Single Clout Variant 28');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (29, 'Single Clout Variant 29');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (30, 'WA 18 (Indoor) Variant 30');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (31, 'Long Adelaide Variant 31');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (32, 'Short Hobart Variant 32');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (33, 'Windsor Variant 33');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (34, 'Short Perth Variant 34');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (35, 'Junior WA 60 Variant 35');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (36, 'Eastern Variant 36');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (37, 'Long Melbourne Variant 37');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (38, 'New National Variant 38');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (39, 'Long Sydney Variant 39');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (40, 'St Nicholas Variant 40');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (41, 'WA900 Variant 41');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (42, 'New National Variant 42');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (43, 'Adelaide Variant 43');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (44, 'Townsville Variant 44');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (45, 'Western Variant 45');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (46, 'Short Sydney Variant 46');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (47, 'WA720 Compound Variant 47');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (48, 'Short Brisbane Variant 48');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (49, 'Bray I Variant 49');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (50, 'Long Melbourne Variant 50');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (51, 'Perth Variant 51');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (52, 'Single Clout Variant 52');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (53, 'Albion Variant 53');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (54, 'Western Variant 54');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (55, 'National Variant 55');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (56, 'Eastern Variant 56');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (57, 'AA50/1440 Variant 57');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (58, 'Short Sydney Variant 58');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (59, 'Canberra Variant 59');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (60, 'York Variant 60');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (61, 'WA90/1440 Variant 61');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (62, 'WA720 Recurve Variant 62');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (63, 'Sydney Variant 63');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (64, 'WA 18 (Indoor) Variant 64');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (65, 'Long Windsor Variant 65');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (66, 'Short Melbourne Variant 66');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (67, 'WA720 Recurve Variant 67');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (68, 'AA40/1440 Variant 68');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (69, 'Long Adelaide Variant 69');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (70, 'Adelaide Variant 70');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (71, 'Darwin Variant 71');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (72, 'WA720 Recurve Variant 72');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (73, 'Long Windsor Variant 73');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (74, 'WA60/1440 Variant 74');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (75, 'New Western Variant 75');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (76, 'Canberra Variant 76');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (77, 'Long Melbourne Variant 77');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (78, 'Albion Variant 78');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (79, 'Hereford Variant 79');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (80, 'Bray II Variant 80');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (81, 'Hobart Variant 81');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (82, 'Eastern Variant 82');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (83, 'Long Windsor Variant 83');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (84, 'AA50/1440 Variant 84');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (85, 'Junior WA 60 Variant 85');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (86, 'Long Brisbane Variant 86');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (87, 'York Variant 87');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (88, 'WA 25 (Indoor) Variant 88');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (89, 'Townsville Variant 89');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (90, 'WA90/1440 Variant 90');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (91, 'Brisbane Variant 91');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (92, 'St Nicholas Variant 92');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (93, 'Bray II Variant 93');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (94, 'Hobart Variant 94');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (95, 'Brisbane Variant 95');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (96, 'WA60/1440 Variant 96');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (97, 'Long Windsor Variant 97');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (98, 'Bray I Variant 98');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (99, 'Bray II Variant 99');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (100, 'Western Variant 100');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (101, 'Adelaide Variant 101');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (102, 'Albion Variant 102');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (103, 'Short Sydney Variant 103');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (104, 'National Variant 104');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (105, 'WA60/1440 Variant 105');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (106, 'Darwin Variant 106');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (107, 'Short Adelaide Variant 107');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (108, 'Hereford Variant 108');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (109, 'WA90/1440 Variant 109');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (110, 'Short Sydney Variant 110');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (111, 'WA720 Recurve Variant 111');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (112, 'Long Hobart Variant 112');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (113, 'Junior WA 60 Variant 113');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (114, 'Long Melbourne Variant 114');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (115, 'Short Perth Variant 115');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (116, 'St Nicholas Variant 116');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (117, 'Long Melbourne Variant 117');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (118, 'Long Melbourne Variant 118');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (119, 'Short Windsor Variant 119');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (120, 'Brisbane Variant 120');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (121, 'Bray II Variant 121');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (122, 'WA90/1440 Variant 122');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (123, 'New National Variant 123');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (124, 'Eastern Variant 124');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (125, 'AA40/1440 Variant 125');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (126, 'WA720 Recurve Variant 126');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (127, 'Single Clout Variant 127');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (128, 'Hobart Variant 128');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (129, 'New Western Variant 129');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (130, 'Single Clout Variant 130');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (131, 'Short Windsor Variant 131');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (132, 'Short Perth Variant 132');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (133, 'Short Perth Variant 133');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (134, 'Long Hobart Variant 134');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (135, 'Adelaide Variant 135');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (136, 'Long Windsor Variant 136');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (137, 'Brisbane Variant 137');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (138, 'Cairns Variant 138');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (139, 'Long Melbourne Variant 139');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (140, 'Windsor Variant 140');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (141, 'WA90/1440 Variant 141');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (142, 'Long Adelaide Variant 142');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (143, 'Long Brisbane Variant 143');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (144, 'Melbourne Variant 144');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (145, 'Bray I Variant 145');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (146, 'WA720 Compound Variant 146');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (147, 'Single Clout Variant 147');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (148, 'AA40/1440 Variant 148');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (149, 'Bray I Variant 149');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (150, 'Hobart Variant 150');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (151, 'Perth Variant 151');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (152, 'WA900 Variant 152');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (153, 'Bray I Variant 153');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (154, 'Long Adelaide Variant 154');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (155, 'Double Clout Variant 155');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (156, 'Windsor Variant 156');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (157, 'Long Adelaide Variant 157');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (158, 'Western Variant 158');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (159, 'Townsville Variant 159');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (160, 'Canberra Variant 160');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (161, 'Windsor Variant 161');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (162, 'WA 18 (Indoor) Variant 162');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (163, 'Junior WA 60 Variant 163');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (164, 'Short Adelaide Variant 164');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (165, 'Junior WA 70 Variant 165');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (166, 'Perth Variant 166');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (167, 'Junior WA 60 Variant 167');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (168, 'Cairns Variant 168');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (169, 'National Variant 169');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (170, 'Cairns Variant 170');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (171, 'Short Windsor Variant 171');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (172, 'WA70/1440 Variant 172');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (173, 'WA 18 (Indoor) Variant 173');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (174, 'WA900 Variant 174');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (175, 'Long Adelaide Variant 175');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (176, 'AA40/1440 Variant 176');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (177, 'Canberra Variant 177');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (178, 'York Variant 178');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (179, 'Adelaide Variant 179');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (180, 'National Variant 180');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (181, 'Western Variant 181');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (182, 'Adelaide Variant 182');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (183, 'Long Perth Variant 183');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (184, 'Melbourne Variant 184');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (185, 'Short Perth Variant 185');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (186, 'Bray II Variant 186');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (187, 'Double Clout Variant 187');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (188, 'WA90/1440 Variant 188');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (189, 'Western Variant 189');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (190, 'Long Adelaide Variant 190');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (191, 'Short Adelaide Variant 191');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (192, 'Hobart Variant 192');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (193, 'WA720 Recurve Variant 193');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (194, 'Long Melbourne Variant 194');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (195, 'National Variant 195');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (196, 'New National Variant 196');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (197, 'Perth Variant 197');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (198, 'AA40/1440 Variant 198');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (199, 'Single Clout Variant 199');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (200, 'Long Brisbane Variant 200');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (201, 'WA 18 (Indoor) Variant 201');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (202, 'Long Perth Variant 202');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (203, 'Short Perth Variant 203');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (204, 'Short Brisbane Variant 204');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (205, 'Windsor Variant 205');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (206, 'Long Hobart Variant 206');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (207, 'Long Brisbane Variant 207');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (208, 'New National Variant 208');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (209, 'National Variant 209');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (210, 'Brisbane Variant 210');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (211, 'WA 25 (Indoor) Variant 211');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (212, 'New National Variant 212');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (213, 'Brisbane Variant 213');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (214, 'Short Adelaide Variant 214');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (215, 'New National Variant 215');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (216, 'Short Adelaide Variant 216');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (217, 'Long Adelaide Variant 217');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (218, 'Short Brisbane Variant 218');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (219, 'Adelaide Variant 219');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (220, 'Brisbane Variant 220');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (221, 'Short Adelaide Variant 221');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (222, 'Albion Variant 222');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (223, 'Short Perth Variant 223');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (224, 'Sydney Variant 224');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (225, 'Junior WA 60 Variant 225');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (226, 'WA720 Compound Variant 226');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (227, 'WA900 Variant 227');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (228, 'WA720 Recurve Variant 228');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (229, 'National Variant 229');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (230, 'St Nicholas Variant 230');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (231, 'WA 25 (Indoor) Variant 231');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (232, 'Albion Variant 232');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (233, 'WA90/1440 Variant 233');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (234, 'Junior WA 70 Variant 234');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (235, 'Double Clout Variant 235');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (236, 'WA60/1440 Variant 236');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (237, 'WA 18 (Indoor) Variant 237');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (238, 'Darwin Variant 238');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (239, 'Albion Variant 239');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (240, 'Long Perth Variant 240');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (241, 'WA 25 (Indoor) Variant 241');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (242, 'Windsor Variant 242');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (243, 'Long Hobart Variant 243');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (244, 'WA 25 (Indoor) Variant 244');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (245, 'Long Brisbane Variant 245');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (246, 'Junior WA 70 Variant 246');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (247, 'Bray I Variant 247');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (248, 'Long Hobart Variant 248');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (249, 'Long Melbourne Variant 249');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (250, 'Adelaide Variant 250');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (251, 'Junior WA 70 Variant 251');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (252, 'Windsor Variant 252');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (253, 'Long Sydney Variant 253');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (254, 'AA50/1440 Variant 254');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (255, 'Bray II Variant 255');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (256, 'Short Melbourne Variant 256');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (257, 'WA 18 (Indoor) Variant 257');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (258, 'Double Clout Variant 258');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (259, 'WA60/1440 Variant 259');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (260, 'Bray I Variant 260');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (261, 'Short Perth Variant 261');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (262, 'Long Melbourne Variant 262');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (263, 'National Variant 263');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (264, 'Junior WA 60 Variant 264');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (265, 'Long Brisbane Variant 265');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (266, 'Cairns Variant 266');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (267, 'WA900 Variant 267');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (268, 'Western Variant 268');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (269, 'Bray II Variant 269');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (270, 'Cairns Variant 270');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (271, 'Long Perth Variant 271');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (272, 'Western Variant 272');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (273, 'WA90/1440 Variant 273');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (274, 'WA90/1440 Variant 274');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (275, 'National Variant 275');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (276, 'Short Brisbane Variant 276');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (277, 'Canberra Variant 277');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (278, 'Short Windsor Variant 278');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (279, 'WA720 Compound Variant 279');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (280, 'Long Perth Variant 280');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (281, 'Darwin Variant 281');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (282, 'Albion Variant 282');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (283, 'Long Adelaide Variant 283');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (284, 'Long Brisbane Variant 284');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (285, 'Single Clout Variant 285');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (286, 'Long Adelaide Variant 286');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (287, 'Short Adelaide Variant 287');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (288, 'Long Hobart Variant 288');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (289, 'WA 18 (Indoor) Variant 289');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (290, 'Albion Variant 290');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (291, 'Perth Variant 291');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (292, 'Darwin Variant 292');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (293, 'Long Brisbane Variant 293');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (294, 'WA 25 (Indoor) Variant 294');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (295, 'Short Melbourne Variant 295');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (296, 'Short Brisbane Variant 296');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (297, 'Melbourne Variant 297');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (298, 'Western Variant 298');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (299, 'Junior WA 70 Variant 299');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (300, 'Darwin Variant 300');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (301, 'Darwin Variant 301');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (302, 'Long Melbourne Variant 302');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (303, 'Long Hobart Variant 303');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (304, 'Townsville Variant 304');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (305, 'Long Brisbane Variant 305');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (306, 'Windsor Variant 306');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (307, 'Long Sydney Variant 307');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (308, 'Windsor Variant 308');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (309, 'National Variant 309');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (310, 'Adelaide Variant 310');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (311, 'WA720 Compound Variant 311');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (312, 'New Western Variant 312');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (313, 'Long Hobart Variant 313');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (314, 'Short Adelaide Variant 314');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (315, 'Single Clout Variant 315');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (316, 'Short Melbourne Variant 316');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (317, 'Canberra Variant 317');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (318, 'Brisbane Variant 318');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (319, 'Sydney Variant 319');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (320, 'New National Variant 320');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (321, 'Sydney Variant 321');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (322, 'WA 18 (Indoor) Variant 322');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (323, 'WA90/1440 Variant 323');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (324, 'Long Brisbane Variant 324');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (325, 'Melbourne Variant 325');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (326, 'WA 25 (Indoor) Variant 326');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (327, 'Long Sydney Variant 327');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (328, 'York Variant 328');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (329, 'Bray II Variant 329');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (330, 'Double Clout Variant 330');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (331, 'New Western Variant 331');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (332, 'Long Perth Variant 332');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (333, 'WA 25 (Indoor) Variant 333');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (334, 'Short Hobart Variant 334');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (335, 'Long Adelaide Variant 335');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (336, 'Single Clout Variant 336');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (337, 'Windsor Variant 337');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (338, 'AA50/1440 Variant 338');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (339, 'Long Melbourne Variant 339');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (340, 'WA720 Compound Variant 340');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (341, 'Western Variant 341');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (342, 'Short Sydney Variant 342');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (343, 'AA50/1440 Variant 343');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (344, 'Short Brisbane Variant 344');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (345, 'Long Adelaide Variant 345');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (346, 'WA 18 (Indoor) Variant 346');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (347, 'York Variant 347');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (348, 'WA720 Compound Variant 348');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (349, 'Townsville Variant 349');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (350, 'New National Variant 350');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (351, 'Perth Variant 351');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (352, 'Long Adelaide Variant 352');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (353, 'Darwin Variant 353');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (354, 'Darwin Variant 354');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (355, 'Single Clout Variant 355');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (356, 'Single Clout Variant 356');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (357, 'Long Adelaide Variant 357');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (358, 'Short Perth Variant 358');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (359, 'WA70/1440 Variant 359');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (360, 'Melbourne Variant 360');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (361, 'WA900 Variant 361');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (362, 'Short Perth Variant 362');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (363, 'National Variant 363');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (364, 'Long Windsor Variant 364');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (365, 'Brisbane Variant 365');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (366, 'Windsor Variant 366');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (367, 'Windsor Variant 367');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (368, 'Hereford Variant 368');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (369, 'Hereford Variant 369');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (370, 'Double Clout Variant 370');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (371, 'Long Brisbane Variant 371');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (372, 'Junior WA 60 Variant 372');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (373, 'Hobart Variant 373');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (374, 'Short Perth Variant 374');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (375, 'Long Perth Variant 375');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (376, 'National Variant 376');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (377, 'Bray I Variant 377');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (378, 'WA 25 (Indoor) Variant 378');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (379, 'Junior WA 60 Variant 379');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (380, 'New National Variant 380');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (381, 'Townsville Variant 381');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (382, 'WA720 Recurve Variant 382');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (383, 'Canberra Variant 383');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (384, 'Albion Variant 384');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (385, 'Hobart Variant 385');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (386, 'Cairns Variant 386');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (387, 'York Variant 387');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (388, 'Sydney Variant 388');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (389, 'Short Sydney Variant 389');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (390, 'York Variant 390');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (391, 'Perth Variant 391');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (392, 'Melbourne Variant 392');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (393, 'York Variant 393');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (394, 'Albion Variant 394');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (395, 'Windsor Variant 395');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (396, 'Long Melbourne Variant 396');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (397, 'AA40/1440 Variant 397');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (398, 'WA720 Recurve Variant 398');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (399, 'Short Sydney Variant 399');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (400, 'Perth Variant 400');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (401, 'Adelaide Variant 401');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (402, 'Long Perth Variant 402');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (403, 'Long Perth Variant 403');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (404, 'Hereford Variant 404');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (405, 'Hobart Variant 405');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (406, 'Eastern Variant 406');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (407, 'Long Hobart Variant 407');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (408, 'Long Windsor Variant 408');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (409, 'Hereford Variant 409');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (410, 'Long Melbourne Variant 410');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (411, 'Long Hobart Variant 411');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (412, 'Townsville Variant 412');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (413, 'Junior WA 60 Variant 413');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (414, 'Darwin Variant 414');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (415, 'New National Variant 415');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (416, 'Short Windsor Variant 416');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (417, 'Bray II Variant 417');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (418, 'Townsville Variant 418');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (419, 'Melbourne Variant 419');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (420, 'Short Sydney Variant 420');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (421, 'Long Brisbane Variant 421');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (422, 'WA70/1440 Variant 422');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (423, 'Long Sydney Variant 423');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (424, 'New Western Variant 424');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (425, 'Short Adelaide Variant 425');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (426, 'St Nicholas Variant 426');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (427, 'Long Adelaide Variant 427');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (428, 'New National Variant 428');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (429, 'Western Variant 429');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (430, 'New National Variant 430');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (431, 'WA720 Recurve Variant 431');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (432, 'Short Brisbane Variant 432');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (433, 'Short Sydney Variant 433');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (434, 'Long Melbourne Variant 434');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (435, 'WA720 Compound Variant 435');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (436, 'WA720 Compound Variant 436');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (437, 'AA40/1440 Variant 437');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (438, 'WA 18 (Indoor) Variant 438');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (439, 'Single Clout Variant 439');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (440, 'AA50/1440 Variant 440');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (441, 'WA70/1440 Variant 441');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (442, 'Junior WA 60 Variant 442');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (443, 'Long Melbourne Variant 443');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (444, 'Bray II Variant 444');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (445, 'Junior WA 70 Variant 445');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (446, 'WA720 Recurve Variant 446');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (447, 'WA720 Compound Variant 447');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (448, 'Long Adelaide Variant 448');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (449, 'Albion Variant 449');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (450, 'Sydney Variant 450');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (451, 'WA720 Recurve Variant 451');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (452, 'Hereford Variant 452');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (453, 'Canberra Variant 453');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (454, 'Short Hobart Variant 454');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (455, 'Adelaide Variant 455');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (456, 'Short Adelaide Variant 456');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (457, 'New National Variant 457');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (458, 'Hobart Variant 458');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (459, 'Townsville Variant 459');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (460, 'York Variant 460');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (461, 'Long Sydney Variant 461');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (462, 'Long Sydney Variant 462');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (463, 'Bray II Variant 463');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (464, 'Short Sydney Variant 464');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (465, 'WA70/1440 Variant 465');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (466, 'WA60/1440 Variant 466');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (467, 'St Nicholas Variant 467');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (468, 'Short Perth Variant 468');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (469, 'Long Perth Variant 469');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (470, 'WA 18 (Indoor) Variant 470');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (471, 'Cairns Variant 471');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (472, 'Double Clout Variant 472');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (473, 'Long Hobart Variant 473');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (474, 'Single Clout Variant 474');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (475, 'Townsville Variant 475');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (476, 'Long Sydney Variant 476');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (477, 'Western Variant 477');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (478, 'Double Clout Variant 478');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (479, 'Long Brisbane Variant 479');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (480, 'Short Windsor Variant 480');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (481, 'Long Windsor Variant 481');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (482, 'Cairns Variant 482');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (483, 'York Variant 483');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (484, 'New National Variant 484');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (485, 'York Variant 485');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (486, 'Windsor Variant 486');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (487, 'Short Melbourne Variant 487');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (488, 'Bray II Variant 488');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (489, 'York Variant 489');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (490, 'York Variant 490');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (491, 'Double Clout Variant 491');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (492, 'Short Hobart Variant 492');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (493, 'Short Perth Variant 493');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (494, 'WA 18 (Indoor) Variant 494');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (495, 'Double Clout Variant 495');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (496, 'Adelaide Variant 496');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (497, 'WA720 Recurve Variant 497');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (498, 'Townsville Variant 498');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (499, 'Short Hobart Variant 499');
INSERT INTO BaseRound (BaseRoundID, RoundName) VALUES (500, 'Darwin Variant 500');"""

insert_statements.extend(sql_data.strip().splitlines())

# ── Write output ───────────────────────────────────────────────────────────────
output_path = "baseround_inserts.sql"
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
