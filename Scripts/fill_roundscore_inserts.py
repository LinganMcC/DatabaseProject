"""
Archery Score Recording Database — Roundscore table
Generates and downloads roundscore_inserts.sql with 500 INSERT statements.
Run in Google Colab: the file will be saved and automatically downloaded.

Table: RoundScore(ScoreID, CompetitionID FK, ArcherID FK, BaseRoundID FK, IsApproved, Date, Time)
CompetitionID NULL = practice score. Assumes Archer 1-500, BaseRound 1-500, Competition 1-500 exist.
"""

import random
from datetime import date, time, timedelta

# ── Data pools ─────────────────────────────────────────────────────────────────
# Approval status: 0 = pending, 1 = approved
approval_values = [0, 1]

# Typical competition start times
start_hours   = list(range(8, 18))
start_minutes = [0, 15, 30, 45]

def random_date(start_year=2010, end_year=2024):
    start = date(start_year, 1, 1)
    end   = date(end_year, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_time():
    return time(random.randint(8, 17), random.choice([0, 15, 30, 45]))

# ── Pre-generated INSERT statements ───────────────────────────────────────────
insert_statements = []
insert_statements.append("-- INSERT statements for the Roundscore table")
insert_statements.append("-- 500 rows")
insert_statements.append("")

sql_data = """\
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (1, NULL, 139, 268, 1, '2023-10-18', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (2, 268, 351, 105, 1, '2021-08-25', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (3, NULL, 108, 480, 1, '2013-01-13', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (4, 214, 92, 77, 1, '2011-07-04', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (5, NULL, 103, 356, 0, '2022-01-23', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (6, 320, 240, 305, 0, '2011-07-01', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (7, 8, 476, 99, 1, '2016-05-17', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (8, 393, 207, 479, 1, '2022-08-02', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (9, 79, 53, 375, 0, '2016-04-12', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (10, NULL, 65, 409, 1, '2017-05-28', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (11, NULL, 378, 447, 1, '2014-09-11', '10:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (12, NULL, 111, 47, 0, '2013-03-20', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (13, NULL, 166, 40, 0, '2013-01-27', '16:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (14, NULL, 242, 168, 1, '2021-03-23', '09:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (15, NULL, 194, 397, 1, '2020-08-22', '13:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (16, NULL, 163, 272, 0, '2023-07-31', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (17, NULL, 427, 143, 0, '2019-10-22', '16:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (18, NULL, 404, 129, 0, '2022-07-07', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (19, 444, 188, 438, 1, '2017-10-05', '14:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (20, NULL, 449, 472, 0, '2018-07-31', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (21, NULL, 6, 101, 1, '2018-02-05', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (22, 159, 169, 49, 1, '2015-09-10', '16:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (23, NULL, 18, 332, 1, '2024-05-23', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (24, 357, 361, 130, 1, '2024-01-10', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (25, NULL, 475, 242, 1, '2020-12-30', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (26, NULL, 332, 385, 0, '2010-11-09', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (27, NULL, 366, 79, 0, '2012-12-14', '09:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (28, NULL, 62, 29, 1, '2024-04-19', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (29, 279, 143, 437, 0, '2024-09-10', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (30, 345, 435, 461, 1, '2013-10-18', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (31, NULL, 482, 341, 1, '2019-05-04', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (32, 390, 257, 76, 1, '2011-11-19', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (33, 312, 102, 353, 1, '2013-11-17', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (34, 180, 61, 175, 1, '2022-09-29', '09:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (35, 471, 47, 94, 0, '2014-03-01', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (36, NULL, 404, 6, 0, '2024-04-23', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (37, 371, 483, 127, 1, '2024-05-28', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (38, 195, 362, 147, 0, '2016-04-04', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (39, NULL, 428, 97, 1, '2014-06-21', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (40, 226, 136, 48, 1, '2017-12-19', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (41, 329, 268, 231, 0, '2010-10-28', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (42, 292, 108, 360, 1, '2017-10-12', '12:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (43, 496, 258, 283, 1, '2012-01-14', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (44, 240, 134, 17, 0, '2021-08-06', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (45, 301, 166, 191, 1, '2024-10-06', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (46, 54, 323, 184, 0, '2013-07-24', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (47, 332, 463, 52, 0, '2018-01-11', '12:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (48, NULL, 96, 386, 0, '2019-11-06', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (49, NULL, 356, 223, 1, '2020-08-15', '11:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (50, NULL, 308, 173, 1, '2018-12-31', '12:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (51, NULL, 450, 120, 0, '2019-06-11', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (52, NULL, 206, 304, 0, '2013-09-05', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (53, NULL, 454, 306, 0, '2022-09-27', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (54, NULL, 404, 492, 0, '2012-01-11', '12:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (55, NULL, 235, 203, 0, '2020-05-01', '08:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (56, 89, 155, 158, 0, '2014-02-21', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (57, NULL, 371, 126, 0, '2022-06-16', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (58, NULL, 177, 52, 1, '2022-05-02', '14:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (59, NULL, 343, 193, 1, '2015-06-12', '09:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (60, 391, 479, 69, 1, '2017-05-03', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (61, NULL, 274, 37, 1, '2020-12-14', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (62, 312, 92, 394, 0, '2018-04-12', '13:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (63, NULL, 1, 313, 1, '2011-09-25', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (64, NULL, 23, 109, 1, '2019-10-07', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (65, 93, 218, 78, 1, '2016-12-23', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (66, 491, 489, 216, 0, '2013-09-01', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (67, NULL, 43, 178, 0, '2024-09-16', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (68, 66, 295, 260, 1, '2020-03-13', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (69, NULL, 344, 206, 1, '2011-03-23', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (70, 325, 60, 310, 1, '2021-04-05', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (71, NULL, 433, 274, 1, '2012-07-03', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (72, NULL, 197, 446, 0, '2013-05-16', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (73, NULL, 363, 303, 1, '2014-06-07', '16:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (74, NULL, 238, 145, 0, '2012-09-22', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (75, 456, 307, 352, 1, '2015-08-30', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (76, NULL, 393, 420, 0, '2022-03-05', '12:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (77, 214, 9, 229, 1, '2016-09-04', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (78, 19, 273, 379, 1, '2015-07-30', '10:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (79, NULL, 65, 373, 0, '2024-03-12', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (80, NULL, 177, 498, 1, '2023-11-05', '11:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (81, 168, 191, 20, 0, '2023-09-01', '09:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (82, NULL, 372, 41, 1, '2024-04-13', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (83, NULL, 95, 487, 1, '2024-08-23', '09:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (84, NULL, 407, 99, 1, '2016-10-19', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (85, NULL, 26, 192, 1, '2014-10-29', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (86, NULL, 399, 96, 1, '2021-04-01', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (87, NULL, 348, 146, 1, '2010-02-11', '14:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (88, 213, 337, 67, 1, '2015-12-28', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (89, 116, 10, 364, 1, '2014-12-16', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (90, NULL, 312, 424, 1, '2023-03-10', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (91, NULL, 244, 477, 0, '2017-09-10', '13:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (92, 228, 78, 237, 1, '2014-09-22', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (93, NULL, 131, 207, 0, '2024-10-26', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (94, NULL, 288, 177, 0, '2014-08-28', '16:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (95, 385, 162, 232, 1, '2010-08-31', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (96, NULL, 290, 221, 1, '2010-07-11', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (97, NULL, 193, 472, 0, '2018-06-28', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (98, 112, 109, 57, 1, '2014-01-03', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (99, NULL, 181, 385, 0, '2019-05-19', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (100, 186, 323, 55, 1, '2021-04-07', '16:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (101, 207, 254, 388, 1, '2016-06-03', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (102, NULL, 91, 205, 1, '2010-01-28', '16:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (103, NULL, 336, 89, 0, '2018-08-07', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (104, NULL, 211, 97, 0, '2023-11-18', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (105, NULL, 258, 42, 1, '2010-07-07', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (106, 321, 242, 351, 0, '2018-04-22', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (107, NULL, 443, 99, 0, '2020-04-08', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (108, 480, 365, 472, 0, '2017-03-28', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (109, 16, 106, 296, 1, '2020-04-19', '11:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (110, NULL, 408, 91, 1, '2021-03-21', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (111, NULL, 466, 82, 0, '2020-05-14', '09:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (112, NULL, 350, 347, 1, '2021-08-28', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (113, 214, 491, 134, 0, '2023-08-13', '16:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (114, NULL, 424, 372, 0, '2016-07-27', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (115, 367, 475, 262, 1, '2019-08-12', '09:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (116, 135, 389, 423, 0, '2013-10-16', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (117, NULL, 73, 468, 0, '2020-10-28', '11:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (118, 329, 356, 38, 1, '2021-01-09', '11:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (119, 353, 228, 170, 1, '2015-10-14', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (120, NULL, 390, 72, 0, '2021-09-14', '12:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (121, 190, 289, 186, 1, '2016-11-17', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (122, NULL, 226, 345, 1, '2013-06-19', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (123, NULL, 440, 197, 1, '2024-04-13', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (124, NULL, 299, 156, 0, '2023-02-08', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (125, 261, 382, 446, 1, '2020-09-12', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (126, NULL, 330, 80, 1, '2021-09-27', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (127, NULL, 249, 332, 0, '2021-10-12', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (128, NULL, 195, 8, 0, '2017-09-05', '11:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (129, 77, 143, 312, 0, '2024-07-30', '11:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (130, NULL, 292, 468, 0, '2021-10-03', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (131, 17, 205, 321, 0, '2017-05-23', '16:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (132, 493, 274, 434, 0, '2011-04-04', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (133, 409, 379, 94, 0, '2015-02-14', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (134, 312, 137, 283, 1, '2012-01-19', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (135, NULL, 68, 268, 1, '2011-05-14', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (136, 390, 298, 245, 1, '2012-03-16', '16:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (137, 325, 38, 101, 1, '2012-08-11', '15:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (138, NULL, 52, 278, 0, '2023-06-03', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (139, NULL, 298, 221, 0, '2019-12-06', '11:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (140, NULL, 129, 387, 1, '2023-06-28', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (141, NULL, 169, 260, 1, '2021-07-14', '12:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (142, 273, 128, 175, 1, '2022-08-03', '16:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (143, NULL, 58, 388, 0, '2020-12-08', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (144, NULL, 261, 241, 1, '2013-08-29', '10:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (145, NULL, 345, 156, 0, '2019-12-10', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (146, 56, 391, 119, 0, '2016-11-21', '16:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (147, 272, 242, 53, 1, '2023-09-03', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (148, 99, 393, 203, 0, '2013-07-17', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (149, 265, 243, 335, 1, '2016-01-16', '11:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (150, NULL, 439, 428, 1, '2018-04-26', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (151, 182, 425, 382, 1, '2020-02-02', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (152, NULL, 391, 214, 0, '2019-01-24', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (153, 413, 72, 500, 1, '2016-02-25', '08:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (154, 367, 132, 151, 1, '2010-07-13', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (155, NULL, 167, 286, 0, '2014-10-28', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (156, NULL, 55, 39, 0, '2013-08-07', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (157, NULL, 304, 241, 0, '2024-10-15', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (158, 311, 301, 193, 0, '2012-04-10', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (159, 190, 225, 473, 1, '2012-06-28', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (160, NULL, 38, 167, 1, '2013-05-28', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (161, NULL, 288, 46, 1, '2015-07-02', '13:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (162, NULL, 419, 150, 0, '2013-02-24', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (163, NULL, 185, 464, 1, '2014-10-26', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (164, NULL, 236, 186, 1, '2014-06-19', '12:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (165, NULL, 478, 12, 0, '2012-09-03', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (166, 250, 409, 25, 0, '2021-06-28', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (167, NULL, 17, 492, 1, '2022-01-31', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (168, NULL, 325, 35, 0, '2022-09-05', '09:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (169, NULL, 409, 263, 0, '2022-11-15', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (170, NULL, 393, 351, 1, '2016-03-18', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (171, NULL, 379, 78, 1, '2011-08-22', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (172, NULL, 400, 355, 1, '2010-06-25', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (173, 425, 200, 10, 0, '2015-01-20', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (174, 439, 115, 300, 1, '2021-12-10', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (175, NULL, 295, 474, 1, '2022-12-09', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (176, NULL, 106, 158, 0, '2012-04-06', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (177, NULL, 277, 179, 0, '2017-05-06', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (178, NULL, 104, 156, 0, '2019-07-08', '12:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (179, NULL, 112, 396, 1, '2010-08-12', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (180, 486, 193, 14, 1, '2014-09-05', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (181, NULL, 205, 102, 0, '2018-07-15', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (182, 90, 260, 468, 0, '2013-08-27', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (183, NULL, 380, 310, 1, '2017-02-08', '14:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (184, 47, 410, 260, 1, '2020-09-20', '12:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (185, NULL, 9, 4, 1, '2019-06-03', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (186, 485, 159, 429, 0, '2019-09-27', '12:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (187, NULL, 44, 334, 1, '2020-07-28', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (188, NULL, 460, 166, 0, '2013-02-26', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (189, NULL, 66, 266, 0, '2013-02-22', '15:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (190, 411, 108, 444, 1, '2018-05-03', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (191, NULL, 215, 89, 0, '2021-08-19', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (192, 474, 57, 403, 0, '2010-09-03', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (193, 321, 192, 466, 1, '2023-12-13', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (194, NULL, 170, 15, 1, '2010-10-08', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (195, 194, 391, 307, 0, '2013-07-19', '09:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (196, 115, 48, 215, 0, '2012-07-09', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (197, NULL, 439, 460, 1, '2013-01-06', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (198, 241, 461, 463, 1, '2012-11-16', '13:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (199, NULL, 343, 367, 0, '2020-09-19', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (200, 264, 67, 413, 0, '2015-01-22', '09:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (201, NULL, 145, 455, 0, '2015-08-09', '11:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (202, 338, 155, 169, 1, '2024-12-28', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (203, NULL, 68, 168, 1, '2018-05-29', '10:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (204, NULL, 410, 198, 0, '2014-06-10', '10:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (205, 18, 428, 407, 0, '2013-08-19', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (206, 247, 248, 440, 1, '2014-03-19', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (207, NULL, 110, 233, 1, '2022-03-30', '15:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (208, NULL, 336, 394, 1, '2017-07-25', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (209, 447, 250, 396, 1, '2024-11-16', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (210, NULL, 135, 33, 1, '2019-07-27', '08:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (211, 500, 235, 425, 0, '2012-09-12', '16:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (212, 178, 158, 232, 1, '2022-05-30', '09:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (213, 482, 454, 262, 0, '2013-03-06', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (214, 382, 182, 270, 0, '2022-08-17', '16:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (215, NULL, 186, 277, 0, '2021-11-27', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (216, 349, 85, 326, 0, '2013-05-30', '16:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (217, NULL, 143, 26, 1, '2016-08-25', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (218, NULL, 240, 165, 0, '2016-09-23', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (219, 285, 343, 160, 0, '2023-10-02', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (220, 211, 72, 74, 1, '2013-08-05', '11:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (221, NULL, 331, 215, 1, '2023-04-07', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (222, NULL, 37, 116, 1, '2013-02-24', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (223, NULL, 300, 484, 0, '2014-08-14', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (224, NULL, 390, 168, 0, '2024-04-13', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (225, NULL, 396, 322, 1, '2015-03-18', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (226, NULL, 278, 381, 1, '2013-06-12', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (227, NULL, 487, 21, 1, '2015-09-24', '09:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (228, NULL, 87, 449, 1, '2016-07-12', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (229, 375, 309, 492, 1, '2015-05-31', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (230, NULL, 327, 54, 1, '2016-03-09', '12:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (231, NULL, 429, 129, 1, '2011-11-12', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (232, NULL, 249, 125, 1, '2014-12-19', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (233, NULL, 54, 400, 1, '2022-07-30', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (234, NULL, 446, 474, 1, '2010-12-11', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (235, NULL, 407, 330, 0, '2022-11-29', '09:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (236, NULL, 123, 185, 1, '2018-10-31', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (237, NULL, 226, 437, 1, '2022-11-10', '16:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (238, NULL, 417, 413, 1, '2010-07-30', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (239, 485, 169, 51, 1, '2019-03-31', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (240, NULL, 130, 184, 1, '2017-11-26', '11:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (241, NULL, 25, 167, 1, '2024-03-28', '12:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (242, 395, 443, 281, 1, '2019-01-01', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (243, NULL, 439, 46, 1, '2017-11-21', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (244, 157, 52, 469, 0, '2024-05-05', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (245, NULL, 328, 96, 1, '2014-07-15', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (246, 413, 225, 459, 1, '2013-07-28', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (247, 98, 298, 159, 1, '2022-07-23', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (248, 357, 39, 102, 0, '2012-01-12', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (249, NULL, 75, 367, 1, '2021-12-13', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (250, 198, 54, 433, 1, '2023-10-05', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (251, 116, 227, 423, 0, '2015-07-08', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (252, NULL, 141, 14, 1, '2015-01-13', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (253, NULL, 226, 332, 0, '2013-04-05', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (254, 11, 440, 314, 1, '2019-11-05', '14:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (255, NULL, 435, 266, 1, '2024-01-26', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (256, NULL, 362, 408, 1, '2015-11-30', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (257, 474, 480, 121, 1, '2022-02-13', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (258, NULL, 69, 165, 0, '2022-01-27', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (259, 470, 402, 260, 1, '2022-01-03', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (260, NULL, 310, 117, 1, '2024-06-19', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (261, NULL, 295, 429, 0, '2020-04-28', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (262, NULL, 224, 34, 0, '2010-07-01', '16:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (263, NULL, 30, 459, 1, '2020-09-09', '10:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (264, NULL, 34, 489, 1, '2022-10-12', '12:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (265, NULL, 252, 221, 0, '2018-11-21', '11:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (266, 357, 346, 156, 1, '2015-03-21', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (267, 277, 349, 301, 1, '2010-02-25', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (268, NULL, 184, 301, 0, '2011-08-05', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (269, NULL, 374, 83, 0, '2015-08-01', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (270, NULL, 16, 333, 1, '2012-09-05', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (271, 207, 294, 359, 1, '2019-02-21', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (272, 176, 94, 50, 1, '2017-12-19', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (273, NULL, 256, 47, 0, '2015-11-05', '14:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (274, 332, 325, 42, 1, '2020-02-18', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (275, 311, 32, 286, 0, '2018-05-15', '09:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (276, 271, 7, 3, 1, '2018-08-18', '12:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (277, NULL, 291, 289, 1, '2011-07-23', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (278, NULL, 256, 94, 0, '2017-09-29', '09:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (279, NULL, 294, 91, 1, '2013-12-25', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (280, NULL, 228, 16, 0, '2022-01-21', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (281, NULL, 56, 179, 0, '2023-03-28', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (282, NULL, 255, 99, 0, '2023-10-03', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (283, NULL, 281, 426, 1, '2020-01-18', '09:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (284, 188, 73, 123, 1, '2014-03-23', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (285, 470, 472, 246, 0, '2021-08-29', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (286, NULL, 289, 295, 1, '2022-04-03', '11:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (287, 230, 391, 102, 1, '2024-01-18', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (288, NULL, 43, 252, 0, '2021-01-07', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (289, NULL, 313, 200, 1, '2021-02-28', '12:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (290, NULL, 22, 97, 0, '2016-11-20', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (291, NULL, 379, 25, 0, '2011-01-22', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (292, 494, 276, 27, 1, '2021-05-27', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (293, NULL, 349, 358, 0, '2014-10-24', '09:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (294, NULL, 457, 114, 1, '2011-08-21', '11:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (295, 328, 314, 8, 0, '2018-07-23', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (296, NULL, 3, 464, 0, '2024-10-17', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (297, NULL, 424, 117, 1, '2019-01-06', '08:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (298, 127, 319, 343, 1, '2019-06-26', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (299, 450, 335, 378, 1, '2019-03-07', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (300, NULL, 194, 143, 0, '2020-12-13', '12:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (301, NULL, 203, 22, 1, '2012-11-21', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (302, NULL, 60, 82, 1, '2011-06-29', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (303, 379, 132, 490, 1, '2016-05-22', '16:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (304, 292, 134, 56, 0, '2018-11-10', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (305, NULL, 255, 103, 0, '2021-08-16', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (306, NULL, 58, 118, 0, '2018-09-15', '10:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (307, NULL, 413, 35, 0, '2019-10-12', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (308, NULL, 74, 227, 0, '2024-11-13', '16:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (309, NULL, 372, 163, 0, '2022-10-04', '08:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (310, 487, 129, 472, 0, '2017-11-08', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (311, NULL, 29, 201, 1, '2013-06-08', '12:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (312, 322, 100, 172, 1, '2010-07-27', '15:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (313, NULL, 309, 271, 1, '2022-06-28', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (314, NULL, 163, 30, 0, '2011-06-18', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (315, NULL, 87, 371, 1, '2018-04-23', '08:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (316, NULL, 351, 120, 0, '2018-07-20', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (317, NULL, 394, 291, 0, '2015-01-14', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (318, 422, 467, 244, 1, '2016-05-02', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (319, NULL, 384, 122, 1, '2023-09-28', '12:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (320, NULL, 326, 233, 1, '2013-06-08', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (321, 147, 327, 375, 0, '2018-09-18', '12:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (322, 11, 222, 413, 1, '2013-03-25', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (323, NULL, 451, 278, 0, '2019-01-09', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (324, 208, 216, 453, 1, '2020-05-01', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (325, NULL, 238, 187, 1, '2017-04-24', '14:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (326, NULL, 106, 126, 0, '2014-04-14', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (327, NULL, 374, 338, 1, '2020-05-23', '16:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (328, 158, 110, 202, 0, '2020-07-19', '09:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (329, 427, 490, 397, 1, '2011-02-21', '11:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (330, 456, 81, 338, 1, '2021-08-10', '14:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (331, NULL, 13, 356, 0, '2018-08-28', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (332, 382, 349, 289, 0, '2024-05-20', '14:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (333, 163, 240, 126, 0, '2020-11-30', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (334, NULL, 403, 34, 0, '2010-06-25', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (335, 47, 161, 477, 1, '2014-07-22', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (336, 34, 186, 320, 1, '2023-02-01', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (337, 90, 149, 156, 0, '2022-08-08', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (338, 61, 273, 467, 1, '2013-07-20', '16:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (339, NULL, 144, 354, 0, '2012-07-17', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (340, 21, 70, 451, 1, '2020-08-09', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (341, 11, 301, 353, 1, '2019-11-22', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (342, NULL, 11, 497, 1, '2022-09-18', '13:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (343, NULL, 454, 190, 0, '2013-12-22', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (344, NULL, 470, 77, 0, '2014-06-03', '13:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (345, NULL, 486, 403, 0, '2017-12-15', '17:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (346, 457, 303, 214, 0, '2018-03-11', '12:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (347, NULL, 267, 463, 0, '2020-12-24', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (348, 123, 359, 157, 1, '2020-01-26', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (349, 384, 389, 337, 1, '2024-10-15', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (350, NULL, 67, 447, 0, '2022-11-13', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (351, 464, 241, 195, 1, '2010-10-22', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (352, 412, 263, 438, 1, '2019-02-18', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (353, NULL, 369, 134, 0, '2020-12-18', '12:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (354, 231, 471, 344, 0, '2024-12-10', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (355, 66, 413, 391, 0, '2015-06-14', '09:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (356, 79, 293, 411, 0, '2011-12-17', '09:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (357, NULL, 378, 414, 1, '2023-11-07', '09:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (358, NULL, 495, 447, 1, '2024-02-26', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (359, NULL, 29, 361, 0, '2014-06-23', '09:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (360, 488, 47, 2, 1, '2015-03-25', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (361, NULL, 199, 165, 0, '2020-09-04', '11:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (362, NULL, 96, 241, 1, '2023-04-11', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (363, 4, 41, 91, 0, '2015-11-27', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (364, NULL, 360, 390, 0, '2014-03-22', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (365, NULL, 117, 84, 1, '2024-04-01', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (366, NULL, 260, 328, 1, '2014-11-23', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (367, NULL, 377, 124, 0, '2024-09-08', '12:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (368, NULL, 34, 32, 0, '2021-01-29', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (369, NULL, 419, 221, 0, '2020-01-02', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (370, 395, 470, 469, 1, '2023-08-01', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (371, NULL, 164, 231, 1, '2020-10-10', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (372, 251, 161, 280, 0, '2015-02-12', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (373, 181, 210, 239, 1, '2017-04-11', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (374, NULL, 238, 232, 0, '2013-03-09', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (375, NULL, 448, 72, 1, '2018-07-22', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (376, 223, 406, 419, 0, '2013-05-22', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (377, 9, 201, 242, 0, '2016-01-29', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (378, 201, 82, 156, 1, '2015-02-09', '11:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (379, NULL, 256, 222, 1, '2013-08-02', '15:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (380, 55, 35, 488, 1, '2020-09-10', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (381, 266, 483, 254, 0, '2019-05-04', '15:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (382, NULL, 324, 82, 1, '2024-02-21', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (383, NULL, 307, 67, 1, '2017-08-26', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (384, 497, 243, 33, 0, '2020-01-11', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (385, 484, 168, 353, 0, '2017-01-04', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (386, NULL, 296, 407, 1, '2014-05-12', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (387, NULL, 294, 498, 0, '2023-04-19', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (388, NULL, 128, 251, 1, '2010-06-08', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (389, 76, 320, 165, 0, '2021-11-14', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (390, NULL, 457, 485, 1, '2011-07-03', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (391, NULL, 406, 395, 1, '2013-03-18', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (392, NULL, 115, 325, 0, '2017-05-04', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (393, NULL, 402, 140, 1, '2020-11-14', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (394, NULL, 331, 97, 0, '2016-08-18', '08:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (395, NULL, 259, 145, 0, '2018-06-08', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (396, 105, 74, 152, 0, '2010-08-25', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (397, 398, 466, 76, 1, '2024-01-15', '14:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (398, NULL, 389, 161, 0, '2016-02-19', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (399, 311, 233, 146, 0, '2023-02-26', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (400, NULL, 64, 27, 1, '2022-05-24', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (401, 426, 369, 193, 0, '2024-02-08', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (402, 168, 314, 429, 0, '2024-06-08', '12:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (403, NULL, 292, 21, 0, '2012-12-16', '15:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (404, NULL, 72, 78, 0, '2021-09-22', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (405, 185, 498, 183, 1, '2011-10-27', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (406, NULL, 253, 206, 0, '2021-10-08', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (407, NULL, 281, 422, 0, '2014-08-25', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (408, 467, 445, 134, 0, '2015-05-15', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (409, 432, 358, 116, 1, '2010-12-14', '08:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (410, NULL, 487, 79, 0, '2021-03-24', '13:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (411, 325, 344, 203, 0, '2021-06-11', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (412, 366, 357, 213, 0, '2010-11-25', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (413, 299, 252, 4, 1, '2011-10-23', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (414, NULL, 425, 85, 1, '2014-10-10', '10:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (415, NULL, 382, 319, 1, '2015-12-17', '16:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (416, NULL, 82, 428, 0, '2023-08-18', '12:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (417, 460, 134, 202, 0, '2024-08-03', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (418, 309, 496, 334, 1, '2014-08-04', '10:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (419, 412, 55, 381, 0, '2014-06-28', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (420, NULL, 346, 110, 1, '2018-02-04', '15:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (421, NULL, 118, 291, 1, '2014-11-12', '16:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (422, 111, 425, 93, 1, '2014-08-18', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (423, NULL, 235, 201, 0, '2021-01-10', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (424, NULL, 342, 439, 0, '2011-09-29', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (425, NULL, 437, 16, 0, '2010-04-02', '12:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (426, 196, 374, 291, 0, '2012-03-07', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (427, 98, 498, 217, 1, '2011-09-16', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (428, NULL, 153, 395, 0, '2012-09-10', '12:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (429, 477, 478, 455, 0, '2012-09-12', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (430, 58, 45, 372, 0, '2020-03-18', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (431, 360, 289, 246, 0, '2013-06-09', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (432, 194, 16, 20, 1, '2019-09-13', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (433, 7, 296, 460, 0, '2024-09-22', '09:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (434, NULL, 369, 246, 0, '2015-12-30', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (435, NULL, 97, 121, 1, '2010-01-16', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (436, NULL, 360, 251, 0, '2011-01-23', '12:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (437, 189, 234, 421, 1, '2022-03-20', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (438, NULL, 191, 372, 0, '2017-03-12', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (439, 206, 191, 240, 1, '2016-07-23', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (440, NULL, 209, 185, 1, '2011-12-10', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (441, NULL, 171, 474, 1, '2024-06-23', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (442, NULL, 442, 349, 0, '2010-12-17', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (443, NULL, 277, 324, 0, '2022-11-13', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (444, NULL, 203, 42, 1, '2012-07-05', '16:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (445, NULL, 295, 3, 1, '2022-05-07', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (446, NULL, 404, 172, 1, '2012-08-15', '13:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (447, NULL, 203, 268, 1, '2014-11-30', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (448, NULL, 353, 385, 0, '2015-01-24', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (449, NULL, 459, 386, 0, '2010-01-05', '16:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (450, NULL, 469, 37, 1, '2015-06-05', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (451, NULL, 278, 327, 0, '2014-04-14', '08:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (452, 62, 107, 96, 0, '2011-07-04', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (453, NULL, 217, 484, 1, '2024-11-02', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (454, NULL, 154, 176, 1, '2018-05-30', '11:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (455, NULL, 302, 471, 1, '2024-03-31', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (456, NULL, 17, 256, 1, '2017-11-19', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (457, NULL, 441, 409, 1, '2022-02-02', '09:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (458, NULL, 318, 451, 1, '2020-12-30', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (459, 250, 389, 464, 0, '2020-08-26', '12:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (460, 371, 426, 367, 0, '2020-03-13', '14:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (461, 241, 18, 166, 1, '2022-05-25', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (462, NULL, 49, 6, 0, '2023-04-24', '08:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (463, 93, 238, 141, 1, '2022-01-06', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (464, NULL, 358, 265, 1, '2013-11-25', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (465, NULL, 21, 149, 1, '2019-07-28', '09:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (466, NULL, 40, 102, 1, '2020-11-27', '11:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (467, 382, 414, 335, 0, '2018-06-14', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (468, 175, 444, 350, 1, '2015-02-17', '15:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (469, 72, 68, 380, 0, '2019-10-29', '15:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (470, NULL, 221, 11, 1, '2024-03-28', '16:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (471, NULL, 18, 143, 1, '2022-07-02', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (472, 135, 450, 486, 1, '2020-08-24', '14:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (473, NULL, 449, 71, 0, '2010-07-17', '10:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (474, NULL, 341, 101, 1, '2024-10-19', '16:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (475, NULL, 245, 35, 0, '2023-01-21', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (476, NULL, 119, 104, 0, '2016-09-26', '10:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (477, 31, 262, 404, 0, '2012-07-12', '16:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (478, NULL, 5, 156, 0, '2017-03-02', '11:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (479, NULL, 97, 340, 1, '2020-09-23', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (480, 199, 284, 325, 0, '2013-04-11', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (481, NULL, 35, 245, 0, '2022-09-12', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (482, NULL, 212, 430, 1, '2015-01-21', '12:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (483, 222, 22, 446, 1, '2018-11-07', '08:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (484, NULL, 477, 192, 1, '2020-02-02', '17:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (485, NULL, 66, 246, 1, '2024-06-28', '10:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (486, NULL, 148, 255, 0, '2019-09-16', '17:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (487, NULL, 288, 44, 0, '2024-05-21', '08:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (488, 144, 238, 333, 1, '2016-10-22', '16:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (489, NULL, 438, 486, 1, '2021-06-21', '15:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (490, NULL, 430, 353, 0, '2020-07-11', '13:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (491, NULL, 500, 176, 0, '2015-08-24', '12:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (492, NULL, 305, 263, 0, '2017-01-08', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (493, NULL, 179, 498, 1, '2014-04-21', '13:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (494, 307, 218, 343, 0, '2023-10-02', '10:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (495, 352, 186, 365, 1, '2014-08-02', '15:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (496, 371, 449, 150, 0, '2014-08-13', '17:30:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (497, 332, 415, 255, 1, '2015-07-06', '14:45:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (498, NULL, 478, 291, 1, '2022-01-20', '13:15:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (499, 37, 130, 64, 1, '2022-05-09', '14:00:00');
INSERT INTO RoundScore (ScoreID, CompetitionID, ArcherID, BaseRoundID, IsApproved, Date, Time) VALUES (500, 416, 479, 131, 1, '2020-03-14', '16:30:00');"""

insert_statements.extend(sql_data.strip().splitlines())

# ── Write output ───────────────────────────────────────────────────────────────
output_path = "roundscore_inserts.sql"
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
