"""
Archery Score Recording Database — Archer table
Generates and downloads archer_inserts.sql with 500 INSERT statements.
Run in Google Colab: the file will be saved and automatically downloaded.

Table: Archer(ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID FK, ClubID FK)
Assumes EquipmentType rows 1-5 and Club rows 1-500 already exist.
"""

import random
from datetime import date, timedelta

# ── Data pools ─────────────────────────────────────────────────────────────────
first_names_male = [
    "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph",
    "Thomas", "Charles", "Christopher", "Daniel", "Matthew", "Anthony", "Mark",
    "Donald", "Steven", "Paul", "Andrew", "Joshua", "Kenneth", "Kevin", "Brian",
    "George", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob",
    "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott",
    "Brandon", "Frank", "Benjamin", "Gregory", "Samuel", "Raymond", "Patrick",
    "Alexander", "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Henry", "Adam",
    "Douglas", "Nathan", "Peter", "Zachary", "Kyle", "Walter", "Harold", "Ethan",
    "Carl", "Keith", "Roger", "Gerald", "Christian", "Terry", "Sean", "Arthur",
]

first_names_female = [
    "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan",
    "Jessica", "Sarah", "Karen", "Lisa", "Nancy", "Betty", "Sandra", "Margaret",
    "Ashley", "Kimberly", "Emily", "Donna", "Michelle", "Carol", "Amanda", "Melissa",
    "Deborah", "Stephanie", "Dorothy", "Rebecca", "Sharon", "Laura", "Cynthia",
    "Amy", "Kathleen", "Angela", "Shirley", "Brenda", "Emma", "Anna", "Pamela",
    "Nicole", "Samantha", "Katherine", "Christine", "Helen", "Debra", "Rachel",
    "Carolyn", "Janet", "Maria", "Catherine", "Heather", "Diane", "Olivia",
    "Julie", "Joyce", "Victoria", "Ruth", "Virginia", "Lauren", "Kelly", "Christina",
    "Joan", "Evelyn", "Judith", "Andrea", "Hannah", "Megan", "Cheryl", "Jacqueline",
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker",
    "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy",
    "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey",
    "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson",
    "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
]

def random_date(start_year=1950, end_year=2010):
    """Generate a random date of birth between two years."""
    start = date(start_year, 1, 1)
    end   = date(end_year, 12, 31)
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, delta))

def escape_sql(value):
    """Escape single quotes in SQL strings."""
    return str(value).replace("'", "''")

# ── Pre-generated INSERT statements ───────────────────────────────────────────
insert_statements = []
insert_statements.append("-- INSERT statements for the Archer table")
insert_statements.append("-- 500 rows")
insert_statements.append("")

sql_data = """\
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (1, 'Evelyn', 'Anderson', 'Female', '1955-11-12', NULL, 38);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (2, 'Joshua', 'Reed', 'Male', '1977-04-05', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (3, 'Christian', 'Carter', 'Male', '1990-06-02', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (4, 'Jessica', 'Ward', 'Female', '1958-11-26', 2, 136);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (5, 'Jacob', 'Thompson', 'Male', '1999-07-10', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (6, 'Joan', 'Nguyen', 'Female', '1952-12-05', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (7, 'Karen', 'Mendoza', 'Female', '1970-12-10', 3, 218);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (8, 'Joshua', 'Wright', 'Male', '1962-10-05', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (9, 'Virginia', 'Thomas', 'Female', '1992-01-19', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (10, 'Virginia', 'Hernandez', 'Female', '2003-08-27', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (11, 'Linda', 'Lopez', 'Female', '1970-07-16', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (12, 'Brian', 'Stewart', 'Male', '1996-07-23', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (13, 'Nancy', 'Stewart', 'Female', '1981-03-20', NULL, 165);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (14, 'Gregory', 'Evans', 'Male', '1994-06-14', NULL, 417);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (15, 'Nancy', 'Green', 'Female', '1972-08-23', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (16, 'Arthur', 'Reyes', 'Male', '1987-01-28', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (17, 'Virginia', 'Miller', 'Female', '1968-04-06', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (18, 'Judith', 'Thomas', 'Female', '1952-08-03', 5, 364);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (19, 'Patricia', 'Peterson', 'Female', '1986-08-09', 1, 431);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (20, 'Ashley', 'Chavez', 'Female', '1963-10-25', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (21, 'Evelyn', 'Stewart', 'Female', '1971-11-13', 4, 197);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (22, 'Thomas', 'Scott', 'Male', '1987-03-24', NULL, 421);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (23, 'Nicole', 'Ramos', 'Female', '2002-01-10', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (24, 'Helen', 'Peterson', 'Female', '1998-10-03', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (25, 'Jacob', 'Kelly', 'Male', '1984-05-11', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (26, 'Catherine', 'Roberts', 'Female', '2009-07-17', NULL, 494);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (27, 'Roger', 'Ramos', 'Male', '1979-10-14', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (28, 'Andrew', 'Evans', 'Male', '2008-09-28', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (29, 'Diane', 'Wood', 'Female', '1957-03-16', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (30, 'Elizabeth', 'Richardson', 'Female', '1956-02-21', NULL, 117);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (31, 'Betty', 'Brooks', 'Female', '1959-01-07', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (32, 'David', 'Adams', 'Male', '1955-01-13', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (33, 'Gary', 'Ortiz', 'Male', '1986-12-20', 5, 88);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (34, 'Dennis', 'Richardson', 'Male', '1971-08-10', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (35, 'Kelly', 'Allen', 'Female', '2009-10-29', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (36, 'Charles', 'Cruz', 'Male', '1981-01-01', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (37, 'Kelly', 'Hill', 'Female', '1967-11-15', NULL, 55);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (38, 'Carolyn', 'Kelly', 'Female', '1976-07-18', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (39, 'Patricia', 'Reed', 'Female', '1954-05-27', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (40, 'Patrick', 'Lewis', 'Male', '2007-02-11', NULL, 348);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (41, 'David', 'Flores', 'Male', '1989-07-19', NULL, 375);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (42, 'Justin', 'Adams', 'Male', '1987-04-12', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (43, 'Amanda', 'Allen', 'Female', '1993-03-25', NULL, 412);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (44, 'Karen', 'Jackson', 'Female', '1970-03-29', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (45, 'Eric', 'Morgan', 'Male', '1961-02-01', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (46, 'Maria', 'Wilson', 'Female', '2010-07-18', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (47, 'Thomas', 'Brooks', 'Male', '1991-08-27', NULL, 60);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (48, 'William', 'Hill', 'Male', '1994-03-13', 1, 121);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (49, 'Kelly', 'Mitchell', 'Female', '2010-02-25', NULL, 301);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (50, 'Betty', 'Morales', 'Female', '2005-03-26', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (51, 'Peter', 'Cruz', 'Male', '1971-03-08', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (52, 'Jessica', 'Gomez', 'Female', '1974-10-02', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (53, 'Jason', 'Chavez', 'Male', '2007-05-16', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (54, 'Steven', 'Reed', 'Male', '1968-05-30', 1, 301);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (55, 'Gregory', 'Jackson', 'Male', '2003-06-21', NULL, 440);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (56, 'Arthur', 'Allen', 'Male', '1965-08-27', 1, 68);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (57, 'Amy', 'Ramos', 'Female', '1979-01-18', 1, 136);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (58, 'Adam', 'Ortiz', 'Male', '1960-03-13', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (59, 'Zachary', 'Cook', 'Male', '1969-11-16', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (60, 'Linda', 'Davis', 'Female', '1992-12-21', NULL, 352);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (61, 'Virginia', 'Martinez', 'Female', '1957-04-01', 3, 34);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (62, 'Christine', 'Carter', 'Female', '2003-08-06', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (63, 'Mark', 'Wood', 'Male', '2008-05-25', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (64, 'Henry', 'Baker', 'Male', '1990-09-08', NULL, 374);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (65, 'Victoria', 'Green', 'Female', '2009-09-02', NULL, 489);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (66, 'Sarah', 'Lopez', 'Female', '1957-08-29', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (67, 'Joseph', 'Ramos', 'Male', '2000-05-20', NULL, 344);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (68, 'Carolyn', 'Bennett', 'Female', '1987-12-11', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (69, 'Sandra', 'Kelly', 'Female', '1995-07-10', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (70, 'Anthony', 'Hall', 'Male', '1999-11-27', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (71, 'Douglas', 'Bailey', 'Male', '2005-10-11', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (72, 'George', 'Wright', 'Male', '1977-09-20', NULL, 4);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (73, 'Aaron', 'Rodriguez', 'Male', '1962-09-23', 1, 383);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (74, 'Joyce', 'Collins', 'Female', '1980-08-01', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (75, 'Richard', 'Martin', 'Male', '1964-02-15', 5, 346);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (76, 'Virginia', 'James', 'Female', '1988-01-16', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (77, 'Gerald', 'Anderson', 'Male', '1980-12-19', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (78, 'Barbara', 'Lewis', 'Female', '1985-06-17', 5, 4);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (79, 'Sharon', 'Moore', 'Female', '1972-12-03', NULL, 62);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (80, 'Ruth', 'Thompson', 'Female', '1961-08-04', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (81, 'Tyler', 'Garcia', 'Male', '1989-02-19', NULL, 472);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (82, 'Victoria', 'Kelly', 'Female', '1986-04-14', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (83, 'Benjamin', 'Perez', 'Male', '2005-06-15', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (84, 'Gary', 'Parker', 'Male', '2002-10-31', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (85, 'Laura', 'Nelson', 'Female', '1965-01-31', 1, 272);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (86, 'Rachel', 'Chavez', 'Female', '1963-04-02', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (87, 'Brian', 'Cox', 'Male', '1963-09-19', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (88, 'Lauren', 'Mendoza', 'Female', '2000-08-23', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (89, 'Peter', 'Rodriguez', 'Male', '1992-01-26', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (90, 'Patrick', 'Cook', 'Male', '1956-08-28', NULL, 232);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (91, 'Jack', 'Torres', 'Male', '1956-11-19', NULL, 237);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (92, 'Stephanie', 'Adams', 'Female', '2004-04-11', 4, 491);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (93, 'Sandra', 'Baker', 'Female', '1957-07-26', 5, 21);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (94, 'Virginia', 'Ortiz', 'Female', '1996-11-24', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (95, 'Heather', 'Evans', 'Female', '1980-05-10', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (96, 'Gregory', 'Gonzalez', 'Male', '2000-01-22', NULL, 130);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (97, 'Lisa', 'Howard', 'Female', '2009-07-15', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (98, 'Christopher', 'Flores', 'Male', '2000-02-22', NULL, 417);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (99, 'Douglas', 'Rogers', 'Male', '1982-06-18', NULL, 159);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (100, 'Samuel', 'Morales', 'Male', '1967-03-24', 2, 80);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (101, 'Betty', 'Cook', 'Female', '1998-06-05', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (102, 'Dennis', 'Martin', 'Male', '1964-07-22', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (103, 'Henry', 'Campbell', 'Male', '2010-09-06', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (104, 'Cynthia', 'Morgan', 'Female', '1971-06-17', NULL, 463);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (105, 'Virginia', 'Reyes', 'Female', '1975-04-13', NULL, 495);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (106, 'Paul', 'Allen', 'Male', '1954-09-06', NULL, 284);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (107, 'Larry', 'Hernandez', 'Male', '1964-05-20', NULL, 464);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (108, 'Nancy', 'Lewis', 'Female', '1990-06-22', 3, 213);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (109, 'Hannah', 'Mitchell', 'Female', '1971-02-25', 4, 192);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (110, 'Frank', 'Gonzalez', 'Male', '2008-04-23', 3, 71);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (111, 'Joan', 'Hughes', 'Female', '1962-06-14', NULL, 316);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (112, 'Robert', 'Allen', 'Male', '1969-05-07', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (113, 'Scott', 'Thomas', 'Male', '1954-04-14', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (114, 'Mark', 'Murphy', 'Male', '2003-07-15', 5, 324);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (115, 'Justin', 'Diaz', 'Male', '1950-02-21', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (116, 'Christopher', 'Ortiz', 'Male', '1982-05-09', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (117, 'Jerry', 'Mitchell', 'Male', '1972-10-03', NULL, 404);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (118, 'Amy', 'James', 'Female', '2006-05-13', NULL, 69);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (119, 'Debra', 'Chavez', 'Female', '1965-09-16', NULL, 324);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (120, 'Thomas', 'Collins', 'Male', '1953-04-26', 3, 23);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (121, 'Frank', 'Flores', 'Male', '1996-03-28', NULL, 130);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (122, 'Larry', 'Rivera', 'Male', '1954-04-16', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (123, 'Olivia', 'Cruz', 'Female', '1984-09-08', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (124, 'Cheryl', 'Wright', 'Female', '1957-05-31', 4, 221);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (125, 'Christine', 'Wilson', 'Female', '1957-03-08', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (126, 'Amanda', 'Ruiz', 'Female', '1989-10-28', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (127, 'Emma', 'Brooks', 'Female', '1955-02-23', NULL, 187);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (128, 'Andrew', 'Cox', 'Male', '2010-11-01', 4, 65);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (129, 'Alexander', 'Campbell', 'Male', '1984-05-07', 5, 310);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (130, 'Maria', 'Mitchell', 'Female', '1989-10-30', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (131, 'Katherine', 'Wood', 'Female', '1975-01-02', 2, 14);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (132, 'Cheryl', 'Roberts', 'Female', '2000-05-22', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (133, 'Sharon', 'Ward', 'Female', '1975-08-15', 4, 63);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (134, 'Zachary', 'Thompson', 'Male', '1989-12-07', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (135, 'Arthur', 'Nguyen', 'Male', '1976-11-28', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (136, 'Donald', 'Sanchez', 'Male', '1962-06-17', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (137, 'Christina', 'Peterson', 'Female', '1961-08-23', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (138, 'Evelyn', 'Ortiz', 'Female', '1986-11-08', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (139, 'Zachary', 'Reyes', 'Male', '1996-05-31', 3, 450);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (140, 'Nathan', 'Cook', 'Male', '1954-12-21', 1, 156);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (141, 'Benjamin', 'Lewis', 'Male', '1981-01-16', NULL, 434);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (142, 'Dorothy', 'Brooks', 'Female', '1999-06-02', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (143, 'Roger', 'Chavez', 'Male', '1965-02-16', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (144, 'Michael', 'Hernandez', 'Male', '1954-01-29', NULL, 334);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (145, 'Linda', 'Murphy', 'Female', '2006-04-07', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (146, 'Kathleen', 'Mendoza', 'Female', '1986-06-07', NULL, 38);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (147, 'Peter', 'Turner', 'Male', '1993-06-11', 4, 175);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (148, 'Katherine', 'Hall', 'Female', '1985-10-09', NULL, 264);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (149, 'Amy', 'Reyes', 'Female', '1960-12-28', NULL, 127);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (150, 'Richard', 'Nguyen', 'Male', '1984-06-18', NULL, 128);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (151, 'Katherine', 'Harris', 'Female', '1964-04-18', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (152, 'Jennifer', 'Lopez', 'Female', '1985-04-12', NULL, 495);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (153, 'Patrick', 'Miller', 'Male', '1954-07-15', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (154, 'Patricia', 'Wilson', 'Female', '1988-08-29', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (155, 'Janet', 'Garcia', 'Female', '1985-12-09', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (156, 'Jerry', 'Cook', 'Male', '1990-05-28', NULL, 423);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (157, 'Matthew', 'Gomez', 'Male', '1983-06-25', NULL, 387);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (158, 'Gerald', 'Phillips', 'Male', '1994-11-12', 1, 20);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (159, 'Joan', 'Gutierrez', 'Female', '1990-12-31', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (160, 'Tyler', 'Ward', 'Male', '1976-11-05', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (161, 'Joan', 'Williams', 'Female', '1983-01-18', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (162, 'Harold', 'King', 'Male', '2008-10-25', 5, 370);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (163, 'Amanda', 'Ortiz', 'Female', '2006-06-07', NULL, 76);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (164, 'Mark', 'Harris', 'Male', '1951-09-13', NULL, 215);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (165, 'Rebecca', 'Evans', 'Female', '1995-01-08', NULL, 447);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (166, 'Christian', 'Clark', 'Male', '2000-04-27', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (167, 'Melissa', 'Collins', 'Female', '1997-10-30', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (168, 'Stephanie', 'Young', 'Female', '1975-01-12', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (169, 'Rebecca', 'Ruiz', 'Female', '1993-11-14', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (170, 'Ashley', 'Kelly', 'Female', '2010-09-14', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (171, 'Donna', 'Nguyen', 'Female', '1953-10-10', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (172, 'Evelyn', 'Ramirez', 'Female', '1968-02-17', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (173, 'Anthony', 'Ward', 'Male', '2002-08-25', 2, 26);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (174, 'Richard', 'Gonzalez', 'Male', '1987-01-30', NULL, 52);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (175, 'Kenneth', 'Evans', 'Male', '2008-07-28', NULL, 334);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (176, 'Christine', 'Torres', 'Female', '2007-12-12', 1, 334);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (177, 'Brian', 'Turner', 'Male', '1965-10-09', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (178, 'Justin', 'Jones', 'Male', '1950-10-31', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (179, 'Kelly', 'Chavez', 'Female', '1998-09-28', NULL, 456);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (180, 'Brenda', 'Harris', 'Female', '1960-02-09', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (181, 'Deborah', 'Johnson', 'Female', '1980-03-30', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (182, 'Megan', 'Adams', 'Female', '1957-10-13', 4, 95);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (183, 'Christine', 'Young', 'Female', '1950-08-12', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (184, 'Helen', 'Hill', 'Female', '2002-04-04', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (185, 'Joseph', 'Bennett', 'Male', '1960-08-09', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (186, 'Ashley', 'Brooks', 'Female', '1976-06-20', 3, 113);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (187, 'Michelle', 'Collins', 'Female', '2004-05-05', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (188, 'Gary', 'Mendoza', 'Male', '2003-06-15', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (189, 'Mark', 'Davis', 'Male', '1999-02-18', 5, 294);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (190, 'Benjamin', 'Gutierrez', 'Male', '1989-08-22', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (191, 'Gerald', 'Edwards', 'Male', '1954-12-29', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (192, 'Jessica', 'Bailey', 'Female', '1991-06-26', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (193, 'Jason', 'Howard', 'Male', '1956-07-21', NULL, 177);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (194, 'Thomas', 'Stewart', 'Male', '1952-11-05', NULL, 93);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (195, 'Maria', 'Carter', 'Female', '1990-03-29', NULL, 42);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (196, 'Ashley', 'Thompson', 'Female', '1998-03-14', 4, 373);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (197, 'Robert', 'Hill', 'Male', '1991-07-16', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (198, 'Gary', 'Collins', 'Male', '1981-01-20', NULL, 97);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (199, 'Adam', 'Ward', 'Male', '1951-05-28', 2, 35);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (200, 'Zachary', 'Kim', 'Male', '2010-04-16', 1, 380);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (201, 'Virginia', 'Robinson', 'Female', '1998-06-04', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (202, 'Frank', 'Kelly', 'Male', '2003-08-23', 3, 155);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (203, 'Henry', 'Hill', 'Male', '1974-09-08', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (204, 'Susan', 'Hall', 'Female', '2007-09-19', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (205, 'Michelle', 'Hill', 'Female', '1983-10-10', NULL, 124);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (206, 'Donna', 'Reyes', 'Female', '1955-03-04', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (207, 'Jerry', 'Young', 'Male', '1972-11-16', NULL, 332);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (208, 'Maria', 'Lopez', 'Female', '1998-01-20', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (209, 'Charles', 'Harris', 'Male', '2002-09-18', 5, 246);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (210, 'Nicole', 'Johnson', 'Female', '1969-01-01', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (211, 'Timothy', 'Gomez', 'Male', '1971-06-22', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (212, 'Christina', 'Morgan', 'Female', '2008-03-14', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (213, 'Christina', 'Gonzalez', 'Female', '1992-02-14', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (214, 'Barbara', 'Reed', 'Female', '1969-11-07', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (215, 'Michelle', 'Sanchez', 'Female', '1979-08-06', NULL, 292);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (216, 'Debra', 'Allen', 'Female', '1993-11-02', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (217, 'Paul', 'Cooper', 'Male', '1993-10-23', 2, 269);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (218, 'Richard', 'Smith', 'Male', '1986-12-31', 2, 35);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (219, 'Jason', 'Cook', 'Male', '1990-11-29', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (220, 'Jennifer', 'Smith', 'Female', '1997-09-30', NULL, 7);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (221, 'Anna', 'Williams', 'Female', '1995-01-21', 4, 55);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (222, 'Jacob', 'Harris', 'Male', '2005-08-08', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (223, 'Diane', 'Hernandez', 'Female', '1983-06-21', NULL, 290);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (224, 'Scott', 'Mendoza', 'Male', '1957-03-26', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (225, 'Joan', 'Davis', 'Female', '2007-02-15', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (226, 'Helen', 'Reed', 'Female', '1958-07-22', 5, 118);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (227, 'Brenda', 'Garcia', 'Female', '1956-09-02', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (228, 'Timothy', 'Ramos', 'Male', '1962-12-08', 4, 154);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (229, 'Jerry', 'Gray', 'Male', '1998-07-01', NULL, 387);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (230, 'Roger', 'Hall', 'Male', '1954-10-26', NULL, 119);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (231, 'Diane', 'Adams', 'Female', '1952-08-28', NULL, 252);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (232, 'Catherine', 'Parker', 'Female', '1966-08-31', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (233, 'Charles', 'Hernandez', 'Male', '1974-01-15', NULL, 365);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (234, 'Katherine', 'Campbell', 'Female', '1959-07-24', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (235, 'Janet', 'Wright', 'Female', '1959-03-04', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (236, 'Megan', 'Evans', 'Female', '1959-04-08', 1, 182);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (237, 'Heather', 'Johnson', 'Female', '1976-03-08', NULL, 399);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (238, 'Christian', 'Perez', 'Male', '1984-02-27', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (239, 'Andrea', 'Jackson', 'Female', '1955-09-05', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (240, 'Evelyn', 'Martinez', 'Female', '1982-05-26', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (241, 'Kyle', 'Wilson', 'Male', '1962-02-26', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (242, 'Catherine', 'Nelson', 'Female', '1989-06-30', NULL, 418);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (243, 'Christine', 'Cox', 'Female', '1968-01-08', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (244, 'Pamela', 'Ruiz', 'Female', '2006-10-12', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (245, 'Diane', 'Campbell', 'Female', '1960-03-20', 5, 304);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (246, 'Walter', 'Clark', 'Male', '1989-05-03', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (247, 'Emily', 'Brooks', 'Female', '1977-03-03', NULL, 338);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (248, 'Catherine', 'Martinez', 'Female', '1990-04-16', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (249, 'Elizabeth', 'Campbell', 'Female', '1998-03-03', 5, 56);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (250, 'Amanda', 'Chavez', 'Female', '2004-12-19', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (251, 'Sandra', 'Johnson', 'Female', '1958-11-06', 3, 262);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (252, 'Maria', 'Gomez', 'Female', '1991-07-18', 5, 177);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (253, 'Sandra', 'Nguyen', 'Female', '1987-04-27', 1, 426);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (254, 'Samantha', 'Baker', 'Female', '1990-11-07', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (255, 'Peter', 'Hughes', 'Male', '1990-08-04', 3, 154);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (256, 'Robert', 'Baker', 'Male', '2008-02-18', 1, 477);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (257, 'Kenneth', 'Nelson', 'Male', '2000-03-24', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (258, 'George', 'Brooks', 'Male', '2008-12-20', NULL, 15);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (259, 'Victoria', 'Roberts', 'Female', '1950-05-26', 2, 143);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (260, 'Sean', 'White', 'Male', '1982-10-26', 3, 235);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (261, 'Judith', 'Ortiz', 'Female', '2007-05-04', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (262, 'Raymond', 'Rivera', 'Male', '1991-01-29', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (263, 'Paul', 'Green', 'Male', '1960-07-29', NULL, 60);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (264, 'Donna', 'Rogers', 'Female', '1984-11-07', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (265, 'Deborah', 'Morales', 'Female', '2007-01-06', 5, 285);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (266, 'Anna', 'Moore', 'Female', '1966-10-14', NULL, 318);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (267, 'Patricia', 'Morales', 'Female', '1962-04-01', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (268, 'Judith', 'Turner', 'Female', '1989-10-27', 4, 43);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (269, 'Justin', 'Jones', 'Male', '1974-08-29', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (270, 'Megan', 'Anderson', 'Female', '2001-05-19', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (271, 'Peter', 'Cooper', 'Male', '1969-08-10', 4, 377);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (272, 'Elizabeth', 'Edwards', 'Female', '1973-07-30', 3, 225);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (273, 'Timothy', 'Ramos', 'Male', '1981-06-16', NULL, 85);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (274, 'Timothy', 'Davis', 'Male', '2001-02-22', NULL, 306);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (275, 'Pamela', 'Nguyen', 'Female', '2001-05-20', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (276, 'Stephen', 'Wood', 'Male', '1961-05-20', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (277, 'Tyler', 'Morales', 'Male', '1962-10-03', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (278, 'Lauren', 'Martinez', 'Female', '2006-11-05', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (279, 'Kelly', 'Morales', 'Female', '1979-05-13', 5, 445);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (280, 'Carolyn', 'Rodriguez', 'Female', '1997-12-12', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (281, 'Keith', 'Wright', 'Male', '1978-12-19', NULL, 281);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (282, 'Debra', 'Mendoza', 'Female', '1954-05-06', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (283, 'Donald', 'Lee', 'Male', '1989-08-04', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (284, 'Steven', 'Wood', 'Male', '1977-01-30', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (285, 'Lisa', 'Mitchell', 'Female', '2009-08-13', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (286, 'Douglas', 'Wood', 'Male', '1958-03-08', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (287, 'Steven', 'Ramos', 'Male', '1970-04-17', NULL, 5);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (288, 'Ashley', 'Diaz', 'Female', '1961-11-10', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (289, 'Anthony', 'Wilson', 'Male', '1978-02-10', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (290, 'Andrew', 'Rodriguez', 'Male', '1997-08-05', 5, 313);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (291, 'Rachel', 'Ramirez', 'Female', '2006-05-07', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (292, 'Daniel', 'Gonzalez', 'Male', '1962-07-24', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (293, 'Emily', 'Young', 'Female', '1974-11-06', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (294, 'Scott', 'Clark', 'Male', '1996-06-13', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (295, 'Susan', 'Walker', 'Female', '1994-05-26', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (296, 'Terry', 'Johnson', 'Male', '1982-05-25', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (297, 'Melissa', 'Stewart', 'Female', '1956-07-19', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (298, 'David', 'Davis', 'Male', '1985-09-14', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (299, 'Olivia', 'Hernandez', 'Female', '2007-06-20', 5, 143);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (300, 'Lisa', 'Rogers', 'Female', '1968-03-25', NULL, 201);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (301, 'Ruth', 'Walker', 'Female', '1955-03-13', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (302, 'Kyle', 'Ward', 'Male', '2004-08-15', NULL, 342);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (303, 'John', 'Moore', 'Male', '1951-01-07', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (304, 'Amanda', 'Mitchell', 'Female', '1961-05-22', 3, 395);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (305, 'Victoria', 'Wright', 'Female', '1996-12-30', NULL, 365);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (306, 'Kelly', 'Rogers', 'Female', '1982-04-23', NULL, 440);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (307, 'Carol', 'Allen', 'Female', '1959-03-26', 5, 117);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (308, 'John', 'Young', 'Male', '1954-02-15', NULL, 197);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (309, 'William', 'Peterson', 'Male', '2008-10-29', 4, 165);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (310, 'Katherine', 'Wright', 'Female', '1956-12-27', NULL, 62);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (311, 'Jeffrey', 'Gutierrez', 'Male', '1954-02-13', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (312, 'Samantha', 'Adams', 'Female', '1957-10-01', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (313, 'Justin', 'Reed', 'Male', '1977-04-07', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (314, 'Dorothy', 'Cooper', 'Female', '1971-12-29', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (315, 'Ryan', 'Cooper', 'Male', '1981-01-29', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (316, 'Sandra', 'Clark', 'Female', '1997-07-13', NULL, 252);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (317, 'Stephen', 'Lopez', 'Male', '1953-12-09', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (318, 'Lisa', 'Howard', 'Female', '1958-07-29', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (319, 'Joseph', 'Parker', 'Male', '2009-06-06', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (320, 'Diane', 'Hughes', 'Female', '1979-04-09', NULL, 140);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (321, 'Ronald', 'Moore', 'Male', '2002-06-16', 1, 55);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (322, 'Christina', 'Green', 'Female', '1986-06-21', NULL, 494);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (323, 'Samantha', 'Reyes', 'Female', '1973-10-10', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (324, 'Jason', 'Adams', 'Male', '1963-04-23', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (325, 'Megan', 'Miller', 'Female', '2010-10-02', NULL, 420);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (326, 'Aaron', 'Edwards', 'Male', '1999-11-17', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (327, 'Paul', 'Thomas', 'Male', '1951-01-27', 1, 67);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (328, 'Maria', 'Mendoza', 'Female', '2006-07-19', NULL, 470);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (329, 'Thomas', 'Sanchez', 'Male', '2007-12-15', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (330, 'David', 'Reyes', 'Male', '1954-07-18', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (331, 'Linda', 'Carter', 'Female', '1988-04-11', NULL, 110);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (332, 'Emma', 'Edwards', 'Female', '1963-05-03', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (333, 'Julie', 'Peterson', 'Female', '1992-12-22', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (334, 'Adam', 'Sanchez', 'Male', '2007-08-28', 5, 323);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (335, 'Carolyn', 'Morris', 'Female', '1998-11-07', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (336, 'Brenda', 'White', 'Female', '1952-05-04', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (337, 'Harold', 'Ortiz', 'Male', '1982-01-25', 5, 499);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (338, 'Gary', 'James', 'Male', '1971-08-21', 3, 392);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (339, 'Carolyn', 'Thompson', 'Female', '1965-10-19', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (340, 'Patrick', 'Reed', 'Male', '2000-07-25', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (341, 'Melissa', 'Morales', 'Female', '1953-05-28', 1, 120);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (342, 'Terry', 'Morris', 'Male', '1950-01-23', 3, 413);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (343, 'Melissa', 'Adams', 'Female', '1955-05-06', 1, 301);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (344, 'Terry', 'Campbell', 'Male', '1956-07-04', NULL, 301);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (345, 'Nicole', 'Adams', 'Female', '1962-03-30', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (346, 'Melissa', 'Bailey', 'Female', '2005-01-22', 3, 341);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (347, 'Samantha', 'Ruiz', 'Female', '1976-06-03', 2, 374);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (348, 'Elizabeth', 'White', 'Female', '2004-01-17', 3, 328);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (349, 'Donna', 'Nelson', 'Female', '1956-12-24', NULL, 164);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (350, 'Gregory', 'Edwards', 'Male', '1951-01-09', 3, 128);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (351, 'Angela', 'Wilson', 'Female', '1950-02-11', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (352, 'Henry', 'Murphy', 'Male', '1983-12-23', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (353, 'Kenneth', 'Edwards', 'Male', '1956-08-12', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (354, 'Sandra', 'Martinez', 'Female', '1980-08-31', NULL, 83);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (355, 'Samuel', 'Kim', 'Male', '2005-01-19', 4, 221);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (356, 'Carol', 'Miller', 'Female', '1959-02-01', 3, 499);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (357, 'Shirley', 'James', 'Female', '1975-04-04', 3, 50);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (358, 'Judith', 'Martin', 'Female', '1954-11-22', 3, 219);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (359, 'Evelyn', 'Sanchez', 'Female', '1958-09-14', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (360, 'Harold', 'Anderson', 'Male', '1977-08-31', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (361, 'Arthur', 'Roberts', 'Male', '1966-08-03', NULL, 190);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (362, 'Barbara', 'King', 'Female', '1989-06-14', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (363, 'Joshua', 'Hughes', 'Male', '2009-11-18', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (364, 'Cynthia', 'Peterson', 'Female', '1955-06-22', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (365, 'Harold', 'Hill', 'Male', '1957-01-31', 4, 258);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (366, 'Zachary', 'Thompson', 'Male', '1964-12-30', 2, 65);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (367, 'Lisa', 'Mendoza', 'Female', '1989-01-22', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (368, 'Sarah', 'Lopez', 'Female', '1984-10-26', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (369, 'Cheryl', 'Collins', 'Female', '1951-02-10', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (370, 'Andrew', 'Reed', 'Male', '2002-09-30', 5, 474);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (371, 'Larry', 'Morgan', 'Male', '1980-11-06', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (372, 'Elizabeth', 'Thompson', 'Female', '1974-09-16', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (373, 'Tyler', 'Nelson', 'Male', '1971-04-25', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (374, 'Jennifer', 'Baker', 'Female', '1977-03-10', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (375, 'Ryan', 'Moore', 'Male', '1976-12-16', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (376, 'Edward', 'Cruz', 'Male', '1968-12-18', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (377, 'Gerald', 'Lee', 'Male', '1955-11-21', NULL, 70);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (378, 'Edward', 'Sanchez', 'Male', '1955-03-04', 2, 234);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (379, 'Dorothy', 'Scott', 'Female', '1983-01-18', NULL, 326);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (380, 'Jacob', 'Mitchell', 'Male', '1993-11-07', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (381, 'Rachel', 'Lee', 'Female', '1973-03-16', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (382, 'Kenneth', 'Kelly', 'Male', '1969-03-24', 2, 347);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (383, 'Julie', 'Rogers', 'Female', '1951-10-20', NULL, 467);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (384, 'John', 'Lewis', 'Male', '1972-08-23', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (385, 'Catherine', 'Hall', 'Female', '1991-03-07', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (386, 'Sandra', 'Smith', 'Female', '1995-11-22', NULL, 153);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (387, 'Sarah', 'Baker', 'Female', '1974-10-21', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (388, 'Joshua', 'Gutierrez', 'Male', '1971-07-24', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (389, 'Michael', 'Wood', 'Male', '1994-08-15', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (390, 'Heather', 'Jones', 'Female', '2002-04-22', 5, 176);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (391, 'Carolyn', 'Cook', 'Female', '1976-12-06', 2, 151);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (392, 'Kimberly', 'King', 'Female', '2000-02-26', NULL, 336);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (393, 'Patrick', 'Lewis', 'Male', '1977-07-20', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (394, 'Christina', 'Thomas', 'Female', '1992-03-19', 1, 242);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (395, 'Dennis', 'Ortiz', 'Male', '1976-10-07', 4, 446);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (396, 'Ronald', 'Baker', 'Male', '1986-09-17', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (397, 'Christopher', 'Morales', 'Male', '1979-11-04', NULL, 325);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (398, 'Zachary', 'Scott', 'Male', '1968-10-14', 2, 251);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (399, 'Nathan', 'Brooks', 'Male', '1988-07-10', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (400, 'Mary', 'Jones', 'Female', '1997-11-20', NULL, 487);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (401, 'Jacqueline', 'Harris', 'Female', '1951-08-11', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (402, 'Kimberly', 'Wilson', 'Female', '1984-05-30', NULL, 86);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (403, 'Scott', 'Nguyen', 'Male', '1990-11-26', NULL, 223);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (404, 'Judith', 'Rivera', 'Female', '1966-11-27', NULL, 10);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (405, 'Steven', 'Ramirez', 'Male', '1951-12-20', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (406, 'Dennis', 'Brooks', 'Male', '1972-12-12', 5, 305);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (407, 'Robert', 'Miller', 'Male', '1960-05-22', NULL, 195);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (408, 'Joan', 'Hughes', 'Female', '1963-09-27', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (409, 'Christian', 'Wright', 'Male', '2005-11-15', 5, 215);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (410, 'Larry', 'Anderson', 'Male', '1959-07-15', 4, 312);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (411, 'Cheryl', 'Sanchez', 'Female', '1982-02-10', NULL, 83);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (412, 'Rebecca', 'Ruiz', 'Female', '1993-02-14', 3, 2);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (413, 'Mark', 'Kelly', 'Male', '2010-01-08', 4, 487);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (414, 'Matthew', 'Allen', 'Male', '2007-10-22', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (415, 'Susan', 'Gonzalez', 'Female', '1965-09-03', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (416, 'Margaret', 'Gonzalez', 'Female', '1954-02-12', 1, 340);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (417, 'Carolyn', 'Cruz', 'Female', '2005-10-14', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (418, 'Mark', 'Phillips', 'Male', '1985-11-28', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (419, 'Joyce', 'Wood', 'Female', '1964-12-18', 1, 357);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (420, 'Anthony', 'Turner', 'Male', '2002-12-31', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (421, 'Linda', 'Mendoza', 'Female', '1961-09-21', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (422, 'Barbara', 'Rodriguez', 'Female', '1973-06-21', 3, 361);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (423, 'Cheryl', 'Gutierrez', 'Female', '2005-06-19', NULL, 339);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (424, 'Rachel', 'James', 'Female', '2010-09-03', 4, 430);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (425, 'Kenneth', 'Cook', 'Male', '1992-02-07', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (426, 'Amy', 'Nelson', 'Female', '1974-12-15', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (427, 'Amy', 'Hernandez', 'Female', '1991-03-10', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (428, 'Katherine', 'Thomas', 'Female', '1994-08-15', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (429, 'James', 'Lopez', 'Male', '2004-03-16', NULL, 456);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (430, 'Debra', 'Campbell', 'Female', '1954-11-14', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (431, 'Lauren', 'Anderson', 'Female', '1958-09-28', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (432, 'Cheryl', 'Mitchell', 'Female', '1959-07-16', 1, 253);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (433, 'Sandra', 'Allen', 'Female', '2004-10-20', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (434, 'Kyle', 'Harris', 'Male', '1980-04-26', NULL, 24);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (435, 'Kelly', 'James', 'Female', '2002-11-14', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (436, 'Terry', 'Miller', 'Male', '1999-08-20', NULL, 474);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (437, 'Steven', 'Wilson', 'Male', '1984-10-03', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (438, 'Kathleen', 'Scott', 'Female', '1985-09-11', NULL, 232);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (439, 'Henry', 'Cox', 'Male', '1995-12-17', NULL, 365);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (440, 'Timothy', 'Richardson', 'Male', '1976-01-26', 3, 364);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (441, 'Margaret', 'Rivera', 'Female', '2000-06-11', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (442, 'Patricia', 'Gutierrez', 'Female', '1959-07-21', NULL, 75);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (443, 'Ronald', 'Wright', 'Male', '1964-06-09', NULL, 75);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (444, 'Rebecca', 'Cooper', 'Female', '1952-11-24', NULL, 53);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (445, 'Amy', 'Rogers', 'Female', '1975-10-22', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (446, 'Susan', 'Johnson', 'Female', '1972-07-19', NULL, 425);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (447, 'Dorothy', 'Harris', 'Female', '1976-05-23', 4, 350);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (448, 'Brian', 'Rogers', 'Male', '1960-09-15', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (449, 'Kimberly', 'Lee', 'Female', '2002-05-24', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (450, 'David', 'Martin', 'Male', '1978-12-11', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (451, 'Carolyn', 'Martinez', 'Female', '1978-07-08', 5, 490);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (452, 'Roger', 'Lee', 'Male', '1987-04-26', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (453, 'Jason', 'James', 'Male', '1979-10-11', NULL, 151);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (454, 'Patricia', 'Anderson', 'Female', '2010-01-05', NULL, 124);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (455, 'Benjamin', 'Carter', 'Male', '1960-03-04', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (456, 'Christian', 'Mitchell', 'Male', '1996-02-21', NULL, 250);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (457, 'Stephanie', 'Adams', 'Female', '1996-02-08', 1, 86);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (458, 'Timothy', 'Bennett', 'Male', '2006-06-23', NULL, 428);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (459, 'Sean', 'Hughes', 'Male', '1989-01-17', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (460, 'Elizabeth', 'Lopez', 'Female', '1956-07-28', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (461, 'Ryan', 'King', 'Male', '1986-07-28', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (462, 'Katherine', 'Williams', 'Female', '1984-12-11', 1, 329);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (463, 'Charles', 'Rivera', 'Male', '1995-02-10', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (464, 'Larry', 'Cruz', 'Male', '1984-03-21', 4, 243);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (465, 'Paul', 'Gomez', 'Male', '1998-12-17', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (466, 'Andrew', 'Thomas', 'Male', '1953-09-30', NULL, 276);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (467, 'Rebecca', 'Hall', 'Female', '1968-12-30', 4, 83);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (468, 'Nicholas', 'Harris', 'Male', '1960-04-13', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (469, 'Justin', 'Bennett', 'Male', '1956-01-17', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (470, 'Carolyn', 'Taylor', 'Female', '2010-03-24', 2, 146);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (471, 'Frank', 'Morales', 'Male', '1990-06-06', NULL, 356);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (472, 'Katherine', 'Diaz', 'Female', '1965-02-16', NULL, 127);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (473, 'Emma', 'Campbell', 'Female', '1962-01-18', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (474, 'Samantha', 'Morales', 'Female', '1999-06-30', 1, 331);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (475, 'Emily', 'Morgan', 'Female', '1967-08-16', 3, 373);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (476, 'Roger', 'Watson', 'Male', '1952-10-19', NULL, 394);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (477, 'Eric', 'Cooper', 'Male', '1998-06-02', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (478, 'Justin', 'Moore', 'Male', '1991-09-10', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (479, 'Jacob', 'Ward', 'Male', '1964-11-17', 5, 229);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (480, 'Andrew', 'Morris', 'Male', '1982-03-11', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (481, 'Thomas', 'King', 'Male', '1983-02-22', 2, 343);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (482, 'Heather', 'Stewart', 'Female', '1990-10-15', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (483, 'Christian', 'Brooks', 'Male', '1974-07-15', 3, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (484, 'Karen', 'Gutierrez', 'Female', '1972-07-27', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (485, 'Rachel', 'Morales', 'Female', '1993-04-02', 5, 257);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (486, 'Amanda', 'Robinson', 'Female', '1956-12-01', NULL, 109);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (487, 'Kenneth', 'Campbell', 'Male', '2004-01-05', 1, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (488, 'Ethan', 'Gray', 'Male', '1992-12-15', 4, 303);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (489, 'Jennifer', 'Young', 'Female', '1953-11-14', 2, 69);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (490, 'Joseph', 'Perez', 'Male', '1973-03-03', NULL, 307);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (491, 'Lisa', 'Ramirez', 'Female', '1990-04-20', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (492, 'Jeffrey', 'Evans', 'Male', '2003-11-27', 2, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (493, 'Samuel', 'Collins', 'Male', '2003-07-09', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (494, 'Kimberly', 'Wilson', 'Female', '1951-06-27', NULL, 424);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (495, 'Brian', 'Stewart', 'Male', '2005-02-25', 5, 450);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (496, 'Ethan', 'James', 'Male', '1961-09-10', 5, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (497, 'Maria', 'Garcia', 'Female', '1997-07-14', 4, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (498, 'Rachel', 'Ramos', 'Female', '2001-09-08', NULL, NULL);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (499, 'Cynthia', 'Hernandez', 'Female', '1975-06-01', NULL, 132);
INSERT INTO Archer (ArcherID, FirstName, LastName, Gender, DOB, DefaultEquipmentID, ClubID) VALUES (500, 'James', 'Kelly', 'Male', '1996-11-17', 1, 193);"""

insert_statements.extend(sql_data.strip().splitlines())

# ── Write output ───────────────────────────────────────────────────────────────
output_path = "archer_inserts.sql"
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
