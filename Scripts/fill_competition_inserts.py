"""
Archery Score Recording Database — Competition table
Generates and downloads competition_inserts.sql with 500 INSERT statements.
Run in Google Colab: the file will be saved and automatically downloaded.

Table: Competition(CompetitionID, BaseRoundID FK, ClubID FK, ChampionshipID FK, CompetitionDate, CompetitionName)
Assumes BaseRound 1-500, Club 1-500, Championship 1-500 exist.
"""

import random
from datetime import date, timedelta

# ── Data pools ─────────────────────────────────────────────────────────────────
competition_prefixes = [
    "Club", "State", "Regional", "Annual", "Open", "Invitational",
    "Winter", "Summer", "Spring", "Autumn", "Indoor", "Outdoor",
]

round_names_pool = [
    "WA90/1440", "WA70/1440", "WA60/1440", "AA50/1440", "AA40/1440",
    "WA720 Recurve", "WA720 Compound", "WA900",
    "Long Sydney", "Sydney", "Brisbane", "Adelaide", "Hobart", "Perth",
    "Darwin", "Canberra", "Melbourne", "Townsville", "Cairns",
    "WA 18 (Indoor)", "WA 25 (Indoor)",
]

def random_date(start_year=2010, end_year=2024):
    start = date(start_year, 1, 1)
    end   = date(end_year, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

def escape_sql(value):
    return str(value).replace("'", "''")

# ── Pre-generated INSERT statements ───────────────────────────────────────────
insert_statements = []
insert_statements.append("-- INSERT statements for the Competition table")
insert_statements.append("-- 500 rows")
insert_statements.append("")

sql_data = """\
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (1, 262, 143, 233, '2012-06-04', '2012 State Long Adelaide Competition 1');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (2, 251, 255, 483, '2013-01-07', '2013 Club WA720 Compound Competition 2');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (3, 378, 28, NULL, '2021-03-04', '2021 Indoor WA70/1440 Competition 3');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (4, 498, 92, NULL, '2017-05-02', '2017 Regional Short Hobart Competition 4');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (5, 319, 320, 40, '2024-10-29', '2024 Spring Junior WA 60 Competition 5');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (6, 253, 406, NULL, '2016-08-01', '2016 Indoor WA 25 (Indoor) Competition 6');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (7, 252, 259, 176, '2022-02-15', '2022 Spring WA70/1440 Competition 7');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (8, 488, 392, 221, '2012-09-02', '2012 Winter Townsville Competition 8');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (9, 162, 437, NULL, '2020-04-23', '2020 Club WA60/1440 Competition 9');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (10, 91, 286, NULL, '2016-10-18', '2016 Outdoor Short Sydney Competition 10');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (11, 252, 221, 367, '2018-09-23', '2018 Summer Junior WA 70 Competition 11');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (12, 57, 292, NULL, '2024-10-21', '2024 Spring National Competition 12');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (13, 277, 293, NULL, '2022-08-11', '2022 Regional Bray I Competition 13');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (14, 29, 201, 303, '2018-06-22', '2018 Autumn National Competition 14');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (15, 181, 393, NULL, '2017-03-10', '2017 Club WA70/1440 Competition 15');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (16, 303, 24, 188, '2017-10-28', '2017 Outdoor Short Windsor Competition 16');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (17, 14, 392, NULL, '2017-08-27', '2017 Winter WA720 Compound Competition 17');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (18, 220, 177, NULL, '2019-03-29', '2019 Invitational AA50/1440 Competition 18');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (19, 339, 126, 332, '2016-12-31', '2016 Autumn WA720 Recurve Competition 19');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (20, 467, 353, 157, '2012-07-26', '2012 Invitational Short Sydney Competition 20');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (21, 11, 276, NULL, '2020-05-03', '2020 Indoor Short Melbourne Competition 21');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (22, 291, 264, NULL, '2015-12-25', '2015 Club Western Competition 22');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (23, 241, 302, 163, '2018-06-22', '2018 Autumn Canberra Competition 23');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (24, 166, 294, 251, '2012-03-30', '2012 Outdoor National Competition 24');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (25, 106, 173, NULL, '2024-12-20', '2024 Invitational Short Sydney Competition 25');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (26, 315, 154, NULL, '2019-10-12', '2019 Annual WA 25 (Indoor) Competition 26');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (27, 326, 434, NULL, '2011-09-10', '2011 Spring Short Brisbane Competition 27');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (28, 148, 136, 294, '2019-01-07', '2019 Annual Albion Competition 28');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (29, 381, 491, 433, '2022-12-20', '2022 State Short Windsor Competition 29');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (30, 173, 140, 411, '2021-11-29', '2021 Summer Short Melbourne Competition 30');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (31, 108, 178, NULL, '2024-08-12', '2024 Open Bray I Competition 31');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (32, 412, 154, NULL, '2022-02-10', '2022 Invitational Brisbane Competition 32');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (33, 213, 206, 264, '2020-03-01', '2020 Indoor Junior WA 70 Competition 33');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (34, 281, 93, NULL, '2024-01-31', '2024 Outdoor Bray II Competition 34');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (35, 442, 96, NULL, '2014-10-11', '2014 Indoor New National Competition 35');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (36, 481, 240, 327, '2021-12-13', '2021 Autumn Junior WA 60 Competition 36');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (37, 465, 223, NULL, '2024-01-22', '2024 Club Bray II Competition 37');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (38, 103, 187, NULL, '2015-05-24', '2015 Regional New National Competition 38');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (39, 351, 392, NULL, '2019-10-07', '2019 Winter Long Perth Competition 39');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (40, 441, 426, NULL, '2024-03-21', '2024 Annual Melbourne Competition 40');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (41, 137, 422, 83, '2015-10-02', '2015 Indoor Long Windsor Competition 41');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (42, 121, 208, 77, '2014-04-22', '2014 Club Short Adelaide Competition 42');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (43, 409, 424, NULL, '2020-11-20', '2020 Spring Short Melbourne Competition 43');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (44, 217, 332, NULL, '2014-07-13', '2014 Regional Long Hobart Competition 44');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (45, 70, 15, 412, '2016-03-25', '2016 Indoor Single Clout Competition 45');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (46, 91, 330, NULL, '2020-11-24', '2020 Club AA50/1440 Competition 46');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (47, 441, 460, 309, '2016-09-07', '2016 State Melbourne Competition 47');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (48, 460, 187, NULL, '2012-01-10', '2012 Winter New Western Competition 48');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (49, 432, 72, 293, '2021-03-22', '2021 State Bray II Competition 49');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (50, 341, 425, NULL, '2021-10-12', '2021 Open WA 25 (Indoor) Competition 50');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (51, 453, 47, 63, '2017-01-11', '2017 Invitational Short Windsor Competition 51');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (52, 378, 200, NULL, '2015-04-17', '2015 Winter Short Brisbane Competition 52');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (53, 74, 55, 497, '2016-02-28', '2016 Summer Melbourne Competition 53');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (54, 131, 442, NULL, '2020-12-31', '2020 Spring Darwin Competition 54');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (55, 359, 486, 280, '2019-07-04', '2019 Summer National Competition 55');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (56, 127, 494, 402, '2013-04-02', '2013 Invitational WA 18 (Indoor) Competition 56');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (57, 367, 189, NULL, '2010-06-22', '2010 Indoor Long Windsor Competition 57');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (58, 18, 431, NULL, '2011-03-24', '2011 Outdoor St Nicholas Competition 58');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (59, 123, 130, NULL, '2016-12-08', '2016 Indoor Western Competition 59');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (60, 186, 463, NULL, '2012-09-26', '2012 Spring Short Adelaide Competition 60');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (61, 440, 227, NULL, '2018-10-25', '2018 Open Short Hobart Competition 61');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (62, 47, 480, NULL, '2015-04-13', '2015 Open Short Brisbane Competition 62');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (63, 441, 456, 225, '2024-02-29', '2024 Invitational Junior WA 60 Competition 63');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (64, 330, 209, NULL, '2016-02-23', '2016 State Junior WA 60 Competition 64');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (65, 482, 252, NULL, '2019-04-06', '2019 Invitational Eastern Competition 65');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (66, 217, 449, NULL, '2012-04-02', '2012 Regional Western Competition 66');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (67, 134, 260, 216, '2023-07-04', '2023 Outdoor Single Clout Competition 67');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (68, 378, 168, NULL, '2010-08-13', '2010 Club Hereford Competition 68');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (69, 329, 95, NULL, '2024-05-18', '2024 Regional WA90/1440 Competition 69');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (70, 206, 103, NULL, '2017-01-14', '2017 Autumn WA720 Recurve Competition 70');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (71, 57, 81, 366, '2024-07-24', '2024 Regional Long Windsor Competition 71');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (72, 352, 211, NULL, '2017-03-01', '2017 Summer WA 18 (Indoor) Competition 72');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (73, 448, 377, 89, '2023-04-21', '2023 Invitational Hobart Competition 73');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (74, 102, 44, NULL, '2014-01-30', '2014 Winter Canberra Competition 74');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (75, 484, 428, NULL, '2015-01-13', '2015 Club WA70/1440 Competition 75');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (76, 473, 286, NULL, '2024-01-21', '2024 Annual WA720 Recurve Competition 76');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (77, 499, 237, 360, '2013-10-14', '2013 Club Long Melbourne Competition 77');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (78, 317, 220, NULL, '2013-05-07', '2013 State Darwin Competition 78');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (79, 88, 485, NULL, '2010-04-26', '2010 Outdoor Bray II Competition 79');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (80, 223, 396, NULL, '2020-03-05', '2020 Indoor WA 25 (Indoor) Competition 80');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (81, 61, 115, NULL, '2014-04-10', '2014 Open Hobart Competition 81');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (82, 383, 254, NULL, '2019-09-04', '2019 Annual Long Windsor Competition 82');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (83, 111, 422, 347, '2014-04-01', '2014 Winter Long Brisbane Competition 83');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (84, 210, 406, 149, '2015-11-15', '2015 Annual Albion Competition 84');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (85, 231, 465, 299, '2024-07-08', '2024 Summer WA720 Recurve Competition 85');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (86, 6, 241, 166, '2018-12-01', '2018 Indoor Short Brisbane Competition 86');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (87, 366, 197, NULL, '2023-05-25', '2023 Open AA40/1440 Competition 87');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (88, 49, 286, 171, '2015-04-08', '2015 Summer Short Perth Competition 88');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (89, 311, 481, NULL, '2023-06-02', '2023 Outdoor New National Competition 89');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (90, 415, 24, 259, '2023-11-25', '2023 Winter Short Hobart Competition 90');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (91, 203, 344, NULL, '2022-07-20', '2022 Club Short Windsor Competition 91');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (92, 92, 134, 253, '2017-08-10', '2017 Summer Long Sydney Competition 92');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (93, 46, 163, NULL, '2019-09-17', '2019 Regional Long Adelaide Competition 93');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (94, 60, 161, 66, '2021-03-13', '2021 Open New National Competition 94');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (95, 185, 475, NULL, '2015-11-27', '2015 Autumn Junior WA 70 Competition 95');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (96, 475, 136, NULL, '2019-10-10', '2019 Regional Long Perth Competition 96');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (97, 378, 252, NULL, '2013-05-24', '2013 Spring St Nicholas Competition 97');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (98, 326, 409, NULL, '2014-03-28', '2014 Regional AA50/1440 Competition 98');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (99, 118, 94, 134, '2013-09-01', '2013 Outdoor Cairns Competition 99');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (100, 224, 60, NULL, '2021-02-06', '2021 Club Townsville Competition 100');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (101, 183, 364, NULL, '2020-04-07', '2020 Summer WA900 Competition 101');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (102, 434, 369, NULL, '2012-10-09', '2012 Invitational WA720 Recurve Competition 102');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (103, 105, 445, 428, '2013-10-10', '2013 Outdoor Bray I Competition 103');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (104, 422, 140, NULL, '2024-11-15', '2024 Autumn Short Brisbane Competition 104');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (105, 299, 498, 393, '2022-10-20', '2022 Regional Melbourne Competition 105');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (106, 472, 40, 256, '2012-02-12', '2012 Invitational WA70/1440 Competition 106');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (107, 146, 349, NULL, '2012-09-26', '2012 Winter Darwin Competition 107');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (108, 303, 476, NULL, '2017-04-04', '2017 Regional WA70/1440 Competition 108');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (109, 42, 236, NULL, '2024-10-16', '2024 Summer Cairns Competition 109');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (110, 322, 490, 337, '2010-02-17', '2010 Invitational WA60/1440 Competition 110');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (111, 336, 319, NULL, '2017-04-15', '2017 Outdoor New Western Competition 111');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (112, 465, 491, NULL, '2012-11-25', '2012 Annual AA50/1440 Competition 112');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (113, 411, 330, 409, '2011-03-31', '2011 Outdoor AA40/1440 Competition 113');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (114, 281, 488, NULL, '2012-01-29', '2012 Winter Long Adelaide Competition 114');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (115, 92, 123, NULL, '2018-12-12', '2018 State WA70/1440 Competition 115');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (116, 437, 107, 400, '2019-01-10', '2019 Open Hereford Competition 116');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (117, 386, 489, NULL, '2012-09-14', '2012 Open WA 25 (Indoor) Competition 117');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (118, 411, 222, NULL, '2016-12-15', '2016 Indoor Long Windsor Competition 118');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (119, 68, 184, NULL, '2018-03-30', '2018 Spring Brisbane Competition 119');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (120, 251, 229, NULL, '2020-09-07', '2020 Open Windsor Competition 120');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (121, 308, 217, 217, '2018-04-05', '2018 Autumn Long Brisbane Competition 121');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (122, 223, 323, NULL, '2010-11-28', '2010 Spring Perth Competition 122');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (123, 499, 238, NULL, '2024-07-11', '2024 Indoor Eastern Competition 123');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (124, 80, 477, NULL, '2024-02-14', '2024 Indoor Bray II Competition 124');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (125, 43, 149, NULL, '2011-10-11', '2011 Summer Short Hobart Competition 125');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (126, 77, 66, NULL, '2016-09-26', '2016 Annual Bray II Competition 126');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (127, 219, 152, NULL, '2022-05-11', '2022 State WA60/1440 Competition 127');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (128, 263, 56, NULL, '2019-04-07', '2019 State Cairns Competition 128');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (129, 339, 369, NULL, '2015-09-07', '2015 Invitational Long Adelaide Competition 129');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (130, 300, 42, NULL, '2010-05-14', '2010 State New National Competition 130');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (131, 339, 237, 94, '2018-10-25', '2018 Club WA720 Recurve Competition 131');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (132, 214, 449, NULL, '2017-01-15', '2017 Autumn New Western Competition 132');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (133, 233, 388, NULL, '2023-12-29', '2023 Open Perth Competition 133');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (134, 495, 471, NULL, '2014-03-14', '2014 Annual Long Brisbane Competition 134');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (135, 41, 383, NULL, '2015-10-26', '2015 Indoor WA720 Compound Competition 135');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (136, 223, 274, 203, '2012-08-13', '2012 Club Short Sydney Competition 136');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (137, 336, 245, NULL, '2019-02-01', '2019 Indoor New National Competition 137');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (138, 309, 372, NULL, '2023-11-15', '2023 Autumn Darwin Competition 138');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (139, 354, 345, NULL, '2018-11-10', '2018 Open WA720 Recurve Competition 139');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (140, 65, 70, 58, '2010-05-11', '2010 Outdoor Brisbane Competition 140');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (141, 440, 14, 333, '2013-04-04', '2013 Indoor Short Adelaide Competition 141');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (142, 224, 432, NULL, '2022-01-30', '2022 Annual WA720 Recurve Competition 142');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (143, 155, 395, NULL, '2020-08-18', '2020 Winter WA70/1440 Competition 143');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (144, 60, 86, NULL, '2019-12-27', '2019 Summer WA 18 (Indoor) Competition 144');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (145, 11, 441, NULL, '2015-06-11', '2015 Annual Hobart Competition 145');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (146, 292, 425, NULL, '2011-02-22', '2011 Invitational WA90/1440 Competition 146');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (147, 53, 323, NULL, '2019-09-08', '2019 Winter WA 25 (Indoor) Competition 147');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (148, 378, 297, NULL, '2022-06-07', '2022 Open WA60/1440 Competition 148');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (149, 250, 205, NULL, '2023-04-04', '2023 Outdoor Albion Competition 149');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (150, 479, 348, NULL, '2020-12-10', '2020 Annual Eastern Competition 150');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (151, 32, 271, 296, '2017-01-31', '2017 Spring AA40/1440 Competition 151');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (152, 138, 458, NULL, '2020-08-13', '2020 State WA 25 (Indoor) Competition 152');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (153, 319, 481, NULL, '2020-01-21', '2020 Outdoor Short Melbourne Competition 153');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (154, 11, 83, 99, '2020-07-11', '2020 Invitational Townsville Competition 154');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (155, 119, 260, 466, '2017-08-10', '2017 Autumn Eastern Competition 155');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (156, 337, 240, 151, '2018-10-03', '2018 Winter National Competition 156');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (157, 335, 377, NULL, '2020-08-05', '2020 Regional Albion Competition 157');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (158, 107, 145, NULL, '2011-12-08', '2011 Indoor WA 18 (Indoor) Competition 158');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (159, 67, 89, 311, '2021-01-14', '2021 State Melbourne Competition 159');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (160, 483, 253, NULL, '2014-09-12', '2014 Spring AA50/1440 Competition 160');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (161, 10, 184, NULL, '2018-01-03', '2018 Indoor Short Sydney Competition 161');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (162, 90, 424, NULL, '2021-04-17', '2021 Club AA40/1440 Competition 162');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (163, 173, 221, 117, '2012-09-15', '2012 Spring Adelaide Competition 163');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (164, 250, 133, NULL, '2017-12-20', '2017 Club Junior WA 60 Competition 164');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (165, 450, 286, 78, '2021-07-24', '2021 Autumn St Nicholas Competition 165');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (166, 54, 362, 485, '2019-10-27', '2019 Summer Junior WA 70 Competition 166');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (167, 57, 500, 313, '2023-09-04', '2023 State Single Clout Competition 167');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (168, 22, 260, 323, '2012-08-25', '2012 Annual Darwin Competition 168');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (169, 81, 373, 227, '2021-05-07', '2021 Summer New Western Competition 169');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (170, 446, 51, 187, '2017-07-04', '2017 Regional WA900 Competition 170');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (171, 435, 104, NULL, '2019-04-29', '2019 Club Short Adelaide Competition 171');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (172, 428, 415, NULL, '2016-06-07', '2016 Spring Short Sydney Competition 172');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (173, 44, 137, NULL, '2019-04-23', '2019 Invitational York Competition 173');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (174, 341, 126, 386, '2021-11-17', '2021 Winter Adelaide Competition 174');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (175, 71, 411, NULL, '2019-03-08', '2019 Summer Bray II Competition 175');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (176, 407, 350, NULL, '2010-09-01', '2010 Summer Sydney Competition 176');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (177, 395, 6, NULL, '2021-08-09', '2021 State WA720 Recurve Competition 177');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (178, 174, 162, NULL, '2013-09-08', '2013 Winter AA50/1440 Competition 178');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (179, 202, 389, 473, '2024-05-21', '2024 Regional Windsor Competition 179');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (180, 30, 324, NULL, '2024-10-23', '2024 Spring Hobart Competition 180');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (181, 215, 206, NULL, '2022-06-02', '2022 Open New Western Competition 181');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (182, 381, 161, NULL, '2010-03-06', '2010 Open Bray II Competition 182');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (183, 313, 472, 207, '2020-01-04', '2020 Indoor Short Brisbane Competition 183');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (184, 455, 279, NULL, '2023-11-13', '2023 Indoor Townsville Competition 184');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (185, 358, 177, NULL, '2024-07-20', '2024 Winter Junior WA 60 Competition 185');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (186, 102, 452, NULL, '2010-10-30', '2010 Spring Perth Competition 186');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (187, 200, 372, NULL, '2012-10-29', '2012 Spring Double Clout Competition 187');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (188, 146, 110, 283, '2017-01-01', '2017 Spring Perth Competition 188');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (189, 388, 326, 15, '2022-02-10', '2022 Autumn Long Adelaide Competition 189');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (190, 124, 427, NULL, '2019-06-26', '2019 Spring WA900 Competition 190');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (191, 375, 31, NULL, '2015-10-29', '2015 Indoor Bray I Competition 191');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (192, 182, 64, 334, '2012-10-18', '2012 Summer Short Hobart Competition 192');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (193, 294, 378, 174, '2015-04-19', '2015 Outdoor Short Windsor Competition 193');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (194, 290, 366, NULL, '2024-01-30', '2024 Indoor Double Clout Competition 194');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (195, 433, 305, 154, '2016-05-19', '2016 Indoor Eastern Competition 195');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (196, 294, 345, 194, '2021-08-28', '2021 Outdoor Short Adelaide Competition 196');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (197, 54, 168, NULL, '2014-04-27', '2014 Invitational Cairns Competition 197');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (198, 51, 76, NULL, '2019-03-30', '2019 State WA720 Recurve Competition 198');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (199, 32, 218, NULL, '2020-09-06', '2020 Annual Townsville Competition 199');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (200, 40, 190, NULL, '2019-01-13', '2019 Autumn Single Clout Competition 200');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (201, 266, 399, NULL, '2015-12-01', '2015 Autumn WA 25 (Indoor) Competition 201');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (202, 326, 217, NULL, '2020-12-24', '2020 Outdoor Melbourne Competition 202');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (203, 422, 84, 66, '2020-11-15', '2020 Outdoor Cairns Competition 203');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (204, 67, 496, NULL, '2021-11-13', '2021 State Western Competition 204');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (205, 109, 234, NULL, '2013-07-08', '2013 Spring Darwin Competition 205');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (206, 472, 488, 437, '2019-03-02', '2019 State WA900 Competition 206');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (207, 190, 293, 268, '2013-06-09', '2013 State Darwin Competition 207');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (208, 157, 192, NULL, '2020-11-24', '2020 Club Sydney Competition 208');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (209, 73, 402, NULL, '2011-02-03', '2011 Open Hobart Competition 209');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (210, 111, 94, NULL, '2020-12-18', '2020 Club WA900 Competition 210');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (211, 281, 179, 23, '2019-05-14', '2019 Summer Windsor Competition 211');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (212, 159, 290, NULL, '2017-07-30', '2017 Winter WA 18 (Indoor) Competition 212');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (213, 428, 369, NULL, '2012-12-23', '2012 Regional Bray I Competition 213');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (214, 326, 236, NULL, '2024-12-18', '2024 Summer Sydney Competition 214');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (215, 444, 373, NULL, '2024-01-06', '2024 Indoor Albion Competition 215');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (216, 210, 199, 203, '2017-08-09', '2017 Spring WA60/1440 Competition 216');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (217, 491, 344, NULL, '2016-03-22', '2016 Indoor WA720 Recurve Competition 217');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (218, 444, 85, NULL, '2022-10-30', '2022 Indoor Junior WA 60 Competition 218');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (219, 363, 159, NULL, '2012-10-11', '2012 Indoor Single Clout Competition 219');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (220, 44, 99, NULL, '2022-02-25', '2022 Autumn Junior WA 70 Competition 220');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (221, 28, 491, NULL, '2014-04-01', '2014 Summer Bray I Competition 221');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (222, 460, 10, 480, '2021-12-05', '2021 Regional WA70/1440 Competition 222');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (223, 141, 403, 425, '2022-12-31', '2022 Summer WA720 Recurve Competition 223');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (224, 414, 274, NULL, '2019-01-05', '2019 Autumn WA60/1440 Competition 224');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (225, 252, 442, NULL, '2017-08-16', '2017 Winter Long Brisbane Competition 225');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (226, 213, 13, NULL, '2017-02-12', '2017 Winter Long Adelaide Competition 226');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (227, 47, 59, NULL, '2022-02-25', '2022 Regional Hobart Competition 227');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (228, 74, 94, 46, '2013-06-17', '2013 Open Melbourne Competition 228');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (229, 348, 87, 493, '2017-04-18', '2017 Regional WA70/1440 Competition 229');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (230, 366, 30, 51, '2017-03-06', '2017 Regional Melbourne Competition 230');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (231, 458, 166, 483, '2012-09-17', '2012 Club Brisbane Competition 231');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (232, 123, 386, NULL, '2015-04-22', '2015 Summer Bray I Competition 232');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (233, 386, 259, NULL, '2012-07-31', '2012 Open AA50/1440 Competition 233');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (234, 163, 238, NULL, '2011-06-21', '2011 Summer WA70/1440 Competition 234');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (235, 209, 325, 454, '2010-06-02', '2010 Open Single Clout Competition 235');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (236, 494, 301, NULL, '2015-07-11', '2015 Spring Hereford Competition 236');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (237, 403, 65, NULL, '2019-02-15', '2019 Summer WA720 Recurve Competition 237');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (238, 434, 326, NULL, '2013-03-12', '2013 Invitational Double Clout Competition 238');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (239, 87, 401, 488, '2019-07-04', '2019 Spring Townsville Competition 239');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (240, 22, 1, NULL, '2023-12-04', '2023 Open Hereford Competition 240');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (241, 498, 86, 478, '2020-10-25', '2020 Open Long Windsor Competition 241');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (242, 129, 430, NULL, '2017-11-18', '2017 Indoor Short Brisbane Competition 242');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (243, 300, 431, NULL, '2011-01-08', '2011 Regional New National Competition 243');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (244, 274, 289, 46, '2018-11-13', '2018 Outdoor WA900 Competition 244');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (245, 426, 72, NULL, '2016-04-08', '2016 Winter Short Brisbane Competition 245');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (246, 313, 259, NULL, '2017-02-20', '2017 Indoor Perth Competition 246');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (247, 326, 134, NULL, '2020-02-26', '2020 Open Short Adelaide Competition 247');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (248, 340, 165, NULL, '2020-04-24', '2020 Autumn Perth Competition 248');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (249, 9, 468, NULL, '2024-07-01', '2024 Club Long Windsor Competition 249');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (250, 244, 3, NULL, '2013-11-22', '2013 Winter Single Clout Competition 250');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (251, 459, 357, NULL, '2018-10-23', '2018 Spring WA720 Recurve Competition 251');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (252, 404, 449, NULL, '2011-09-28', '2011 Spring WA70/1440 Competition 252');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (253, 457, 427, NULL, '2019-12-26', '2019 Indoor WA900 Competition 253');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (254, 181, 498, NULL, '2023-06-27', '2023 Invitational Canberra Competition 254');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (255, 91, 430, NULL, '2010-03-11', '2010 State Cairns Competition 255');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (256, 190, 480, 5, '2014-12-20', '2014 Outdoor WA70/1440 Competition 256');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (257, 389, 144, NULL, '2018-01-10', '2018 Annual WA720 Recurve Competition 257');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (258, 418, 315, NULL, '2014-12-17', '2014 Annual WA 25 (Indoor) Competition 258');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (259, 496, 186, 253, '2023-08-05', '2023 Annual WA90/1440 Competition 259');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (260, 101, 421, NULL, '2012-06-27', '2012 Open Windsor Competition 260');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (261, 257, 253, 100, '2024-10-19', '2024 Outdoor Windsor Competition 261');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (262, 345, 350, NULL, '2013-12-08', '2013 State Short Windsor Competition 262');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (263, 66, 382, 133, '2022-10-13', '2022 Annual Bray II Competition 263');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (264, 374, 401, 435, '2010-07-09', '2010 Outdoor National Competition 264');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (265, 273, 315, 287, '2020-03-07', '2020 Club Short Melbourne Competition 265');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (266, 329, 345, NULL, '2011-03-01', '2011 Invitational Short Melbourne Competition 266');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (267, 433, 209, 349, '2021-08-16', '2021 Summer WA 25 (Indoor) Competition 267');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (268, 186, 265, NULL, '2015-01-14', '2015 Club Long Hobart Competition 268');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (269, 471, 216, NULL, '2017-02-03', '2017 Club Long Melbourne Competition 269');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (270, 100, 172, 293, '2010-07-27', '2010 Outdoor Adelaide Competition 270');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (271, 354, 217, NULL, '2015-08-10', '2015 Annual Short Sydney Competition 271');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (272, 169, 160, 321, '2012-03-03', '2012 Club WA 18 (Indoor) Competition 272');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (273, 222, 414, 409, '2024-01-18', '2024 Invitational Long Adelaide Competition 273');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (274, 127, 56, NULL, '2017-08-23', '2017 Club Perth Competition 274');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (275, 267, 407, 38, '2023-06-16', '2023 Autumn Townsville Competition 275');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (276, 392, 49, NULL, '2022-12-26', '2022 State WA720 Recurve Competition 276');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (277, 499, 32, NULL, '2018-06-19', '2018 Invitational Western Competition 277');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (278, 34, 401, 471, '2019-11-30', '2019 Club Short Hobart Competition 278');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (279, 313, 321, NULL, '2012-04-14', '2012 Indoor AA50/1440 Competition 279');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (280, 287, 27, 196, '2019-01-04', '2019 State Albion Competition 280');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (281, 386, 211, 307, '2024-10-18', '2024 Autumn WA90/1440 Competition 281');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (282, 233, 197, NULL, '2019-08-09', '2019 Autumn Albion Competition 282');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (283, 52, 174, NULL, '2010-08-01', '2010 Summer Bray II Competition 283');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (284, 169, 301, 53, '2010-04-11', '2010 Autumn Eastern Competition 284');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (285, 35, 304, NULL, '2014-05-06', '2014 Autumn Long Sydney Competition 285');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (286, 327, 261, 216, '2020-10-18', '2020 Outdoor Albion Competition 286');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (287, 228, 96, 409, '2010-12-28', '2010 Club Long Sydney Competition 287');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (288, 160, 300, NULL, '2024-08-13', '2024 Invitational Short Hobart Competition 288');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (289, 299, 454, NULL, '2013-04-07', '2013 Regional WA 18 (Indoor) Competition 289');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (290, 159, 309, NULL, '2018-04-10', '2018 Club Bray II Competition 290');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (291, 301, 337, NULL, '2011-04-15', '2011 Annual Bray I Competition 291');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (292, 420, 428, NULL, '2011-03-24', '2011 Winter Short Perth Competition 292');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (293, 101, 500, 466, '2014-07-07', '2014 State Perth Competition 293');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (294, 97, 342, NULL, '2020-06-25', '2020 Autumn Western Competition 294');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (295, 170, 437, NULL, '2017-07-12', '2017 Autumn Short Hobart Competition 295');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (296, 215, 169, 233, '2010-12-12', '2010 Summer Adelaide Competition 296');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (297, 472, 2, NULL, '2015-03-02', '2015 Summer Albion Competition 297');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (298, 110, 123, NULL, '2017-06-08', '2017 Outdoor Canberra Competition 298');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (299, 106, 205, 4, '2018-02-20', '2018 Club AA40/1440 Competition 299');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (300, 184, 16, NULL, '2013-03-12', '2013 Open Townsville Competition 300');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (301, 100, 324, NULL, '2018-01-27', '2018 Club WA70/1440 Competition 301');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (302, 102, 102, 113, '2015-11-17', '2015 Outdoor Long Brisbane Competition 302');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (303, 174, 434, NULL, '2014-01-02', '2014 Annual WA70/1440 Competition 303');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (304, 91, 432, 52, '2010-06-21', '2010 Indoor Long Sydney Competition 304');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (305, 195, 336, NULL, '2012-06-28', '2012 Invitational Short Brisbane Competition 305');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (306, 157, 234, 415, '2018-05-09', '2018 Indoor Short Sydney Competition 306');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (307, 482, 270, NULL, '2023-12-24', '2023 Winter Eastern Competition 307');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (308, 34, 61, 474, '2012-12-07', '2012 Annual Brisbane Competition 308');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (309, 273, 194, NULL, '2017-02-17', '2017 Autumn Short Melbourne Competition 309');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (310, 326, 126, NULL, '2023-10-26', '2023 Autumn Brisbane Competition 310');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (311, 438, 275, 77, '2017-05-08', '2017 Annual AA50/1440 Competition 311');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (312, 323, 408, 65, '2021-05-26', '2021 Autumn WA 25 (Indoor) Competition 312');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (313, 108, 373, 241, '2024-11-18', '2024 Autumn AA40/1440 Competition 313');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (314, 86, 261, NULL, '2024-06-20', '2024 Spring Darwin Competition 314');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (315, 256, 266, NULL, '2017-03-21', '2017 Outdoor Darwin Competition 315');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (316, 270, 356, NULL, '2021-02-05', '2021 Summer Long Hobart Competition 316');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (317, 298, 206, NULL, '2023-02-05', '2023 Indoor WA60/1440 Competition 317');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (318, 107, 113, NULL, '2020-02-21', '2020 Annual Long Melbourne Competition 318');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (319, 112, 157, NULL, '2018-06-17', '2018 Autumn Short Sydney Competition 319');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (320, 479, 432, NULL, '2022-05-08', '2022 State Long Sydney Competition 320');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (321, 385, 44, 266, '2017-11-20', '2017 Annual Short Windsor Competition 321');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (322, 22, 239, NULL, '2017-07-18', '2017 Winter Townsville Competition 322');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (323, 240, 222, NULL, '2021-02-27', '2021 Invitational Long Hobart Competition 323');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (324, 196, 13, 120, '2015-12-16', '2015 Indoor AA40/1440 Competition 324');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (325, 184, 462, 432, '2021-04-03', '2021 Spring Double Clout Competition 325');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (326, 330, 41, NULL, '2015-02-09', '2015 State WA900 Competition 326');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (327, 37, 185, 103, '2017-06-27', '2017 Annual National Competition 327');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (328, 169, 129, NULL, '2016-02-27', '2016 Annual Eastern Competition 328');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (329, 310, 71, NULL, '2022-03-08', '2022 Open WA90/1440 Competition 329');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (330, 395, 154, 178, '2019-01-22', '2019 Winter Short Windsor Competition 330');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (331, 388, 336, 335, '2021-07-01', '2021 Regional Long Melbourne Competition 331');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (332, 117, 117, NULL, '2014-09-16', '2014 Summer Adelaide Competition 332');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (333, 265, 301, NULL, '2020-07-06', '2020 Outdoor Cairns Competition 333');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (334, 175, 406, 434, '2014-03-19', '2014 Winter Junior WA 60 Competition 334');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (335, 483, 358, NULL, '2019-11-03', '2019 Summer Single Clout Competition 335');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (336, 16, 192, 448, '2012-11-17', '2012 Open New National Competition 336');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (337, 5, 256, NULL, '2017-12-15', '2017 Invitational Adelaide Competition 337');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (338, 215, 218, NULL, '2019-01-18', '2019 Outdoor Double Clout Competition 338');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (339, 154, 167, NULL, '2022-09-24', '2022 Club Long Sydney Competition 339');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (340, 79, 488, NULL, '2022-09-29', '2022 Indoor Long Windsor Competition 340');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (341, 468, 312, NULL, '2018-10-08', '2018 Winter Short Brisbane Competition 341');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (342, 486, 201, 198, '2014-03-23', '2014 Summer WA720 Compound Competition 342');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (343, 169, 292, NULL, '2024-05-01', '2024 Open WA720 Recurve Competition 343');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (344, 88, 54, NULL, '2013-12-26', '2013 Club Western Competition 344');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (345, 309, 251, 102, '2011-07-24', '2011 Winter Hobart Competition 345');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (346, 106, 120, 269, '2011-07-28', '2011 Summer AA50/1440 Competition 346');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (347, 189, 266, 168, '2019-03-20', '2019 Winter Short Sydney Competition 347');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (348, 57, 67, NULL, '2020-09-22', '2020 Outdoor AA40/1440 Competition 348');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (349, 200, 490, NULL, '2014-08-19', '2014 Regional Short Brisbane Competition 349');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (350, 159, 222, NULL, '2024-11-28', '2024 Summer Short Sydney Competition 350');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (351, 310, 295, NULL, '2023-03-06', '2023 Annual Bray I Competition 351');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (352, 367, 351, NULL, '2014-07-11', '2014 Club Sydney Competition 352');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (353, 229, 33, NULL, '2023-07-26', '2023 Annual Bray II Competition 353');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (354, 169, 467, NULL, '2021-01-04', '2021 Summer Cairns Competition 354');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (355, 295, 21, NULL, '2016-06-16', '2016 Indoor Cairns Competition 355');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (356, 178, 359, NULL, '2016-09-02', '2016 Winter Albion Competition 356');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (357, 422, 415, NULL, '2019-04-24', '2019 Annual Long Brisbane Competition 357');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (358, 461, 317, NULL, '2020-04-08', '2020 Winter St Nicholas Competition 358');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (359, 94, 358, NULL, '2018-10-29', '2018 Outdoor WA60/1440 Competition 359');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (360, 123, 454, NULL, '2016-02-21', '2016 Indoor Double Clout Competition 360');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (361, 150, 342, NULL, '2014-11-15', '2014 Summer Melbourne Competition 361');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (362, 391, 284, 189, '2011-09-19', '2011 State Bray I Competition 362');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (363, 393, 400, NULL, '2020-02-12', '2020 Regional Long Adelaide Competition 363');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (364, 107, 260, 14, '2011-08-23', '2011 Indoor Western Competition 364');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (365, 346, 384, NULL, '2017-09-16', '2017 Outdoor Long Melbourne Competition 365');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (366, 439, 100, NULL, '2010-03-29', '2010 Open WA900 Competition 366');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (367, 364, 470, 344, '2020-05-31', '2020 Summer Cairns Competition 367');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (368, 35, 43, NULL, '2015-06-08', '2015 Outdoor Townsville Competition 368');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (369, 72, 242, NULL, '2013-08-14', '2013 Regional WA70/1440 Competition 369');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (370, 311, 52, 64, '2021-12-28', '2021 Outdoor Long Melbourne Competition 370');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (371, 87, 40, NULL, '2010-04-02', '2010 Indoor Long Hobart Competition 371');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (372, 79, 226, NULL, '2014-11-10', '2014 Outdoor WA60/1440 Competition 372');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (373, 458, 346, NULL, '2019-12-01', '2019 Outdoor AA50/1440 Competition 373');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (374, 429, 326, NULL, '2024-05-18', '2024 Indoor Eastern Competition 374');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (375, 338, 460, 354, '2016-11-30', '2016 Summer AA50/1440 Competition 375');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (376, 307, 3, 194, '2014-07-11', '2014 Annual Darwin Competition 376');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (377, 466, 123, 9, '2019-06-17', '2019 Club WA90/1440 Competition 377');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (378, 173, 421, 343, '2011-06-02', '2011 Annual WA720 Compound Competition 378');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (379, 409, 428, NULL, '2013-10-07', '2013 Outdoor Short Sydney Competition 379');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (380, 23, 213, NULL, '2017-05-03', '2017 Invitational Single Clout Competition 380');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (381, 321, 98, NULL, '2022-02-24', '2022 Winter Short Melbourne Competition 381');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (382, 62, 119, 183, '2017-04-03', '2017 Regional WA90/1440 Competition 382');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (383, 206, 335, NULL, '2018-09-24', '2018 Annual Cairns Competition 383');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (384, 113, 34, NULL, '2016-03-31', '2016 Indoor Albion Competition 384');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (385, 189, 23, 112, '2019-03-22', '2019 Open Junior WA 60 Competition 385');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (386, 307, 256, NULL, '2012-04-14', '2012 Outdoor Double Clout Competition 386');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (387, 406, 473, NULL, '2013-11-05', '2013 Open WA720 Compound Competition 387');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (388, 308, 167, NULL, '2018-09-19', '2018 Indoor Junior WA 60 Competition 388');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (389, 356, 69, NULL, '2024-04-01', '2024 Outdoor Long Perth Competition 389');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (390, 436, 342, NULL, '2017-07-08', '2017 Club Long Windsor Competition 390');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (391, 467, 300, NULL, '2021-06-18', '2021 Indoor New National Competition 391');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (392, 120, 258, NULL, '2010-04-19', '2010 Annual WA70/1440 Competition 392');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (393, 316, 389, NULL, '2016-12-05', '2016 Annual New National Competition 393');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (394, 220, 388, 41, '2011-05-06', '2011 Regional Darwin Competition 394');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (395, 256, 152, 193, '2014-08-02', '2014 Indoor WA60/1440 Competition 395');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (396, 122, 473, NULL, '2019-12-15', '2019 Outdoor Perth Competition 396');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (397, 69, 143, NULL, '2010-11-21', '2010 Spring Melbourne Competition 397');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (398, 332, 417, 13, '2015-02-20', '2015 Outdoor Perth Competition 398');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (399, 176, 125, 28, '2024-11-30', '2024 Annual National Competition 399');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (400, 357, 369, 447, '2018-07-23', '2018 Spring Long Perth Competition 400');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (401, 94, 227, NULL, '2011-06-14', '2011 Summer AA40/1440 Competition 401');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (402, 489, 99, 73, '2014-07-31', '2014 Regional WA720 Recurve Competition 402');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (403, 89, 304, NULL, '2014-08-02', '2014 Annual Bray I Competition 403');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (404, 41, 219, NULL, '2016-12-26', '2016 Regional New Western Competition 404');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (405, 102, 126, NULL, '2023-08-04', '2023 Annual Short Hobart Competition 405');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (406, 147, 296, NULL, '2024-04-03', '2024 Annual Long Hobart Competition 406');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (407, 442, 401, NULL, '2018-01-24', '2018 Winter Canberra Competition 407');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (408, 86, 242, NULL, '2021-05-02', '2021 Autumn New National Competition 408');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (409, 222, 390, 489, '2020-10-23', '2020 Club Junior WA 70 Competition 409');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (410, 196, 219, NULL, '2016-09-25', '2016 Autumn Double Clout Competition 410');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (411, 79, 284, NULL, '2015-10-09', '2015 Winter Cairns Competition 411');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (412, 157, 233, 288, '2023-08-05', '2023 Summer AA40/1440 Competition 412');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (413, 171, 70, NULL, '2014-05-23', '2014 Regional Brisbane Competition 413');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (414, 3, 7, NULL, '2018-05-24', '2018 Summer Long Melbourne Competition 414');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (415, 474, 213, NULL, '2018-05-15', '2018 Winter WA 25 (Indoor) Competition 415');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (416, 158, 329, NULL, '2011-08-07', '2011 Winter WA60/1440 Competition 416');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (417, 472, 64, NULL, '2022-09-08', '2022 Regional Brisbane Competition 417');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (418, 391, 224, NULL, '2017-10-26', '2017 Spring Eastern Competition 418');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (419, 251, 326, NULL, '2011-04-18', '2011 Indoor Canberra Competition 419');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (420, 475, 218, NULL, '2015-06-09', '2015 Summer WA60/1440 Competition 420');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (421, 472, 417, NULL, '2010-08-20', '2010 Outdoor St Nicholas Competition 421');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (422, 331, 76, 234, '2013-04-22', '2013 Open Short Adelaide Competition 422');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (423, 309, 297, NULL, '2013-08-15', '2013 Club WA900 Competition 423');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (424, 395, 48, NULL, '2018-08-15', '2018 Winter Eastern Competition 424');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (425, 301, 499, NULL, '2021-08-18', '2021 Annual Short Melbourne Competition 425');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (426, 85, 425, NULL, '2016-10-11', '2016 Spring Double Clout Competition 426');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (427, 338, 454, NULL, '2016-11-27', '2016 Outdoor Melbourne Competition 427');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (428, 386, 449, NULL, '2011-12-30', '2011 State York Competition 428');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (429, 294, 398, NULL, '2013-03-15', '2013 Open New National Competition 429');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (430, 108, 477, NULL, '2016-11-28', '2016 Club Short Sydney Competition 430');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (431, 418, 252, 36, '2019-05-16', '2019 Spring Melbourne Competition 431');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (432, 336, 148, NULL, '2013-10-29', '2013 Regional Darwin Competition 432');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (433, 96, 361, 250, '2014-01-30', '2014 Spring WA900 Competition 433');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (434, 231, 291, NULL, '2014-03-01', '2014 Annual AA50/1440 Competition 434');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (435, 384, 94, NULL, '2014-04-21', '2014 Open Melbourne Competition 435');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (436, 226, 321, NULL, '2012-06-13', '2012 Indoor Short Sydney Competition 436');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (437, 41, 151, 64, '2016-03-17', '2016 State Perth Competition 437');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (438, 16, 300, 249, '2012-04-05', '2012 Club AA50/1440 Competition 438');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (439, 137, 385, NULL, '2024-12-03', '2024 Autumn WA60/1440 Competition 439');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (440, 50, 109, NULL, '2010-03-01', '2010 Winter Long Windsor Competition 440');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (441, 267, 493, NULL, '2020-11-24', '2020 Summer Junior WA 70 Competition 441');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (442, 173, 310, NULL, '2018-04-26', '2018 Indoor Perth Competition 442');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (443, 162, 419, 185, '2024-12-01', '2024 Winter Canberra Competition 443');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (444, 313, 30, NULL, '2017-05-29', '2017 State WA90/1440 Competition 444');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (445, 234, 446, NULL, '2013-02-11', '2013 Club Long Windsor Competition 445');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (446, 63, 445, NULL, '2015-07-30', '2015 Invitational Townsville Competition 446');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (447, 317, 352, NULL, '2020-08-28', '2020 Spring Melbourne Competition 447');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (448, 339, 97, 327, '2017-03-24', '2017 Club York Competition 448');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (449, 185, 448, 414, '2017-04-20', '2017 Indoor Townsville Competition 449');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (450, 120, 311, NULL, '2023-09-28', '2023 State Short Perth Competition 450');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (451, 220, 481, NULL, '2020-09-05', '2020 Indoor Western Competition 451');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (452, 464, 52, NULL, '2016-08-04', '2016 Autumn Brisbane Competition 452');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (453, 365, 74, NULL, '2022-10-29', '2022 Outdoor Bray I Competition 453');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (454, 17, 66, NULL, '2011-12-15', '2011 Open National Competition 454');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (455, 281, 448, NULL, '2020-01-04', '2020 State WA 18 (Indoor) Competition 455');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (456, 340, 277, 109, '2013-10-28', '2013 Indoor Western Competition 456');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (457, 46, 55, NULL, '2010-08-28', '2010 Regional Long Perth Competition 457');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (458, 463, 197, NULL, '2014-12-11', '2014 Outdoor Long Adelaide Competition 458');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (459, 341, 244, NULL, '2012-10-05', '2012 Indoor Long Sydney Competition 459');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (460, 473, 274, NULL, '2021-01-13', '2021 State Western Competition 460');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (461, 171, 447, 295, '2023-06-22', '2023 State Hereford Competition 461');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (462, 176, 194, NULL, '2018-07-24', '2018 Indoor Hereford Competition 462');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (463, 402, 288, NULL, '2019-10-20', '2019 Annual Adelaide Competition 463');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (464, 133, 60, 58, '2012-01-01', '2012 Invitational New National Competition 464');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (465, 304, 480, 483, '2012-08-09', '2012 Autumn Darwin Competition 465');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (466, 66, 437, NULL, '2018-07-12', '2018 Autumn New National Competition 466');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (467, 1, 160, 275, '2014-04-05', '2014 Winter Short Melbourne Competition 467');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (468, 164, 395, NULL, '2012-10-31', '2012 Spring St Nicholas Competition 468');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (469, 309, 303, 203, '2010-03-17', '2010 Spring Cairns Competition 469');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (470, 162, 75, NULL, '2016-08-28', '2016 Annual WA 25 (Indoor) Competition 470');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (471, 349, 234, 146, '2013-04-09', '2013 Outdoor St Nicholas Competition 471');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (472, 435, 411, NULL, '2010-10-09', '2010 Autumn Long Perth Competition 472');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (473, 159, 258, NULL, '2012-10-08', '2012 Open Eastern Competition 473');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (474, 294, 245, NULL, '2014-11-03', '2014 Summer Hobart Competition 474');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (475, 361, 495, NULL, '2017-06-22', '2017 Regional Eastern Competition 475');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (476, 108, 435, NULL, '2015-01-18', '2015 Outdoor New National Competition 476');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (477, 27, 473, NULL, '2014-01-06', '2014 Summer New Western Competition 477');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (478, 201, 154, NULL, '2024-10-14', '2024 Regional WA70/1440 Competition 478');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (479, 281, 201, NULL, '2020-08-14', '2020 Invitational Junior WA 70 Competition 479');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (480, 201, 201, 373, '2016-05-07', '2016 Open Western Competition 480');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (481, 473, 100, NULL, '2022-04-17', '2022 Winter WA720 Compound Competition 481');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (482, 68, 166, NULL, '2023-01-07', '2023 Club Eastern Competition 482');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (483, 156, 235, NULL, '2022-12-12', '2022 Regional Townsville Competition 483');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (484, 357, 248, 75, '2014-09-15', '2014 Annual New National Competition 484');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (485, 101, 377, NULL, '2018-02-15', '2018 Outdoor Windsor Competition 485');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (486, 53, 348, NULL, '2013-04-24', '2013 Winter Short Melbourne Competition 486');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (487, 348, 431, 29, '2012-02-26', '2012 Invitational WA 18 (Indoor) Competition 487');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (488, 92, 484, 264, '2024-07-31', '2024 Invitational Short Windsor Competition 488');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (489, 223, 497, 370, '2019-01-23', '2019 Annual WA60/1440 Competition 489');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (490, 61, 124, NULL, '2016-10-15', '2016 Outdoor Long Windsor Competition 490');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (491, 489, 89, NULL, '2018-06-03', '2018 Outdoor St Nicholas Competition 491');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (492, 338, 46, NULL, '2024-08-02', '2024 Winter Long Hobart Competition 492');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (493, 324, 335, NULL, '2010-04-06', '2010 State WA900 Competition 493');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (494, 43, 63, NULL, '2024-12-31', '2024 Spring Adelaide Competition 494');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (495, 12, 301, NULL, '2022-11-04', '2022 Summer Long Hobart Competition 495');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (496, 356, 382, 304, '2014-01-23', '2014 Winter WA 18 (Indoor) Competition 496');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (497, 331, 360, NULL, '2022-10-26', '2022 Regional WA720 Compound Competition 497');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (498, 167, 33, NULL, '2022-01-21', '2022 Regional Long Melbourne Competition 498');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (499, 417, 359, 285, '2022-01-12', '2022 Spring WA 25 (Indoor) Competition 499');
INSERT INTO Competition (CompetitionID, BaseRoundID, ClubID, ChampionshipID, CompetitionDate, CompetitionName) VALUES (500, 33, 266, NULL, '2022-02-02', '2022 Outdoor Hereford Competition 500');"""

insert_statements.extend(sql_data.strip().splitlines())

# ── Write output ───────────────────────────────────────────────────────────────
output_path = "competition_inserts.sql"
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
