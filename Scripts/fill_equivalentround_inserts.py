"""
Archery Score Recording Database — Equivalentround table
Generates and downloads equivalentround_inserts.sql with 500 INSERT statements.
Run in Google Colab: the file will be saved and automatically downloaded.

Table: EquivalentRound(EquivalentRoundID, BaseRoundID FK, ActualRoundID FK, ClassID FK, EquipmentID FK, ValidFrom, ValidTo)
ValidTo NULL means currently active. Assumes BaseRound 1-500, Class 1-16, EquipmentType 1-5 exist.
"""

import random
from datetime import date, timedelta

# ── Data pools ─────────────────────────────────────────────────────────────────
# ClassID reference: 1=Female Open, 2=Male Open, 3=50+F, 4=50+M,
#   5=60+F, 6=60+M, 7=70+F, 8=70+M, 9=U21F, 10=U21M,
#   11=U18F, 12=U18M, 13=U16F, 14=U16M, 15=U14F, 16=U14M
class_ids = list(range(1, 17))

# EquipmentID reference: 1=Recurve, 2=Compound, 3=Recurve Barebow,
#   4=Compound Barebow, 5=Longbow
equipment_ids = list(range(1, 6))

def random_date(start_year, end_year):
    start = date(start_year, 1, 1)
    end   = date(end_year, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

# ── Pre-generated INSERT statements ───────────────────────────────────────────
insert_statements = []
insert_statements.append("-- INSERT statements for the Equivalentround table")
insert_statements.append("-- 500 rows")
insert_statements.append("")

sql_data = """\
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (1, 64, 386, 7, 1, '2004-01-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (2, 356, 93, 1, 5, '2010-01-11', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (3, 63, 21, 5, 5, '2004-08-16', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (4, 45, 288, 9, 1, '2001-11-24', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (5, 260, 153, 12, 5, '2003-11-06', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (6, 484, 337, 1, 2, '2006-09-28', '2021-10-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (7, 464, 401, 10, 5, '2009-12-23', '2021-07-01');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (8, 356, 161, 12, 5, '2012-01-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (9, 353, 51, 2, 2, '2000-10-27', '2019-05-12');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (10, 439, 427, 7, 2, '2013-07-03', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (11, 303, 184, 9, 2, '2013-12-15', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (12, 282, 131, 9, 4, '2014-07-28', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (13, 205, 234, 3, 3, '2015-03-05', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (14, 356, 74, 7, 1, '2014-02-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (15, 325, 357, 7, 3, '2012-08-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (16, 421, 262, 6, 4, '2003-06-11', '2024-10-31');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (17, 223, 195, 1, 5, '2005-07-20', '2017-05-25');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (18, 273, 57, 14, 1, '2007-05-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (19, 186, 466, 11, 3, '2003-04-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (20, 116, 141, 1, 1, '2008-06-16', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (21, 114, 194, 4, 1, '2003-12-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (22, 449, 157, 16, 1, '2011-11-12', '2022-06-01');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (23, 444, 145, 9, 5, '2002-03-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (24, 88, 163, 13, 2, '2007-09-28', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (25, 348, 496, 13, 4, '2013-04-14', '2016-02-08');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (26, 352, 263, 5, 2, '2003-03-14', '2024-03-31');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (27, 137, 28, 12, 2, '2015-03-18', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (28, 362, 235, 6, 4, '2007-12-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (29, 258, 147, 9, 4, '2011-09-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (30, 452, 473, 8, 3, '2014-04-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (31, 486, 157, 14, 3, '2002-01-08', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (32, 40, 374, 8, 1, '2003-09-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (33, 44, 381, 10, 5, '2011-01-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (34, 6, 493, 14, 5, '2003-01-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (35, 264, 351, 4, 4, '2000-04-23', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (36, 467, 426, 1, 4, '2015-10-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (37, 177, 126, 2, 5, '2010-01-23', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (38, 346, 477, 8, 2, '2001-09-07', '2017-06-30');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (39, 264, 181, 2, 4, '2011-02-11', '2020-03-08');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (40, 497, 58, 11, 2, '2012-02-03', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (41, 440, 61, 10, 3, '2010-11-01', '2018-05-22');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (42, 2, 378, 13, 2, '2006-11-02', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (43, 492, 330, 2, 4, '2013-11-08', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (44, 30, 183, 1, 5, '2010-04-29', '2019-12-20');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (45, 55, 3, 12, 2, '2009-01-06', '2017-02-19');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (46, 221, 252, 7, 1, '2011-11-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (47, 79, 211, 4, 4, '2000-02-26', '2023-05-13');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (48, 129, 116, 16, 4, '2008-05-24', '2020-10-20');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (49, 457, 94, 9, 1, '2009-11-01', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (50, 225, 83, 5, 3, '2009-09-25', '2023-12-14');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (51, 102, 57, 7, 3, '2000-11-25', '2020-09-20');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (52, 381, 170, 2, 2, '2014-12-10', '2021-05-17');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (53, 492, 341, 9, 1, '2009-06-11', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (54, 254, 410, 5, 3, '2008-12-19', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (55, 473, 380, 13, 2, '2002-06-17', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (56, 406, 11, 5, 2, '2007-09-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (57, 393, 351, 8, 1, '2015-03-19', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (58, 220, 500, 1, 4, '2010-10-08', '2021-06-13');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (59, 43, 390, 14, 2, '2013-11-07', '2021-09-25');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (60, 96, 128, 9, 1, '2005-11-28', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (61, 127, 342, 14, 2, '2010-08-18', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (62, 415, 53, 6, 2, '2013-04-05', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (63, 77, 118, 4, 2, '2008-12-31', '2018-02-26');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (64, 476, 75, 14, 1, '2013-10-29', '2016-07-27');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (65, 195, 209, 10, 2, '2004-12-21', '2021-05-16');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (66, 32, 262, 14, 1, '2006-10-28', '2020-01-29');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (67, 144, 483, 12, 4, '2005-07-16', '2016-07-13');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (68, 94, 21, 1, 1, '2014-10-24', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (69, 109, 147, 16, 3, '2013-08-08', '2018-01-27');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (70, 130, 486, 16, 3, '2007-07-01', '2017-01-31');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (71, 343, 7, 5, 3, '2008-02-01', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (72, 186, 381, 12, 2, '2014-08-01', '2022-07-21');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (73, 197, 45, 4, 2, '2014-02-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (74, 62, 22, 7, 2, '2015-10-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (75, 51, 39, 11, 3, '2010-08-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (76, 104, 274, 5, 1, '2002-11-13', '2022-03-04');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (77, 365, 130, 12, 3, '2010-01-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (78, 61, 467, 14, 1, '2010-10-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (79, 477, 488, 1, 2, '2013-06-09', '2017-06-12');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (80, 149, 24, 2, 2, '2008-11-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (81, 273, 446, 3, 2, '2009-10-26', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (82, 197, 288, 13, 4, '2013-08-14', '2018-01-23');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (83, 2, 82, 7, 5, '2015-08-17', '2024-11-12');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (84, 263, 234, 9, 3, '2004-12-09', '2019-01-04');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (85, 283, 61, 6, 2, '2001-01-08', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (86, 150, 21, 5, 3, '2002-12-25', '2024-11-12');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (87, 27, 329, 8, 2, '2011-12-28', '2023-04-10');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (88, 178, 324, 12, 3, '2001-11-12', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (89, 453, 282, 9, 2, '2009-02-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (90, 151, 167, 2, 1, '2007-12-22', '2019-02-19');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (91, 91, 132, 1, 5, '2014-09-28', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (92, 399, 481, 4, 4, '2014-08-31', '2023-01-09');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (93, 325, 310, 7, 4, '2004-12-12', '2018-04-15');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (94, 298, 323, 13, 2, '2010-01-02', '2024-02-22');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (95, 223, 189, 5, 4, '2002-02-06', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (96, 236, 95, 6, 2, '2012-10-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (97, 374, 93, 10, 1, '2006-12-15', '2017-12-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (98, 419, 202, 7, 1, '2003-03-21', '2018-10-01');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (99, 233, 466, 13, 1, '2011-10-25', '2024-05-31');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (100, 414, 7, 4, 4, '2008-08-11', '2016-02-25');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (101, 391, 426, 2, 2, '2005-07-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (102, 138, 74, 1, 1, '2002-05-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (103, 419, 174, 3, 2, '2003-02-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (104, 289, 457, 15, 2, '2006-11-23', '2017-09-24');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (105, 125, 29, 9, 5, '2002-10-05', '2016-07-01');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (106, 53, 279, 10, 1, '2011-06-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (107, 213, 73, 1, 2, '2000-07-15', '2020-04-27');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (108, 76, 181, 10, 2, '2015-05-08', '2024-01-07');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (109, 422, 462, 4, 4, '2003-10-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (110, 115, 53, 10, 3, '2001-09-16', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (111, 61, 185, 3, 1, '2013-07-23', '2020-10-21');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (112, 272, 172, 6, 4, '2003-05-15', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (113, 352, 155, 10, 3, '2002-05-01', '2021-08-06');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (114, 339, 189, 9, 1, '2000-01-18', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (115, 77, 399, 5, 3, '2003-04-25', '2024-02-02');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (116, 408, 403, 16, 1, '2002-07-16', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (117, 492, 373, 9, 2, '2002-01-10', '2017-06-06');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (118, 94, 393, 13, 3, '2007-02-28', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (119, 247, 356, 14, 5, '2014-04-12', '2024-12-29');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (120, 484, 335, 8, 4, '2009-05-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (121, 276, 274, 16, 5, '2012-01-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (122, 197, 43, 14, 5, '2012-12-16', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (123, 416, 384, 8, 1, '2005-04-10', '2018-04-12');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (124, 436, 9, 12, 5, '2010-08-18', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (125, 472, 57, 2, 3, '2008-02-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (126, 444, 399, 5, 3, '2010-04-29', '2022-03-08');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (127, 498, 477, 14, 2, '2004-09-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (128, 29, 383, 5, 1, '2015-08-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (129, 194, 376, 1, 4, '2008-05-02', '2017-03-10');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (130, 340, 298, 3, 4, '2013-04-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (131, 16, 76, 12, 2, '2001-10-09', '2016-02-21');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (132, 292, 426, 14, 2, '2004-02-03', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (133, 72, 384, 10, 4, '2009-03-25', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (134, 228, 401, 1, 3, '2002-06-30', '2023-03-16');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (135, 17, 310, 6, 5, '2003-08-06', '2020-10-01');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (136, 349, 486, 15, 5, '2015-12-15', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (137, 471, 293, 10, 2, '2009-07-02', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (138, 140, 499, 3, 5, '2008-06-19', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (139, 65, 381, 7, 4, '2013-11-19', '2020-05-25');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (140, 95, 422, 3, 4, '2010-09-15', '2023-03-14');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (141, 208, 424, 13, 2, '2001-03-23', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (142, 332, 218, 7, 3, '2002-06-07', '2020-01-25');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (143, 309, 399, 11, 1, '2005-05-16', '2022-01-27');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (144, 55, 34, 7, 5, '2000-03-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (145, 159, 97, 7, 1, '2005-05-22', '2022-05-24');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (146, 290, 23, 16, 1, '2001-01-28', '2019-06-18');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (147, 5, 183, 10, 4, '2011-03-21', '2024-06-06');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (148, 201, 372, 12, 2, '2015-10-05', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (149, 170, 209, 4, 5, '2003-05-15', '2024-12-04');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (150, 196, 245, 2, 3, '2003-08-13', '2021-03-11');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (151, 41, 454, 3, 2, '2004-11-01', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (152, 335, 73, 6, 5, '2011-07-31', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (153, 312, 334, 11, 4, '2002-12-10', '2020-01-15');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (154, 320, 439, 14, 1, '2015-12-26', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (155, 199, 123, 7, 5, '2013-08-11', '2017-09-16');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (156, 291, 322, 16, 1, '2000-05-02', '2019-06-21');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (157, 281, 445, 3, 4, '2002-02-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (158, 87, 479, 10, 2, '2001-07-12', '2020-01-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (159, 181, 46, 3, 2, '2015-12-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (160, 133, 243, 9, 4, '2014-08-02', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (161, 482, 64, 16, 1, '2008-02-25', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (162, 206, 210, 5, 4, '2008-03-23', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (163, 320, 488, 11, 3, '2001-11-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (164, 260, 231, 9, 1, '2013-12-02', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (165, 30, 380, 8, 5, '2000-03-06', '2017-03-07');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (166, 149, 193, 6, 5, '2008-12-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (167, 115, 199, 15, 1, '2007-10-29', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (168, 329, 274, 15, 1, '2001-12-04', '2017-03-19');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (169, 470, 492, 13, 4, '2004-06-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (170, 34, 163, 11, 5, '2010-11-27', '2024-04-24');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (171, 244, 59, 9, 4, '2000-11-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (172, 486, 241, 5, 2, '2007-03-07', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (173, 308, 397, 13, 1, '2008-02-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (174, 243, 110, 2, 2, '2000-07-06', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (175, 351, 217, 9, 3, '2014-04-04', '2017-08-03');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (176, 36, 141, 13, 1, '2006-09-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (177, 232, 447, 14, 5, '2004-10-19', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (178, 133, 95, 2, 1, '2009-08-11', '2024-06-12');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (179, 153, 85, 7, 3, '2009-05-26', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (180, 275, 353, 6, 4, '2007-12-15', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (181, 293, 200, 1, 5, '2013-05-23', '2024-02-08');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (182, 342, 297, 5, 3, '2014-11-23', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (183, 481, 376, 11, 1, '2003-05-17', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (184, 479, 76, 16, 3, '2002-07-19', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (185, 346, 209, 9, 5, '2000-01-31', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (186, 483, 427, 5, 4, '2014-05-01', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (187, 50, 19, 7, 2, '2009-06-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (188, 397, 86, 13, 2, '2007-10-22', '2018-02-21');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (189, 498, 348, 1, 3, '2008-02-28', '2019-06-11');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (190, 258, 420, 4, 4, '2014-07-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (191, 212, 211, 12, 3, '2012-03-01', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (192, 499, 392, 11, 1, '2003-12-11', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (193, 192, 91, 6, 5, '2009-10-10', '2023-05-25');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (194, 353, 349, 14, 3, '2015-09-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (195, 474, 464, 4, 1, '2002-04-30', '2016-03-08');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (196, 316, 478, 14, 1, '2011-02-18', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (197, 320, 475, 4, 4, '2011-04-16', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (198, 17, 342, 10, 4, '2004-10-01', '2021-02-05');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (199, 283, 196, 4, 2, '2010-07-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (200, 180, 496, 15, 4, '2014-06-18', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (201, 380, 203, 1, 3, '2005-01-08', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (202, 138, 451, 9, 3, '2009-04-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (203, 3, 461, 14, 1, '2000-05-07', '2024-11-11');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (204, 192, 431, 11, 3, '2003-10-28', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (205, 221, 124, 13, 2, '2013-10-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (206, 425, 27, 14, 2, '2014-04-09', '2024-03-01');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (207, 89, 207, 11, 5, '2003-07-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (208, 51, 364, 5, 5, '2002-08-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (209, 402, 201, 9, 5, '2003-07-26', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (210, 105, 48, 3, 1, '2009-10-23', '2024-08-20');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (211, 304, 79, 1, 5, '2015-11-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (212, 498, 41, 13, 1, '2002-12-05', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (213, 325, 324, 12, 2, '2005-05-17', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (214, 114, 153, 7, 5, '2005-07-02', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (215, 414, 403, 13, 3, '2014-10-14', '2016-12-05');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (216, 479, 74, 1, 5, '2002-04-27', '2022-09-06');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (217, 63, 55, 5, 3, '2005-11-16', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (218, 48, 40, 16, 3, '2004-08-30', '2021-07-04');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (219, 408, 12, 14, 1, '2010-11-29', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (220, 40, 108, 14, 4, '2007-01-12', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (221, 231, 414, 6, 2, '2006-09-13', '2018-01-01');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (222, 338, 291, 2, 1, '2007-09-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (223, 248, 315, 1, 2, '2011-09-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (224, 475, 63, 7, 5, '2000-08-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (225, 266, 263, 5, 2, '2008-03-08', '2018-06-07');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (226, 16, 168, 5, 2, '2001-11-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (227, 482, 65, 9, 3, '2010-10-20', '2017-01-11');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (228, 179, 363, 10, 4, '2011-02-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (229, 485, 205, 7, 3, '2003-11-17', '2024-01-17');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (230, 144, 493, 13, 1, '2013-02-02', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (231, 301, 160, 6, 2, '2010-12-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (232, 229, 217, 9, 3, '2013-12-20', '2020-04-17');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (233, 220, 103, 12, 3, '2014-03-11', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (234, 231, 86, 2, 5, '2005-09-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (235, 151, 310, 12, 4, '2000-09-02', '2019-08-14');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (236, 220, 405, 6, 3, '2005-07-02', '2023-05-14');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (237, 191, 191, 5, 3, '2002-09-28', '2023-09-20');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (238, 6, 368, 11, 2, '2010-06-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (239, 165, 461, 8, 5, '2001-06-26', '2022-09-30');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (240, 109, 270, 7, 1, '2012-07-31', '2022-10-25');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (241, 485, 453, 3, 5, '2014-06-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (242, 388, 223, 11, 3, '2004-06-11', '2024-12-31');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (243, 253, 256, 2, 3, '2009-06-12', '2021-01-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (244, 88, 308, 11, 5, '2008-08-02', '2016-03-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (245, 146, 10, 1, 4, '2006-05-18', '2020-07-07');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (246, 19, 459, 2, 3, '2014-06-18', '2021-04-08');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (247, 49, 425, 14, 3, '2006-02-28', '2019-11-17');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (248, 205, 41, 11, 4, '2013-09-25', '2019-05-07');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (249, 357, 233, 16, 1, '2008-05-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (250, 53, 15, 8, 1, '2000-03-26', '2019-08-15');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (251, 442, 353, 14, 2, '2003-10-26', '2024-02-13');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (252, 462, 416, 12, 5, '2000-02-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (253, 445, 27, 9, 1, '2002-06-26', '2019-05-31');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (254, 39, 136, 11, 5, '2008-07-06', '2017-11-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (255, 474, 71, 15, 1, '2002-10-31', '2017-08-29');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (256, 386, 300, 14, 4, '2014-12-27', '2021-12-01');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (257, 124, 296, 16, 4, '2006-04-17', '2024-03-12');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (258, 248, 116, 3, 3, '2006-08-23', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (259, 181, 286, 8, 2, '2015-08-03', '2021-07-18');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (260, 31, 109, 1, 2, '2010-07-02', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (261, 97, 250, 4, 3, '2004-09-05', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (262, 390, 271, 11, 3, '2015-11-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (263, 79, 435, 4, 2, '2004-11-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (264, 198, 500, 15, 5, '2011-07-08', '2020-06-27');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (265, 97, 36, 9, 4, '2003-09-07', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (266, 488, 446, 4, 2, '2010-05-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (267, 382, 57, 8, 1, '2010-05-03', '2016-04-27');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (268, 244, 339, 15, 3, '2005-12-15', '2022-03-04');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (269, 44, 182, 14, 2, '2003-05-18', '2020-10-30');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (270, 261, 171, 2, 4, '2006-02-11', '2016-07-20');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (271, 333, 196, 14, 2, '2006-08-05', '2017-12-24');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (272, 305, 142, 16, 5, '2009-09-21', '2016-07-23');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (273, 331, 128, 4, 2, '2002-08-01', '2016-05-26');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (274, 295, 137, 8, 1, '2011-12-08', '2018-07-16');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (275, 452, 318, 13, 4, '2008-10-23', '2024-03-25');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (276, 422, 451, 9, 4, '2004-08-12', '2018-04-13');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (277, 178, 327, 10, 5, '2006-06-17', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (278, 49, 95, 16, 3, '2015-06-06', '2019-07-14');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (279, 349, 36, 6, 2, '2007-06-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (280, 73, 493, 1, 4, '2009-08-06', '2017-12-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (281, 499, 136, 3, 2, '2015-03-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (282, 5, 305, 12, 4, '2013-01-29', '2018-10-10');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (283, 242, 57, 2, 1, '2012-09-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (284, 149, 428, 8, 5, '2011-04-14', '2017-08-23');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (285, 397, 49, 4, 3, '2007-07-12', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (286, 377, 180, 9, 4, '2005-09-07', '2016-02-25');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (287, 424, 181, 10, 3, '2011-08-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (288, 439, 443, 16, 1, '2006-01-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (289, 373, 328, 1, 2, '2009-03-15', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (290, 338, 73, 12, 4, '2000-09-10', '2024-04-23');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (291, 357, 499, 14, 3, '2004-08-17', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (292, 100, 472, 13, 1, '2006-02-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (293, 348, 279, 15, 5, '2003-12-04', '2023-08-13');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (294, 179, 455, 11, 4, '2013-03-19', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (295, 142, 159, 7, 1, '2012-12-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (296, 176, 428, 4, 4, '2010-03-16', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (297, 406, 406, 12, 3, '2002-06-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (298, 256, 475, 5, 4, '2015-04-10', '2019-04-01');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (299, 320, 286, 6, 3, '2010-12-02', '2024-12-19');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (300, 151, 8, 15, 1, '2004-11-15', '2022-08-26');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (301, 64, 28, 16, 3, '2000-02-11', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (302, 339, 428, 1, 1, '2005-08-21', '2019-03-06');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (303, 403, 440, 5, 1, '2015-12-30', '2024-03-21');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (304, 101, 222, 3, 3, '2004-11-27', '2019-12-23');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (305, 128, 416, 13, 4, '2008-12-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (306, 51, 458, 9, 3, '2013-05-22', '2022-04-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (307, 224, 348, 11, 5, '2003-02-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (308, 103, 129, 5, 4, '2012-06-06', '2019-06-03');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (309, 44, 153, 15, 5, '2004-02-11', '2020-11-24');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (310, 50, 71, 15, 3, '2011-04-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (311, 365, 184, 15, 3, '2009-08-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (312, 493, 211, 15, 1, '2012-07-14', '2024-08-06');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (313, 216, 46, 5, 5, '2006-10-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (314, 298, 263, 12, 2, '2013-12-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (315, 290, 450, 10, 1, '2008-10-21', '2023-07-07');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (316, 4, 237, 15, 1, '2001-11-24', '2023-04-15');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (317, 55, 171, 4, 3, '2012-09-06', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (318, 170, 443, 2, 1, '2013-02-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (319, 379, 368, 2, 2, '2011-07-31', '2024-04-20');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (320, 496, 254, 5, 2, '2015-02-26', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (321, 80, 155, 10, 1, '2010-11-16', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (322, 103, 59, 3, 1, '2003-06-07', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (323, 62, 267, 4, 2, '2004-07-31', '2016-04-10');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (324, 427, 259, 15, 4, '2001-03-31', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (325, 154, 208, 16, 2, '2005-04-08', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (326, 280, 134, 15, 5, '2002-10-06', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (327, 326, 12, 6, 2, '2014-09-29', '2021-09-26');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (328, 380, 359, 7, 4, '2010-10-10', '2023-06-27');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (329, 52, 492, 16, 3, '2014-12-22', '2020-04-29');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (330, 358, 410, 4, 4, '2009-05-08', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (331, 76, 15, 10, 4, '2002-09-11', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (332, 6, 298, 10, 1, '2014-06-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (333, 337, 318, 15, 1, '2007-12-15', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (334, 240, 452, 15, 3, '2000-03-15', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (335, 184, 257, 7, 3, '2015-11-03', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (336, 263, 33, 6, 2, '2007-11-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (337, 289, 174, 15, 2, '2006-03-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (338, 338, 156, 13, 1, '2014-06-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (339, 493, 242, 6, 5, '2015-11-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (340, 398, 338, 9, 2, '2015-08-26', '2022-07-06');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (341, 179, 300, 13, 1, '2001-01-03', '2024-03-20');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (342, 82, 119, 4, 1, '2011-03-15', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (343, 244, 166, 8, 2, '2002-05-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (344, 90, 373, 13, 4, '2001-06-11', '2018-10-22');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (345, 59, 20, 3, 4, '2008-05-24', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (346, 431, 16, 6, 3, '2002-05-31', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (347, 194, 69, 7, 2, '2005-08-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (348, 348, 147, 8, 2, '2003-08-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (349, 271, 415, 7, 1, '2013-01-20', '2023-07-01');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (350, 50, 105, 2, 2, '2000-02-12', '2020-07-29');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (351, 291, 280, 3, 3, '2004-02-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (352, 491, 467, 16, 2, '2004-08-26', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (353, 243, 257, 12, 3, '2013-11-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (354, 437, 71, 3, 4, '2009-08-03', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (355, 448, 37, 3, 2, '2011-08-08', '2017-04-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (356, 256, 119, 2, 5, '2012-02-15', '2018-07-06');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (357, 421, 482, 10, 3, '2008-10-03', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (358, 35, 447, 6, 3, '2001-09-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (359, 124, 437, 10, 4, '2013-11-15', '2023-10-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (360, 457, 57, 16, 3, '2014-08-26', '2019-10-16');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (361, 216, 134, 7, 3, '2001-05-01', '2022-02-18');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (362, 419, 376, 11, 1, '2005-04-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (363, 413, 486, 2, 3, '2001-08-02', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (364, 307, 379, 3, 5, '2010-09-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (365, 139, 371, 2, 1, '2000-10-18', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (366, 116, 333, 12, 4, '2010-09-17', '2018-07-21');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (367, 11, 477, 2, 1, '2004-05-26', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (368, 441, 195, 1, 5, '2010-10-24', '2024-08-02');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (369, 194, 357, 5, 4, '2015-09-24', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (370, 71, 60, 15, 1, '2013-10-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (371, 189, 181, 7, 3, '2009-10-16', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (372, 122, 119, 3, 5, '2000-03-23', '2024-05-19');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (373, 386, 455, 2, 1, '2005-08-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (374, 40, 30, 5, 4, '2004-01-19', '2019-07-10');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (375, 180, 309, 8, 3, '2002-11-28', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (376, 246, 337, 4, 1, '2001-09-17', '2022-02-04');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (377, 106, 254, 12, 2, '2009-12-12', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (378, 483, 188, 10, 2, '2011-10-25', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (379, 164, 358, 4, 1, '2007-10-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (380, 362, 487, 16, 3, '2001-10-04', '2017-07-15');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (381, 431, 500, 8, 3, '2012-05-26', '2020-03-05');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (382, 372, 418, 5, 1, '2005-04-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (383, 333, 392, 15, 1, '2000-06-23', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (384, 18, 139, 9, 5, '2008-08-13', '2016-12-12');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (385, 31, 143, 13, 4, '2000-06-03', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (386, 197, 228, 2, 2, '2004-08-12', '2023-05-27');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (387, 221, 273, 2, 3, '2000-09-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (388, 179, 480, 1, 5, '2007-07-17', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (389, 465, 135, 7, 1, '2007-08-25', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (390, 319, 223, 14, 1, '2002-06-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (391, 488, 370, 10, 5, '2010-05-25', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (392, 369, 291, 9, 2, '2008-07-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (393, 474, 122, 5, 1, '2006-04-18', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (394, 487, 141, 3, 2, '2012-03-04', '2022-05-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (395, 203, 20, 9, 3, '2006-01-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (396, 401, 335, 1, 1, '2006-11-19', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (397, 165, 429, 9, 2, '2009-12-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (398, 226, 5, 15, 1, '2008-01-17', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (399, 433, 285, 7, 4, '2001-04-24', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (400, 41, 142, 11, 1, '2009-11-17', '2024-08-03');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (401, 403, 142, 9, 4, '2002-11-08', '2017-12-15');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (402, 76, 447, 2, 2, '2002-07-26', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (403, 95, 351, 15, 5, '2007-02-12', '2024-01-17');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (404, 117, 32, 9, 3, '2000-05-12', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (405, 440, 435, 12, 5, '2001-01-01', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (406, 180, 56, 3, 5, '2009-12-14', '2016-11-13');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (407, 122, 105, 11, 5, '2008-04-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (408, 349, 213, 3, 4, '2006-05-08', '2019-08-30');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (409, 311, 404, 12, 3, '2009-02-25', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (410, 192, 241, 10, 5, '2000-09-12', '2016-07-01');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (411, 149, 477, 5, 5, '2000-07-28', '2018-05-16');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (412, 414, 161, 12, 2, '2008-06-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (413, 17, 337, 5, 4, '2014-07-24', '2016-11-12');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (414, 491, 479, 8, 5, '2011-04-17', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (415, 323, 281, 14, 5, '2002-09-20', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (416, 271, 409, 2, 5, '2010-08-05', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (417, 267, 226, 11, 3, '2004-05-16', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (418, 151, 467, 8, 3, '2005-06-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (419, 186, 119, 15, 3, '2002-08-03', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (420, 228, 376, 14, 3, '2001-10-14', '2021-09-02');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (421, 40, 469, 12, 4, '2013-07-28', '2024-10-25');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (422, 215, 118, 5, 5, '2005-06-29', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (423, 209, 346, 5, 5, '2005-11-02', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (424, 175, 161, 4, 1, '2009-02-28', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (425, 76, 295, 16, 2, '2004-01-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (426, 8, 86, 4, 4, '2005-11-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (427, 365, 477, 16, 1, '2002-11-01', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (428, 427, 221, 1, 2, '2001-08-21', '2021-12-08');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (429, 471, 199, 14, 3, '2002-11-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (430, 286, 124, 10, 1, '2007-07-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (431, 460, 173, 4, 1, '2001-08-27', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (432, 182, 487, 15, 4, '2014-02-23', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (433, 428, 224, 10, 4, '2015-09-14', '2018-01-21');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (434, 371, 393, 3, 2, '2000-03-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (435, 190, 346, 15, 4, '2007-03-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (436, 261, 370, 9, 1, '2005-03-17', '2019-10-29');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (437, 25, 289, 14, 3, '2007-03-29', '2024-06-28');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (438, 92, 489, 5, 1, '2004-09-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (439, 143, 295, 11, 1, '2007-10-16', '2017-04-30');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (440, 148, 141, 16, 4, '2005-01-06', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (441, 148, 481, 9, 5, '2002-05-19', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (442, 342, 143, 5, 1, '2004-08-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (443, 261, 387, 6, 1, '2013-06-03', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (444, 492, 457, 7, 1, '2010-12-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (445, 14, 190, 7, 3, '2012-10-22', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (446, 228, 267, 5, 4, '2006-08-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (447, 367, 362, 4, 4, '2009-09-11', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (448, 45, 443, 5, 3, '2014-12-31', '2019-12-19');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (449, 412, 41, 8, 1, '2007-05-03', '2019-10-05');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (450, 142, 233, 3, 3, '2000-11-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (451, 478, 362, 11, 2, '2012-07-08', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (452, 450, 321, 2, 1, '2005-07-07', '2020-03-20');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (453, 447, 483, 8, 2, '2005-12-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (454, 249, 417, 6, 4, '2006-05-04', '2023-02-13');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (455, 449, 46, 7, 1, '2009-09-27', '2022-04-03');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (456, 313, 107, 6, 1, '2009-05-18', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (457, 315, 195, 8, 3, '2010-11-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (458, 489, 93, 10, 2, '2006-07-21', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (459, 251, 408, 13, 5, '2008-01-04', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (460, 152, 50, 8, 1, '2006-06-11', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (461, 229, 167, 8, 4, '2002-08-06', '2019-07-30');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (462, 339, 59, 12, 4, '2015-10-22', '2021-06-04');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (463, 431, 413, 16, 5, '2009-03-29', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (464, 15, 149, 9, 5, '2004-10-28', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (465, 401, 210, 2, 5, '2007-04-01', '2019-07-24');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (466, 211, 201, 15, 4, '2008-12-09', '2016-08-11');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (467, 138, 249, 8, 3, '2014-04-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (468, 158, 230, 14, 2, '2012-11-02', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (469, 275, 106, 4, 5, '2013-09-12', '2022-10-13');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (470, 277, 11, 1, 4, '2002-01-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (471, 171, 468, 12, 5, '2001-06-03', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (472, 266, 108, 12, 5, '2004-06-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (473, 430, 275, 13, 2, '2006-07-05', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (474, 467, 192, 11, 4, '2004-11-01', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (475, 128, 482, 1, 1, '2000-06-13', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (476, 270, 53, 13, 4, '2000-12-12', '2019-05-19');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (477, 13, 118, 8, 1, '2006-02-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (478, 417, 402, 13, 4, '2002-12-10', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (479, 449, 139, 3, 1, '2001-08-28', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (480, 361, 391, 14, 1, '2000-04-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (481, 278, 310, 5, 1, '2013-03-11', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (482, 100, 426, 10, 3, '2009-07-14', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (483, 12, 155, 9, 4, '2004-07-18', '2023-05-11');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (484, 296, 242, 13, 3, '2009-08-19', '2020-07-22');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (485, 288, 143, 16, 3, '2015-10-06', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (486, 126, 196, 1, 4, '2008-10-29', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (487, 391, 280, 4, 4, '2005-01-09', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (488, 13, 204, 8, 4, '2008-04-17', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (489, 56, 330, 10, 3, '2003-03-23', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (490, 500, 43, 4, 5, '2003-10-18', '2021-06-29');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (491, 304, 128, 3, 2, '2009-01-15', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (492, 243, 268, 8, 1, '2011-01-25', '2019-06-29');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (493, 380, 173, 5, 1, '2007-03-18', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (494, 307, 209, 1, 3, '2015-06-26', '2022-04-22');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (495, 407, 251, 16, 3, '2014-08-16', '2021-03-04');
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (496, 363, 248, 3, 1, '2009-07-19', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (497, 193, 66, 1, 2, '2011-08-30', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (498, 86, 102, 15, 1, '2000-11-15', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (499, 254, 88, 16, 2, '2012-04-08', NULL);
INSERT INTO EquivalentRound (EquivalentRoundID, BaseRoundID, ActualRoundID, ClassID, EquipmentID, ValidFrom, ValidTo) VALUES (500, 5, 152, 4, 4, '2006-08-07', NULL);"""

insert_statements.extend(sql_data.strip().splitlines())

# ── Write output ───────────────────────────────────────────────────────────────
output_path = "equivalentround_inserts.sql"
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
