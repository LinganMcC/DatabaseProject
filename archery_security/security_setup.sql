-- =========================================
-- CREATE ROLES
-- =========================================

CREATE ROLE 'archer_role';
CREATE ROLE 'recorder_role';
CREATE ROLE 'admin_role';

-- =========================================
-- ARCHER ROLE
-- =========================================

GRANT SELECT ON archer_database.Archer TO 'archer_role';
GRANT SELECT ON archer_database.BaseRound TO 'archer_role';
GRANT SELECT ON archer_database.RangeType TO 'archer_role';
GRANT SELECT ON archer_database.JunctionRoundRange TO 'archer_role';
GRANT SELECT ON archer_database.EquipmentType TO 'archer_role';
GRANT SELECT ON archer_database.EquivalentRound TO 'archer_role';

GRANT SELECT, INSERT ON archer_database.RoundScore TO 'archer_role';
GRANT SELECT, INSERT ON archer_database.`End` TO 'archer_role';
GRANT SELECT, INSERT ON archer_database.Arrow TO 'archer_role';

-- =========================================
-- RECORDER ROLE
-- =========================================

GRANT SELECT, INSERT, UPDATE
ON archer_database.Archer
TO 'recorder_role';

GRANT SELECT, INSERT, UPDATE
ON archer_database.RoundScore
TO 'recorder_role';

GRANT SELECT, INSERT, UPDATE
ON archer_database.`End`
TO 'recorder_role';

GRANT SELECT, INSERT, UPDATE
ON archer_database.Arrow
TO 'recorder_role';

GRANT SELECT, INSERT, UPDATE
ON archer_database.Competition
TO 'recorder_role';

GRANT SELECT, INSERT, UPDATE
ON archer_database.Championship
TO 'recorder_role';

-- =========================================
-- ADMIN ROLE
-- =========================================

GRANT ALL PRIVILEGES
ON archer_database.*
TO 'admin_role';

-- =========================================
-- CREATE USERS
-- =========================================

CREATE USER 'archer_user'@'localhost'
IDENTIFIED BY 'StrongPassword1!';

CREATE USER 'recorder_user'@'localhost'
IDENTIFIED BY 'StrongPassword2!';

CREATE USER 'admin_user'@'localhost'
IDENTIFIED BY 'StrongPassword3!';

-- =========================================
-- ASSIGN ROLES
-- =========================================

GRANT 'archer_role'
TO 'archer_user'@'localhost';

GRANT 'recorder_role'
TO 'recorder_user'@'localhost';

GRANT 'admin_role'
TO 'admin_user'@'localhost';

FLUSH PRIVILEGES;