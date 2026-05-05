"""
Archery Score Recording Database — Club table
Generates and downloads club_inserts.sql with 500 INSERT statements.
Run in Google Colab: the file will be saved and automatically downloaded.
"""

import random

# ── Data pools ─────────────────────────────────────────────────────────────────
australian_cities = [
    "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Hobart",
    "Darwin", "Canberra", "Newcastle", "Wollongong", "Geelong", "Townsville",
    "Cairns", "Toowoomba", "Ballarat", "Bendigo", "Launceston", "Mackay",
    "Rockhampton", "Bunbury", "Bundaberg", "Hervey Bay", "Wagga Wagga",
    "Coffs Harbour", "Shepparton", "Albury", "Port Macquarie", "Tamworth",
    "Orange", "Dubbo", "Bathurst", "Nowra", "Lismore", "Mildura",
    "Warrnambool", "Sale", "Horsham", "Swan Hill", "Echuca", "Sunbury",
    "Cranbourne", "Frankston", "Dandenong", "Ringwood", "Doncaster",
    "Box Hill", "Burwood", "Camberwell", "Hawthorn", "Geelong",
]

club_suffixes = [
    "Archery Club", "Archers", "Bowmen",
    "Archery Association", "Target Archery Club", "Field Archers",
]

def escape_sql(value):
    return str(value).replace("'", "''")

# ── Pre-generated INSERT statements ───────────────────────────────────────────
insert_statements = []
insert_statements.append("-- INSERT statements for the Club table")
insert_statements.append("-- 500 rows")
insert_statements.append("")

sql_data = """\
INSERT INTO Club (ClubID, Name) VALUES (1, 'Cranbourne Archery Club 1');
INSERT INTO Club (ClubID, Name) VALUES (2, 'Melbourne Field Archers 2');
INSERT INTO Club (ClubID, Name) VALUES (3, 'Mackay Archers 3');
INSERT INTO Club (ClubID, Name) VALUES (4, 'Ballarat Archers 4');
INSERT INTO Club (ClubID, Name) VALUES (5, 'Camberwell Archery Club 5');
INSERT INTO Club (ClubID, Name) VALUES (6, 'Ringwood Field Archers 6');
INSERT INTO Club (ClubID, Name) VALUES (7, 'Warrnambool Archery Club 7');
INSERT INTO Club (ClubID, Name) VALUES (8, 'Swan Hill Archery Association 8');
INSERT INTO Club (ClubID, Name) VALUES (9, 'Brisbane Archery Club 9');
INSERT INTO Club (ClubID, Name) VALUES (10, 'Hobart Archers 10');
INSERT INTO Club (ClubID, Name) VALUES (11, 'Ballarat Target Archery Club 11');
INSERT INTO Club (ClubID, Name) VALUES (12, 'Echuca Archery Club 12');
INSERT INTO Club (ClubID, Name) VALUES (13, 'Sale Archers 13');
INSERT INTO Club (ClubID, Name) VALUES (14, 'Box Hill Field Archers 14');
INSERT INTO Club (ClubID, Name) VALUES (15, 'Doncaster Target Archery Club 15');
INSERT INTO Club (ClubID, Name) VALUES (16, 'Port Macquarie Archers 16');
INSERT INTO Club (ClubID, Name) VALUES (17, 'Orange Target Archery Club 17');
INSERT INTO Club (ClubID, Name) VALUES (18, 'Mackay Archery Club 18');
INSERT INTO Club (ClubID, Name) VALUES (19, 'Hawthorn Archers 19');
INSERT INTO Club (ClubID, Name) VALUES (20, 'Doncaster Archery Association 20');
INSERT INTO Club (ClubID, Name) VALUES (21, 'Hervey Bay Bowmen 21');
INSERT INTO Club (ClubID, Name) VALUES (22, 'Wollongong Archers 22');
INSERT INTO Club (ClubID, Name) VALUES (23, 'Hawthorn Bowmen 23');
INSERT INTO Club (ClubID, Name) VALUES (24, 'Darwin Archery Club 24');
INSERT INTO Club (ClubID, Name) VALUES (25, 'Shepparton Archery Club 25');
INSERT INTO Club (ClubID, Name) VALUES (26, 'Wagga Wagga Bowmen 26');
INSERT INTO Club (ClubID, Name) VALUES (27, 'Echuca Bowmen 27');
INSERT INTO Club (ClubID, Name) VALUES (28, 'Brisbane Field Archers 28');
INSERT INTO Club (ClubID, Name) VALUES (29, 'Dubbo Target Archery Club 29');
INSERT INTO Club (ClubID, Name) VALUES (30, 'Canberra Archery Association 30');
INSERT INTO Club (ClubID, Name) VALUES (31, 'Hobart Target Archery Club 31');
INSERT INTO Club (ClubID, Name) VALUES (32, 'Rockhampton Field Archers 32');
INSERT INTO Club (ClubID, Name) VALUES (33, 'Sunbury Bowmen 33');
INSERT INTO Club (ClubID, Name) VALUES (34, 'Horsham Archers 34');
INSERT INTO Club (ClubID, Name) VALUES (35, 'Box Hill Archery Club 35');
INSERT INTO Club (ClubID, Name) VALUES (36, 'Brisbane Field Archers 36');
INSERT INTO Club (ClubID, Name) VALUES (37, 'Ballarat Bowmen 37');
INSERT INTO Club (ClubID, Name) VALUES (38, 'Hobart Archers 38');
INSERT INTO Club (ClubID, Name) VALUES (39, 'Darwin Archery Association 39');
INSERT INTO Club (ClubID, Name) VALUES (40, 'Mackay Archery Association 40');
INSERT INTO Club (ClubID, Name) VALUES (41, 'Cranbourne Bowmen 41');
INSERT INTO Club (ClubID, Name) VALUES (42, 'Geelong Bowmen 42');
INSERT INTO Club (ClubID, Name) VALUES (43, 'Wagga Wagga Archers 43');
INSERT INTO Club (ClubID, Name) VALUES (44, 'Dandenong Bowmen 44');
INSERT INTO Club (ClubID, Name) VALUES (45, 'Doncaster Field Archers 45');
INSERT INTO Club (ClubID, Name) VALUES (46, 'Frankston Archery Club 46');
INSERT INTO Club (ClubID, Name) VALUES (47, 'Echuca Field Archers 47');
INSERT INTO Club (ClubID, Name) VALUES (48, 'Geelong Target Archery Club 48');
INSERT INTO Club (ClubID, Name) VALUES (49, 'Burwood Archers 49');
INSERT INTO Club (ClubID, Name) VALUES (50, 'Geelong Archery Association 50');
INSERT INTO Club (ClubID, Name) VALUES (51, 'Shepparton Bowmen 51');
INSERT INTO Club (ClubID, Name) VALUES (52, 'Cranbourne Field Archers 52');
INSERT INTO Club (ClubID, Name) VALUES (53, 'Sale Archers 53');
INSERT INTO Club (ClubID, Name) VALUES (54, 'Ringwood Bowmen 54');
INSERT INTO Club (ClubID, Name) VALUES (55, 'Geelong Archery Club 55');
INSERT INTO Club (ClubID, Name) VALUES (56, 'Ballarat Archery Club 56');
INSERT INTO Club (ClubID, Name) VALUES (57, 'Bundaberg Archery Association 57');
INSERT INTO Club (ClubID, Name) VALUES (58, 'Mackay Archery Club 58');
INSERT INTO Club (ClubID, Name) VALUES (59, 'Toowoomba Target Archery Club 59');
INSERT INTO Club (ClubID, Name) VALUES (60, 'Box Hill Bowmen 60');
INSERT INTO Club (ClubID, Name) VALUES (61, 'Toowoomba Field Archers 61');
INSERT INTO Club (ClubID, Name) VALUES (62, 'Nowra Archery Association 62');
INSERT INTO Club (ClubID, Name) VALUES (63, 'Frankston Archery Association 63');
INSERT INTO Club (ClubID, Name) VALUES (64, 'Wollongong Bowmen 64');
INSERT INTO Club (ClubID, Name) VALUES (65, 'Newcastle Archers 65');
INSERT INTO Club (ClubID, Name) VALUES (66, 'Camberwell Target Archery Club 66');
INSERT INTO Club (ClubID, Name) VALUES (67, 'Warrnambool Bowmen 67');
INSERT INTO Club (ClubID, Name) VALUES (68, 'Camberwell Target Archery Club 68');
INSERT INTO Club (ClubID, Name) VALUES (69, 'Tamworth Target Archery Club 69');
INSERT INTO Club (ClubID, Name) VALUES (70, 'Albury Bowmen 70');
INSERT INTO Club (ClubID, Name) VALUES (71, 'Ballarat Archers 71');
INSERT INTO Club (ClubID, Name) VALUES (72, 'Lismore Archery Association 72');
INSERT INTO Club (ClubID, Name) VALUES (73, 'Hobart Archery Club 73');
INSERT INTO Club (ClubID, Name) VALUES (74, 'Canberra Archers 74');
INSERT INTO Club (ClubID, Name) VALUES (75, 'Cranbourne Archers 75');
INSERT INTO Club (ClubID, Name) VALUES (76, 'Ringwood Archery Association 76');
INSERT INTO Club (ClubID, Name) VALUES (77, 'Echuca Archery Club 77');
INSERT INTO Club (ClubID, Name) VALUES (78, 'Shepparton Archery Association 78');
INSERT INTO Club (ClubID, Name) VALUES (79, 'Echuca Archery Association 79');
INSERT INTO Club (ClubID, Name) VALUES (80, 'Mildura Bowmen 80');
INSERT INTO Club (ClubID, Name) VALUES (81, 'Sale Archery Club 81');
INSERT INTO Club (ClubID, Name) VALUES (82, 'Ringwood Field Archers 82');
INSERT INTO Club (ClubID, Name) VALUES (83, 'Canberra Field Archers 83');
INSERT INTO Club (ClubID, Name) VALUES (84, 'Warrnambool Bowmen 84');
INSERT INTO Club (ClubID, Name) VALUES (85, 'Geelong Field Archers 85');
INSERT INTO Club (ClubID, Name) VALUES (86, 'Hervey Bay Archery Club 86');
INSERT INTO Club (ClubID, Name) VALUES (87, 'Rockhampton Archery Association 87');
INSERT INTO Club (ClubID, Name) VALUES (88, 'Geelong Archery Association 88');
INSERT INTO Club (ClubID, Name) VALUES (89, 'Sydney Field Archers 89');
INSERT INTO Club (ClubID, Name) VALUES (90, 'Burwood Bowmen 90');
INSERT INTO Club (ClubID, Name) VALUES (91, 'Lismore Archers 91');
INSERT INTO Club (ClubID, Name) VALUES (92, 'Lismore Archery Club 92');
INSERT INTO Club (ClubID, Name) VALUES (93, 'Cranbourne Bowmen 93');
INSERT INTO Club (ClubID, Name) VALUES (94, 'Cranbourne Target Archery Club 94');
INSERT INTO Club (ClubID, Name) VALUES (95, 'Echuca Archers 95');
INSERT INTO Club (ClubID, Name) VALUES (96, 'Wollongong Bowmen 96');
INSERT INTO Club (ClubID, Name) VALUES (97, 'Hawthorn Archers 97');
INSERT INTO Club (ClubID, Name) VALUES (98, 'Warrnambool Target Archery Club 98');
INSERT INTO Club (ClubID, Name) VALUES (99, 'Sydney Target Archery Club 99');
INSERT INTO Club (ClubID, Name) VALUES (100, 'Bundaberg Archery Association 100');
INSERT INTO Club (ClubID, Name) VALUES (101, 'Melbourne Archery Club 101');
INSERT INTO Club (ClubID, Name) VALUES (102, 'Coffs Harbour Bowmen 102');
INSERT INTO Club (ClubID, Name) VALUES (103, 'Bendigo Archery Club 103');
INSERT INTO Club (ClubID, Name) VALUES (104, 'Bendigo Target Archery Club 104');
INSERT INTO Club (ClubID, Name) VALUES (105, 'Hobart Archery Club 105');
INSERT INTO Club (ClubID, Name) VALUES (106, 'Burwood Archery Association 106');
INSERT INTO Club (ClubID, Name) VALUES (107, 'Adelaide Target Archery Club 107');
INSERT INTO Club (ClubID, Name) VALUES (108, 'Geelong Archers 108');
INSERT INTO Club (ClubID, Name) VALUES (109, 'Newcastle Field Archers 109');
INSERT INTO Club (ClubID, Name) VALUES (110, 'Bathurst Target Archery Club 110');
INSERT INTO Club (ClubID, Name) VALUES (111, 'Geelong Bowmen 111');
INSERT INTO Club (ClubID, Name) VALUES (112, 'Mildura Target Archery Club 112');
INSERT INTO Club (ClubID, Name) VALUES (113, 'Tamworth Archers 113');
INSERT INTO Club (ClubID, Name) VALUES (114, 'Warrnambool Field Archers 114');
INSERT INTO Club (ClubID, Name) VALUES (115, 'Doncaster Archers 115');
INSERT INTO Club (ClubID, Name) VALUES (116, 'Box Hill Bowmen 116');
INSERT INTO Club (ClubID, Name) VALUES (117, 'Albury Field Archers 117');
INSERT INTO Club (ClubID, Name) VALUES (118, 'Frankston Bowmen 118');
INSERT INTO Club (ClubID, Name) VALUES (119, 'Orange Target Archery Club 119');
INSERT INTO Club (ClubID, Name) VALUES (120, 'Orange Archery Club 120');
INSERT INTO Club (ClubID, Name) VALUES (121, 'Bendigo Archers 121');
INSERT INTO Club (ClubID, Name) VALUES (122, 'Adelaide Bowmen 122');
INSERT INTO Club (ClubID, Name) VALUES (123, 'Melbourne Target Archery Club 123');
INSERT INTO Club (ClubID, Name) VALUES (124, 'Sale Archers 124');
INSERT INTO Club (ClubID, Name) VALUES (125, 'Swan Hill Archers 125');
INSERT INTO Club (ClubID, Name) VALUES (126, 'Sydney Archery Club 126');
INSERT INTO Club (ClubID, Name) VALUES (127, 'Box Hill Field Archers 127');
INSERT INTO Club (ClubID, Name) VALUES (128, 'Perth Archers 128');
INSERT INTO Club (ClubID, Name) VALUES (129, 'Adelaide Archery Club 129');
INSERT INTO Club (ClubID, Name) VALUES (130, 'Hervey Bay Archery Club 130');
INSERT INTO Club (ClubID, Name) VALUES (131, 'Lismore Archers 131');
INSERT INTO Club (ClubID, Name) VALUES (132, 'Mackay Field Archers 132');
INSERT INTO Club (ClubID, Name) VALUES (133, 'Nowra Archers 133');
INSERT INTO Club (ClubID, Name) VALUES (134, 'Warrnambool Archers 134');
INSERT INTO Club (ClubID, Name) VALUES (135, 'Burwood Target Archery Club 135');
INSERT INTO Club (ClubID, Name) VALUES (136, 'Horsham Archery Association 136');
INSERT INTO Club (ClubID, Name) VALUES (137, 'Bendigo Archery Association 137');
INSERT INTO Club (ClubID, Name) VALUES (138, 'Port Macquarie Archers 138');
INSERT INTO Club (ClubID, Name) VALUES (139, 'Darwin Archery Club 139');
INSERT INTO Club (ClubID, Name) VALUES (140, 'Dandenong Archery Association 140');
INSERT INTO Club (ClubID, Name) VALUES (141, 'Wagga Wagga Archery Association 141');
INSERT INTO Club (ClubID, Name) VALUES (142, 'Port Macquarie Archery Association 142');
INSERT INTO Club (ClubID, Name) VALUES (143, 'Burwood Archery Club 143');
INSERT INTO Club (ClubID, Name) VALUES (144, 'Ringwood Field Archers 144');
INSERT INTO Club (ClubID, Name) VALUES (145, 'Frankston Archery Club 145');
INSERT INTO Club (ClubID, Name) VALUES (146, 'Perth Archery Association 146');
INSERT INTO Club (ClubID, Name) VALUES (147, 'Burwood Bowmen 147');
INSERT INTO Club (ClubID, Name) VALUES (148, 'Darwin Archers 148');
INSERT INTO Club (ClubID, Name) VALUES (149, 'Cairns Archers 149');
INSERT INTO Club (ClubID, Name) VALUES (150, 'Warrnambool Archery Association 150');
INSERT INTO Club (ClubID, Name) VALUES (151, 'Newcastle Archery Association 151');
INSERT INTO Club (ClubID, Name) VALUES (152, 'Townsville Bowmen 152');
INSERT INTO Club (ClubID, Name) VALUES (153, 'Dubbo Archers 153');
INSERT INTO Club (ClubID, Name) VALUES (154, 'Adelaide Archery Association 154');
INSERT INTO Club (ClubID, Name) VALUES (155, 'Sale Archery Club 155');
INSERT INTO Club (ClubID, Name) VALUES (156, 'Perth Field Archers 156');
INSERT INTO Club (ClubID, Name) VALUES (157, 'Warrnambool Archery Club 157');
INSERT INTO Club (ClubID, Name) VALUES (158, 'Hobart Archers 158');
INSERT INTO Club (ClubID, Name) VALUES (159, 'Geelong Archery Association 159');
INSERT INTO Club (ClubID, Name) VALUES (160, 'Nowra Archery Association 160');
INSERT INTO Club (ClubID, Name) VALUES (161, 'Toowoomba Archery Association 161');
INSERT INTO Club (ClubID, Name) VALUES (162, 'Perth Archers 162');
INSERT INTO Club (ClubID, Name) VALUES (163, 'Shepparton Archery Club 163');
INSERT INTO Club (ClubID, Name) VALUES (164, 'Shepparton Bowmen 164');
INSERT INTO Club (ClubID, Name) VALUES (165, 'Dubbo Bowmen 165');
INSERT INTO Club (ClubID, Name) VALUES (166, 'Tamworth Field Archers 166');
INSERT INTO Club (ClubID, Name) VALUES (167, 'Burwood Target Archery Club 167');
INSERT INTO Club (ClubID, Name) VALUES (168, 'Dandenong Field Archers 168');
INSERT INTO Club (ClubID, Name) VALUES (169, 'Nowra Archers 169');
INSERT INTO Club (ClubID, Name) VALUES (170, 'Cairns Bowmen 170');
INSERT INTO Club (ClubID, Name) VALUES (171, 'Toowoomba Archery Club 171');
INSERT INTO Club (ClubID, Name) VALUES (172, 'Swan Hill Field Archers 172');
INSERT INTO Club (ClubID, Name) VALUES (173, 'Warrnambool Archery Club 173');
INSERT INTO Club (ClubID, Name) VALUES (174, 'Camberwell Bowmen 174');
INSERT INTO Club (ClubID, Name) VALUES (175, 'Perth Archery Club 175');
INSERT INTO Club (ClubID, Name) VALUES (176, 'Swan Hill Archery Association 176');
INSERT INTO Club (ClubID, Name) VALUES (177, 'Lismore Target Archery Club 177');
INSERT INTO Club (ClubID, Name) VALUES (178, 'Geelong Archery Club 178');
INSERT INTO Club (ClubID, Name) VALUES (179, 'Lismore Archery Club 179');
INSERT INTO Club (ClubID, Name) VALUES (180, 'Townsville Archery Club 180');
INSERT INTO Club (ClubID, Name) VALUES (181, 'Echuca Archery Club 181');
INSERT INTO Club (ClubID, Name) VALUES (182, 'Ringwood Archers 182');
INSERT INTO Club (ClubID, Name) VALUES (183, 'Albury Archery Club 183');
INSERT INTO Club (ClubID, Name) VALUES (184, 'Horsham Archers 184');
INSERT INTO Club (ClubID, Name) VALUES (185, 'Swan Hill Target Archery Club 185');
INSERT INTO Club (ClubID, Name) VALUES (186, 'Brisbane Target Archery Club 186');
INSERT INTO Club (ClubID, Name) VALUES (187, 'Hobart Archery Association 187');
INSERT INTO Club (ClubID, Name) VALUES (188, 'Dandenong Target Archery Club 188');
INSERT INTO Club (ClubID, Name) VALUES (189, 'Horsham Target Archery Club 189');
INSERT INTO Club (ClubID, Name) VALUES (190, 'Bundaberg Bowmen 190');
INSERT INTO Club (ClubID, Name) VALUES (191, 'Toowoomba Field Archers 191');
INSERT INTO Club (ClubID, Name) VALUES (192, 'Box Hill Bowmen 192');
INSERT INTO Club (ClubID, Name) VALUES (193, 'Bendigo Bowmen 193');
INSERT INTO Club (ClubID, Name) VALUES (194, 'Albury Archers 194');
INSERT INTO Club (ClubID, Name) VALUES (195, 'Dandenong Field Archers 195');
INSERT INTO Club (ClubID, Name) VALUES (196, 'Bunbury Archery Association 196');
INSERT INTO Club (ClubID, Name) VALUES (197, 'Bundaberg Archery Club 197');
INSERT INTO Club (ClubID, Name) VALUES (198, 'Sydney Archery Association 198');
INSERT INTO Club (ClubID, Name) VALUES (199, 'Sunbury Target Archery Club 199');
INSERT INTO Club (ClubID, Name) VALUES (200, 'Darwin Archery Club 200');
INSERT INTO Club (ClubID, Name) VALUES (201, 'Warrnambool Archers 201');
INSERT INTO Club (ClubID, Name) VALUES (202, 'Lismore Bowmen 202');
INSERT INTO Club (ClubID, Name) VALUES (203, 'Newcastle Bowmen 203');
INSERT INTO Club (ClubID, Name) VALUES (204, 'Adelaide Archers 204');
INSERT INTO Club (ClubID, Name) VALUES (205, 'Coffs Harbour Bowmen 205');
INSERT INTO Club (ClubID, Name) VALUES (206, 'Geelong Archery Association 206');
INSERT INTO Club (ClubID, Name) VALUES (207, 'Warrnambool Field Archers 207');
INSERT INTO Club (ClubID, Name) VALUES (208, 'Bunbury Target Archery Club 208');
INSERT INTO Club (ClubID, Name) VALUES (209, 'Frankston Target Archery Club 209');
INSERT INTO Club (ClubID, Name) VALUES (210, 'Sydney Field Archers 210');
INSERT INTO Club (ClubID, Name) VALUES (211, 'Sale Bowmen 211');
INSERT INTO Club (ClubID, Name) VALUES (212, 'Dandenong Archery Club 212');
INSERT INTO Club (ClubID, Name) VALUES (213, 'Newcastle Bowmen 213');
INSERT INTO Club (ClubID, Name) VALUES (214, 'Canberra Archery Club 214');
INSERT INTO Club (ClubID, Name) VALUES (215, 'Camberwell Target Archery Club 215');
INSERT INTO Club (ClubID, Name) VALUES (216, 'Wollongong Bowmen 216');
INSERT INTO Club (ClubID, Name) VALUES (217, 'Rockhampton Target Archery Club 217');
INSERT INTO Club (ClubID, Name) VALUES (218, 'Toowoomba Field Archers 218');
INSERT INTO Club (ClubID, Name) VALUES (219, 'Hervey Bay Archers 219');
INSERT INTO Club (ClubID, Name) VALUES (220, 'Ringwood Field Archers 220');
INSERT INTO Club (ClubID, Name) VALUES (221, 'Launceston Target Archery Club 221');
INSERT INTO Club (ClubID, Name) VALUES (222, 'Nowra Bowmen 222');
INSERT INTO Club (ClubID, Name) VALUES (223, 'Perth Archery Club 223');
INSERT INTO Club (ClubID, Name) VALUES (224, 'Cranbourne Archery Association 224');
INSERT INTO Club (ClubID, Name) VALUES (225, 'Mackay Archery Club 225');
INSERT INTO Club (ClubID, Name) VALUES (226, 'Sydney Bowmen 226');
INSERT INTO Club (ClubID, Name) VALUES (227, 'Geelong Archers 227');
INSERT INTO Club (ClubID, Name) VALUES (228, 'Cranbourne Bowmen 228');
INSERT INTO Club (ClubID, Name) VALUES (229, 'Geelong Field Archers 229');
INSERT INTO Club (ClubID, Name) VALUES (230, 'Orange Target Archery Club 230');
INSERT INTO Club (ClubID, Name) VALUES (231, 'Box Hill Archery Association 231');
INSERT INTO Club (ClubID, Name) VALUES (232, 'Sale Archery Club 232');
INSERT INTO Club (ClubID, Name) VALUES (233, 'Canberra Archery Club 233');
INSERT INTO Club (ClubID, Name) VALUES (234, 'Doncaster Archers 234');
INSERT INTO Club (ClubID, Name) VALUES (235, 'Warrnambool Archery Club 235');
INSERT INTO Club (ClubID, Name) VALUES (236, 'Coffs Harbour Target Archery Club 236');
INSERT INTO Club (ClubID, Name) VALUES (237, 'Sale Archers 237');
INSERT INTO Club (ClubID, Name) VALUES (238, 'Tamworth Archers 238');
INSERT INTO Club (ClubID, Name) VALUES (239, 'Brisbane Bowmen 239');
INSERT INTO Club (ClubID, Name) VALUES (240, 'Coffs Harbour Archery Club 240');
INSERT INTO Club (ClubID, Name) VALUES (241, 'Wagga Wagga Archers 241');
INSERT INTO Club (ClubID, Name) VALUES (242, 'Ringwood Archers 242');
INSERT INTO Club (ClubID, Name) VALUES (243, 'Dandenong Archery Club 243');
INSERT INTO Club (ClubID, Name) VALUES (244, 'Wagga Wagga Target Archery Club 244');
INSERT INTO Club (ClubID, Name) VALUES (245, 'Port Macquarie Target Archery Club 245');
INSERT INTO Club (ClubID, Name) VALUES (246, 'Camberwell Archers 246');
INSERT INTO Club (ClubID, Name) VALUES (247, 'Bendigo Archers 247');
INSERT INTO Club (ClubID, Name) VALUES (248, 'Townsville Archery Association 248');
INSERT INTO Club (ClubID, Name) VALUES (249, 'Melbourne Archers 249');
INSERT INTO Club (ClubID, Name) VALUES (250, 'Camberwell Bowmen 250');
INSERT INTO Club (ClubID, Name) VALUES (251, 'Port Macquarie Field Archers 251');
INSERT INTO Club (ClubID, Name) VALUES (252, 'Camberwell Archers 252');
INSERT INTO Club (ClubID, Name) VALUES (253, 'Mackay Archers 253');
INSERT INTO Club (ClubID, Name) VALUES (254, 'Doncaster Archery Club 254');
INSERT INTO Club (ClubID, Name) VALUES (255, 'Shepparton Archery Club 255');
INSERT INTO Club (ClubID, Name) VALUES (256, 'Bathurst Archers 256');
INSERT INTO Club (ClubID, Name) VALUES (257, 'Cairns Archery Association 257');
INSERT INTO Club (ClubID, Name) VALUES (258, 'Wagga Wagga Bowmen 258');
INSERT INTO Club (ClubID, Name) VALUES (259, 'Ballarat Archers 259');
INSERT INTO Club (ClubID, Name) VALUES (260, 'Melbourne Field Archers 260');
INSERT INTO Club (ClubID, Name) VALUES (261, 'Cairns Archery Association 261');
INSERT INTO Club (ClubID, Name) VALUES (262, 'Hervey Bay Bowmen 262');
INSERT INTO Club (ClubID, Name) VALUES (263, 'Adelaide Bowmen 263');
INSERT INTO Club (ClubID, Name) VALUES (264, 'Wagga Wagga Field Archers 264');
INSERT INTO Club (ClubID, Name) VALUES (265, 'Lismore Archery Association 265');
INSERT INTO Club (ClubID, Name) VALUES (266, 'Ringwood Target Archery Club 266');
INSERT INTO Club (ClubID, Name) VALUES (267, 'Hervey Bay Archery Club 267');
INSERT INTO Club (ClubID, Name) VALUES (268, 'Canberra Bowmen 268');
INSERT INTO Club (ClubID, Name) VALUES (269, 'Townsville Target Archery Club 269');
INSERT INTO Club (ClubID, Name) VALUES (270, 'Launceston Archery Club 270');
INSERT INTO Club (ClubID, Name) VALUES (271, 'Darwin Target Archery Club 271');
INSERT INTO Club (ClubID, Name) VALUES (272, 'Tamworth Bowmen 272');
INSERT INTO Club (ClubID, Name) VALUES (273, 'Burwood Bowmen 273');
INSERT INTO Club (ClubID, Name) VALUES (274, 'Tamworth Target Archery Club 274');
INSERT INTO Club (ClubID, Name) VALUES (275, 'Lismore Archery Club 275');
INSERT INTO Club (ClubID, Name) VALUES (276, 'Shepparton Target Archery Club 276');
INSERT INTO Club (ClubID, Name) VALUES (277, 'Cairns Bowmen 277');
INSERT INTO Club (ClubID, Name) VALUES (278, 'Brisbane Field Archers 278');
INSERT INTO Club (ClubID, Name) VALUES (279, 'Tamworth Archery Club 279');
INSERT INTO Club (ClubID, Name) VALUES (280, 'Mildura Target Archery Club 280');
INSERT INTO Club (ClubID, Name) VALUES (281, 'Ringwood Field Archers 281');
INSERT INTO Club (ClubID, Name) VALUES (282, 'Camberwell Field Archers 282');
INSERT INTO Club (ClubID, Name) VALUES (283, 'Dandenong Archers 283');
INSERT INTO Club (ClubID, Name) VALUES (284, 'Coffs Harbour Archery Association 284');
INSERT INTO Club (ClubID, Name) VALUES (285, 'Adelaide Field Archers 285');
INSERT INTO Club (ClubID, Name) VALUES (286, 'Hervey Bay Target Archery Club 286');
INSERT INTO Club (ClubID, Name) VALUES (287, 'Bundaberg Field Archers 287');
INSERT INTO Club (ClubID, Name) VALUES (288, 'Canberra Field Archers 288');
INSERT INTO Club (ClubID, Name) VALUES (289, 'Bunbury Target Archery Club 289');
INSERT INTO Club (ClubID, Name) VALUES (290, 'Bunbury Field Archers 290');
INSERT INTO Club (ClubID, Name) VALUES (291, 'Port Macquarie Bowmen 291');
INSERT INTO Club (ClubID, Name) VALUES (292, 'Albury Field Archers 292');
INSERT INTO Club (ClubID, Name) VALUES (293, 'Rockhampton Target Archery Club 293');
INSERT INTO Club (ClubID, Name) VALUES (294, 'Newcastle Archers 294');
INSERT INTO Club (ClubID, Name) VALUES (295, 'Port Macquarie Field Archers 295');
INSERT INTO Club (ClubID, Name) VALUES (296, 'Shepparton Field Archers 296');
INSERT INTO Club (ClubID, Name) VALUES (297, 'Camberwell Archers 297');
INSERT INTO Club (ClubID, Name) VALUES (298, 'Sunbury Target Archery Club 298');
INSERT INTO Club (ClubID, Name) VALUES (299, 'Bunbury Archery Association 299');
INSERT INTO Club (ClubID, Name) VALUES (300, 'Sale Archery Club 300');
INSERT INTO Club (ClubID, Name) VALUES (301, 'Bunbury Bowmen 301');
INSERT INTO Club (ClubID, Name) VALUES (302, 'Toowoomba Archery Association 302');
INSERT INTO Club (ClubID, Name) VALUES (303, 'Swan Hill Target Archery Club 303');
INSERT INTO Club (ClubID, Name) VALUES (304, 'Frankston Bowmen 304');
INSERT INTO Club (ClubID, Name) VALUES (305, 'Dubbo Archery Association 305');
INSERT INTO Club (ClubID, Name) VALUES (306, 'Orange Field Archers 306');
INSERT INTO Club (ClubID, Name) VALUES (307, 'Toowoomba Target Archery Club 307');
INSERT INTO Club (ClubID, Name) VALUES (308, 'Bathurst Field Archers 308');
INSERT INTO Club (ClubID, Name) VALUES (309, 'Geelong Field Archers 309');
INSERT INTO Club (ClubID, Name) VALUES (310, 'Hobart Bowmen 310');
INSERT INTO Club (ClubID, Name) VALUES (311, 'Lismore Field Archers 311');
INSERT INTO Club (ClubID, Name) VALUES (312, 'Cranbourne Target Archery Club 312');
INSERT INTO Club (ClubID, Name) VALUES (313, 'Hervey Bay Archery Club 313');
INSERT INTO Club (ClubID, Name) VALUES (314, 'Hawthorn Archers 314');
INSERT INTO Club (ClubID, Name) VALUES (315, 'Ringwood Bowmen 315');
INSERT INTO Club (ClubID, Name) VALUES (316, 'Ballarat Archers 316');
INSERT INTO Club (ClubID, Name) VALUES (317, 'Wollongong Archery Club 317');
INSERT INTO Club (ClubID, Name) VALUES (318, 'Brisbane Archers 318');
INSERT INTO Club (ClubID, Name) VALUES (319, 'Bathurst Target Archery Club 319');
INSERT INTO Club (ClubID, Name) VALUES (320, 'Geelong Archery Club 320');
INSERT INTO Club (ClubID, Name) VALUES (321, 'Dubbo Archery Association 321');
INSERT INTO Club (ClubID, Name) VALUES (322, 'Cranbourne Target Archery Club 322');
INSERT INTO Club (ClubID, Name) VALUES (323, 'Cairns Field Archers 323');
INSERT INTO Club (ClubID, Name) VALUES (324, 'Doncaster Archery Association 324');
INSERT INTO Club (ClubID, Name) VALUES (325, 'Nowra Archery Association 325');
INSERT INTO Club (ClubID, Name) VALUES (326, 'Bendigo Archers 326');
INSERT INTO Club (ClubID, Name) VALUES (327, 'Frankston Field Archers 327');
INSERT INTO Club (ClubID, Name) VALUES (328, 'Sydney Archery Club 328');
INSERT INTO Club (ClubID, Name) VALUES (329, 'Geelong Archery Association 329');
INSERT INTO Club (ClubID, Name) VALUES (330, 'Ballarat Archers 330');
INSERT INTO Club (ClubID, Name) VALUES (331, 'Doncaster Target Archery Club 331');
INSERT INTO Club (ClubID, Name) VALUES (332, 'Dubbo Archery Club 332');
INSERT INTO Club (ClubID, Name) VALUES (333, 'Sale Archers 333');
INSERT INTO Club (ClubID, Name) VALUES (334, 'Canberra Archery Association 334');
INSERT INTO Club (ClubID, Name) VALUES (335, 'Newcastle Archery Association 335');
INSERT INTO Club (ClubID, Name) VALUES (336, 'Dandenong Target Archery Club 336');
INSERT INTO Club (ClubID, Name) VALUES (337, 'Sale Target Archery Club 337');
INSERT INTO Club (ClubID, Name) VALUES (338, 'Bundaberg Archery Association 338');
INSERT INTO Club (ClubID, Name) VALUES (339, 'Sunbury Field Archers 339');
INSERT INTO Club (ClubID, Name) VALUES (340, 'Lismore Archery Association 340');
INSERT INTO Club (ClubID, Name) VALUES (341, 'Sale Archery Association 341');
INSERT INTO Club (ClubID, Name) VALUES (342, 'Geelong Field Archers 342');
INSERT INTO Club (ClubID, Name) VALUES (343, 'Bathurst Archery Association 343');
INSERT INTO Club (ClubID, Name) VALUES (344, 'Launceston Archers 344');
INSERT INTO Club (ClubID, Name) VALUES (345, 'Cranbourne Bowmen 345');
INSERT INTO Club (ClubID, Name) VALUES (346, 'Geelong Target Archery Club 346');
INSERT INTO Club (ClubID, Name) VALUES (347, 'Nowra Field Archers 347');
INSERT INTO Club (ClubID, Name) VALUES (348, 'Bendigo Bowmen 348');
INSERT INTO Club (ClubID, Name) VALUES (349, 'Orange Archery Club 349');
INSERT INTO Club (ClubID, Name) VALUES (350, 'Box Hill Bowmen 350');
INSERT INTO Club (ClubID, Name) VALUES (351, 'Bendigo Bowmen 351');
INSERT INTO Club (ClubID, Name) VALUES (352, 'Hervey Bay Bowmen 352');
INSERT INTO Club (ClubID, Name) VALUES (353, 'Warrnambool Archery Club 353');
INSERT INTO Club (ClubID, Name) VALUES (354, 'Newcastle Archers 354');
INSERT INTO Club (ClubID, Name) VALUES (355, 'Ballarat Archery Association 355');
INSERT INTO Club (ClubID, Name) VALUES (356, 'Doncaster Archers 356');
INSERT INTO Club (ClubID, Name) VALUES (357, 'Box Hill Archers 357');
INSERT INTO Club (ClubID, Name) VALUES (358, 'Adelaide Archery Association 358');
INSERT INTO Club (ClubID, Name) VALUES (359, 'Port Macquarie Bowmen 359');
INSERT INTO Club (ClubID, Name) VALUES (360, 'Warrnambool Archery Association 360');
INSERT INTO Club (ClubID, Name) VALUES (361, 'Port Macquarie Archery Club 361');
INSERT INTO Club (ClubID, Name) VALUES (362, 'Toowoomba Archery Association 362');
INSERT INTO Club (ClubID, Name) VALUES (363, 'Shepparton Target Archery Club 363');
INSERT INTO Club (ClubID, Name) VALUES (364, 'Doncaster Archery Club 364');
INSERT INTO Club (ClubID, Name) VALUES (365, 'Hawthorn Target Archery Club 365');
INSERT INTO Club (ClubID, Name) VALUES (366, 'Shepparton Archery Association 366');
INSERT INTO Club (ClubID, Name) VALUES (367, 'Sydney Bowmen 367');
INSERT INTO Club (ClubID, Name) VALUES (368, 'Bunbury Archery Association 368');
INSERT INTO Club (ClubID, Name) VALUES (369, 'Port Macquarie Target Archery Club 369');
INSERT INTO Club (ClubID, Name) VALUES (370, 'Camberwell Field Archers 370');
INSERT INTO Club (ClubID, Name) VALUES (371, 'Warrnambool Target Archery Club 371');
INSERT INTO Club (ClubID, Name) VALUES (372, 'Ballarat Archery Association 372');
INSERT INTO Club (ClubID, Name) VALUES (373, 'Ballarat Bowmen 373');
INSERT INTO Club (ClubID, Name) VALUES (374, 'Tamworth Archery Association 374');
INSERT INTO Club (ClubID, Name) VALUES (375, 'Melbourne Archery Association 375');
INSERT INTO Club (ClubID, Name) VALUES (376, 'Hervey Bay Field Archers 376');
INSERT INTO Club (ClubID, Name) VALUES (377, 'Ringwood Archery Association 377');
INSERT INTO Club (ClubID, Name) VALUES (378, 'Burwood Archers 378');
INSERT INTO Club (ClubID, Name) VALUES (379, 'Dubbo Archers 379');
INSERT INTO Club (ClubID, Name) VALUES (380, 'Sunbury Target Archery Club 380');
INSERT INTO Club (ClubID, Name) VALUES (381, 'Melbourne Archery Association 381');
INSERT INTO Club (ClubID, Name) VALUES (382, 'Swan Hill Target Archery Club 382');
INSERT INTO Club (ClubID, Name) VALUES (383, 'Dandenong Archery Club 383');
INSERT INTO Club (ClubID, Name) VALUES (384, 'Hobart Field Archers 384');
INSERT INTO Club (ClubID, Name) VALUES (385, 'Tamworth Archers 385');
INSERT INTO Club (ClubID, Name) VALUES (386, 'Dubbo Archers 386');
INSERT INTO Club (ClubID, Name) VALUES (387, 'Perth Bowmen 387');
INSERT INTO Club (ClubID, Name) VALUES (388, 'Shepparton Bowmen 388');
INSERT INTO Club (ClubID, Name) VALUES (389, 'Toowoomba Archery Association 389');
INSERT INTO Club (ClubID, Name) VALUES (390, 'Bundaberg Bowmen 390');
INSERT INTO Club (ClubID, Name) VALUES (391, 'Hawthorn Archery Association 391');
INSERT INTO Club (ClubID, Name) VALUES (392, 'Mackay Archery Association 392');
INSERT INTO Club (ClubID, Name) VALUES (393, 'Launceston Archery Club 393');
INSERT INTO Club (ClubID, Name) VALUES (394, 'Bathurst Archery Club 394');
INSERT INTO Club (ClubID, Name) VALUES (395, 'Camberwell Target Archery Club 395');
INSERT INTO Club (ClubID, Name) VALUES (396, 'Perth Bowmen 396');
INSERT INTO Club (ClubID, Name) VALUES (397, 'Ballarat Field Archers 397');
INSERT INTO Club (ClubID, Name) VALUES (398, 'Adelaide Field Archers 398');
INSERT INTO Club (ClubID, Name) VALUES (399, 'Brisbane Archery Club 399');
INSERT INTO Club (ClubID, Name) VALUES (400, 'Bendigo Archers 400');
INSERT INTO Club (ClubID, Name) VALUES (401, 'Melbourne Target Archery Club 401');
INSERT INTO Club (ClubID, Name) VALUES (402, 'Wollongong Archers 402');
INSERT INTO Club (ClubID, Name) VALUES (403, 'Newcastle Archery Association 403');
INSERT INTO Club (ClubID, Name) VALUES (404, 'Dandenong Archery Club 404');
INSERT INTO Club (ClubID, Name) VALUES (405, 'Horsham Archers 405');
INSERT INTO Club (ClubID, Name) VALUES (406, 'Dubbo Field Archers 406');
INSERT INTO Club (ClubID, Name) VALUES (407, 'Launceston Bowmen 407');
INSERT INTO Club (ClubID, Name) VALUES (408, 'Geelong Target Archery Club 408');
INSERT INTO Club (ClubID, Name) VALUES (409, 'Echuca Field Archers 409');
INSERT INTO Club (ClubID, Name) VALUES (410, 'Box Hill Archery Club 410');
INSERT INTO Club (ClubID, Name) VALUES (411, 'Geelong Archers 411');
INSERT INTO Club (ClubID, Name) VALUES (412, 'Bunbury Archery Club 412');
INSERT INTO Club (ClubID, Name) VALUES (413, 'Swan Hill Archery Club 413');
INSERT INTO Club (ClubID, Name) VALUES (414, 'Bunbury Target Archery Club 414');
INSERT INTO Club (ClubID, Name) VALUES (415, 'Ringwood Archery Association 415');
INSERT INTO Club (ClubID, Name) VALUES (416, 'Albury Field Archers 416');
INSERT INTO Club (ClubID, Name) VALUES (417, 'Cairns Archery Club 417');
INSERT INTO Club (ClubID, Name) VALUES (418, 'Swan Hill Field Archers 418');
INSERT INTO Club (ClubID, Name) VALUES (419, 'Cranbourne Archers 419');
INSERT INTO Club (ClubID, Name) VALUES (420, 'Darwin Field Archers 420');
INSERT INTO Club (ClubID, Name) VALUES (421, 'Geelong Bowmen 421');
INSERT INTO Club (ClubID, Name) VALUES (422, 'Ringwood Target Archery Club 422');
INSERT INTO Club (ClubID, Name) VALUES (423, 'Canberra Target Archery Club 423');
INSERT INTO Club (ClubID, Name) VALUES (424, 'Brisbane Bowmen 424');
INSERT INTO Club (ClubID, Name) VALUES (425, 'Warrnambool Archery Association 425');
INSERT INTO Club (ClubID, Name) VALUES (426, 'Dandenong Bowmen 426');
INSERT INTO Club (ClubID, Name) VALUES (427, 'Adelaide Target Archery Club 427');
INSERT INTO Club (ClubID, Name) VALUES (428, 'Frankston Bowmen 428');
INSERT INTO Club (ClubID, Name) VALUES (429, 'Sydney Archery Association 429');
INSERT INTO Club (ClubID, Name) VALUES (430, 'Nowra Archery Club 430');
INSERT INTO Club (ClubID, Name) VALUES (431, 'Tamworth Bowmen 431');
INSERT INTO Club (ClubID, Name) VALUES (432, 'Cranbourne Archery Association 432');
INSERT INTO Club (ClubID, Name) VALUES (433, 'Box Hill Archers 433');
INSERT INTO Club (ClubID, Name) VALUES (434, 'Tamworth Archers 434');
INSERT INTO Club (ClubID, Name) VALUES (435, 'Burwood Target Archery Club 435');
INSERT INTO Club (ClubID, Name) VALUES (436, 'Frankston Bowmen 436');
INSERT INTO Club (ClubID, Name) VALUES (437, 'Sunbury Target Archery Club 437');
INSERT INTO Club (ClubID, Name) VALUES (438, 'Geelong Archery Association 438');
INSERT INTO Club (ClubID, Name) VALUES (439, 'Dubbo Archery Association 439');
INSERT INTO Club (ClubID, Name) VALUES (440, 'Burwood Target Archery Club 440');
INSERT INTO Club (ClubID, Name) VALUES (441, 'Mackay Bowmen 441');
INSERT INTO Club (ClubID, Name) VALUES (442, 'Bendigo Archery Club 442');
INSERT INTO Club (ClubID, Name) VALUES (443, 'Mackay Archery Association 443');
INSERT INTO Club (ClubID, Name) VALUES (444, 'Bendigo Archery Association 444');
INSERT INTO Club (ClubID, Name) VALUES (445, 'Horsham Target Archery Club 445');
INSERT INTO Club (ClubID, Name) VALUES (446, 'Dandenong Archery Association 446');
INSERT INTO Club (ClubID, Name) VALUES (447, 'Hervey Bay Archery Club 447');
INSERT INTO Club (ClubID, Name) VALUES (448, 'Nowra Bowmen 448');
INSERT INTO Club (ClubID, Name) VALUES (449, 'Townsville Archery Association 449');
INSERT INTO Club (ClubID, Name) VALUES (450, 'Toowoomba Bowmen 450');
INSERT INTO Club (ClubID, Name) VALUES (451, 'Launceston Bowmen 451');
INSERT INTO Club (ClubID, Name) VALUES (452, 'Mackay Target Archery Club 452');
INSERT INTO Club (ClubID, Name) VALUES (453, 'Doncaster Bowmen 453');
INSERT INTO Club (ClubID, Name) VALUES (454, 'Sale Archery Club 454');
INSERT INTO Club (ClubID, Name) VALUES (455, 'Mildura Archers 455');
INSERT INTO Club (ClubID, Name) VALUES (456, 'Hobart Archers 456');
INSERT INTO Club (ClubID, Name) VALUES (457, 'Burwood Archery Association 457');
INSERT INTO Club (ClubID, Name) VALUES (458, 'Nowra Target Archery Club 458');
INSERT INTO Club (ClubID, Name) VALUES (459, 'Hawthorn Archers 459');
INSERT INTO Club (ClubID, Name) VALUES (460, 'Doncaster Archery Association 460');
INSERT INTO Club (ClubID, Name) VALUES (461, 'Frankston Field Archers 461');
INSERT INTO Club (ClubID, Name) VALUES (462, 'Nowra Archery Association 462');
INSERT INTO Club (ClubID, Name) VALUES (463, 'Melbourne Archery Club 463');
INSERT INTO Club (ClubID, Name) VALUES (464, 'Rockhampton Archers 464');
INSERT INTO Club (ClubID, Name) VALUES (465, 'Albury Field Archers 465');
INSERT INTO Club (ClubID, Name) VALUES (466, 'Bendigo Bowmen 466');
INSERT INTO Club (ClubID, Name) VALUES (467, 'Dandenong Target Archery Club 467');
INSERT INTO Club (ClubID, Name) VALUES (468, 'Coffs Harbour Archery Association 468');
INSERT INTO Club (ClubID, Name) VALUES (469, 'Sale Target Archery Club 469');
INSERT INTO Club (ClubID, Name) VALUES (470, 'Wagga Wagga Archery Association 470');
INSERT INTO Club (ClubID, Name) VALUES (471, 'Camberwell Target Archery Club 471');
INSERT INTO Club (ClubID, Name) VALUES (472, 'Hervey Bay Bowmen 472');
INSERT INTO Club (ClubID, Name) VALUES (473, 'Doncaster Archery Association 473');
INSERT INTO Club (ClubID, Name) VALUES (474, 'Mackay Bowmen 474');
INSERT INTO Club (ClubID, Name) VALUES (475, 'Launceston Archers 475');
INSERT INTO Club (ClubID, Name) VALUES (476, 'Canberra Field Archers 476');
INSERT INTO Club (ClubID, Name) VALUES (477, 'Cairns Bowmen 477');
INSERT INTO Club (ClubID, Name) VALUES (478, 'Canberra Field Archers 478');
INSERT INTO Club (ClubID, Name) VALUES (479, 'Warrnambool Field Archers 479');
INSERT INTO Club (ClubID, Name) VALUES (480, 'Townsville Archers 480');
INSERT INTO Club (ClubID, Name) VALUES (481, 'Toowoomba Field Archers 481');
INSERT INTO Club (ClubID, Name) VALUES (482, 'Bathurst Bowmen 482');
INSERT INTO Club (ClubID, Name) VALUES (483, 'Burwood Target Archery Club 483');
INSERT INTO Club (ClubID, Name) VALUES (484, 'Hawthorn Target Archery Club 484');
INSERT INTO Club (ClubID, Name) VALUES (485, 'Echuca Bowmen 485');
INSERT INTO Club (ClubID, Name) VALUES (486, 'Darwin Archers 486');
INSERT INTO Club (ClubID, Name) VALUES (487, 'Rockhampton Archers 487');
INSERT INTO Club (ClubID, Name) VALUES (488, 'Coffs Harbour Archers 488');
INSERT INTO Club (ClubID, Name) VALUES (489, 'Bunbury Archery Club 489');
INSERT INTO Club (ClubID, Name) VALUES (490, 'Box Hill Target Archery Club 490');
INSERT INTO Club (ClubID, Name) VALUES (491, 'Newcastle Bowmen 491');
INSERT INTO Club (ClubID, Name) VALUES (492, 'Brisbane Archery Club 492');
INSERT INTO Club (ClubID, Name) VALUES (493, 'Sale Bowmen 493');
INSERT INTO Club (ClubID, Name) VALUES (494, 'Doncaster Archers 494');
INSERT INTO Club (ClubID, Name) VALUES (495, 'Cranbourne Archery Association 495');
INSERT INTO Club (ClubID, Name) VALUES (496, 'Darwin Archery Club 496');
INSERT INTO Club (ClubID, Name) VALUES (497, 'Horsham Bowmen 497');
INSERT INTO Club (ClubID, Name) VALUES (498, 'Bathurst Archery Association 498');
INSERT INTO Club (ClubID, Name) VALUES (499, 'Orange Bowmen 499');
INSERT INTO Club (ClubID, Name) VALUES (500, 'Townsville Archery Club 500');"""

insert_statements.extend(sql_data.strip().splitlines())

# ── Write output ───────────────────────────────────────────────────────────────
output_path = "club_inserts.sql"
with open(output_path, "w") as f:
    f.write("\n".join(insert_statements))

count = sum(1 for s in insert_statements if s.startswith("INSERT"))
print(f"Successfully generated {count} INSERT statements at '{output_path}'")
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
