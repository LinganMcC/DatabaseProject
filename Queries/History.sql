USE archer_database;

-- ────────────────────────────────────────────────────────────────────────────
-- View history score listing over time.
-- Aggregates arrows into a per-RoundScore total, joined to archer + round.
-- ────────────────────────────────────────────────────────────────────────────
SELECT
    rs.ScoreID,
    CONCAT(a.FirstName, ' ', a.LastName) AS Archer,
    br.RoundName,
    et.Name        AS Equipment,
    rs.`Date`,
    rs.`Time`,
    SUM(ar.Score)  AS TotalScore,
    rs.IsApproved
FROM RoundScore rs
JOIN Archer        a  ON a.ArcherID    = rs.ArcherID
JOIN BaseRound     br ON br.BaseRoundID = rs.BaseRoundID
JOIN EquipmentType et ON et.EquipmentID = rs.EquipmentID
JOIN End           e  ON e.ScoreID     = rs.ScoreID
JOIN Arrow         ar ON ar.EndID      = e.EndID
GROUP BY rs.ScoreID, a.FirstName, a.LastName, br.RoundName, et.Name, rs.`Date`, rs.`Time`, rs.IsApproved
ORDER BY rs.`Date` DESC, TotalScore DESC;


-- ────────────────────────────────────────────────────────────────────────────
-- Filter scores by date range and round type.
-- Example: WA-style rounds shot between 2020 and 2024.
-- ────────────────────────────────────────────────────────────────────────────
SELECT
    rs.ScoreID,
    CONCAT(a.FirstName, ' ', a.LastName) AS Archer,
    br.RoundName,
    rs.`Date`,
    SUM(ar.Score) AS TotalScore
FROM RoundScore rs
JOIN Archer    a  ON a.ArcherID    = rs.ArcherID
JOIN BaseRound br ON br.BaseRoundID = rs.BaseRoundID
JOIN End       e  ON e.ScoreID     = rs.ScoreID
JOIN Arrow     ar ON ar.EndID      = e.EndID
WHERE rs.`Date` BETWEEN '2020-01-01' AND '2024-12-31'
  AND br.RoundName LIKE 'WA%'
GROUP BY rs.ScoreID, a.FirstName, a.LastName, br.RoundName, rs.`Date`
ORDER BY rs.`Date`, TotalScore DESC;


-- ────────────────────────────────────────────────────────────────────────────
-- Sort score listings by date and score for a single archer (e.g. ArcherID 1).
-- ────────────────────────────────────────────────────────────────────────────
SELECT
    rs.ScoreID,
    br.RoundName,
    rs.`Date`,
    rs.`Time`,
    SUM(ar.Score) AS TotalScore
FROM RoundScore rs
JOIN BaseRound br ON br.BaseRoundID = rs.BaseRoundID
JOIN End       e  ON e.ScoreID     = rs.ScoreID
JOIN Arrow     ar ON ar.EndID      = e.EndID
WHERE rs.ArcherID = 1
GROUP BY rs.ScoreID, br.RoundName, rs.`Date`, rs.`Time`
ORDER BY rs.`Date` DESC, TotalScore DESC;
