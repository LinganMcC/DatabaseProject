USE archer_database;

-- ────────────────────────────────────────────────────────────────────────────
-- View club competition results (placings, arrow totals, scores).
-- Example: results for CompetitionID 1 — ranks archers by total score.
-- ────────────────────────────────────────────────────────────────────────────
SELECT
    RANK() OVER (ORDER BY SUM(ar.Score) DESC) AS Placing,
    CONCAT(a.FirstName, ' ', a.LastName) AS Archer,
    c.Name           AS Club,
    et.Name          AS Equipment,
    COUNT(ar.ArrowID) AS ArrowsShot,
    SUM(ar.Score)    AS TotalScore
FROM Competition       comp
JOIN RoundScore        rs ON rs.CompetitionID = comp.CompetitionID
JOIN Archer            a  ON a.ArcherID      = rs.ArcherID
JOIN Club              c  ON c.ClubID        = a.ClubID
JOIN EquipmentType     et ON et.EquipmentID  = rs.EquipmentID
JOIN End               e  ON e.ScoreID       = rs.ScoreID
JOIN Arrow             ar ON ar.EndID        = e.EndID
WHERE comp.CompetitionID = 1
GROUP BY rs.ScoreID, a.FirstName, a.LastName, c.Name, et.Name
ORDER BY TotalScore DESC;


-- ────────────────────────────────────────────────────────────────────────────
-- View yearly club championship results and identify winners.
-- For each championship, returns the archer with the highest total score.
-- ────────────────────────────────────────────────────────────────────────────
WITH ChampionshipTotals AS (
    SELECT
        ch.ChampionshipID,
        ch.ChampionshipName,
        ch.Year,
        rs.ArcherID,
        SUM(ar.Score) AS TotalScore
    FROM Championship ch
    JOIN Competition  comp ON comp.ChampionshipID = ch.ChampionshipID
    JOIN RoundScore   rs   ON rs.CompetitionID    = comp.CompetitionID
    JOIN End          e    ON e.ScoreID           = rs.ScoreID
    JOIN Arrow        ar   ON ar.EndID            = e.EndID
    GROUP BY ch.ChampionshipID, ch.ChampionshipName, ch.Year, rs.ArcherID
)
SELECT
    ct.ChampionshipName,
    ct.Year,
    CONCAT(a.FirstName, ' ', a.LastName) AS Winner,
    c.Name AS Club,
    ct.TotalScore
FROM ChampionshipTotals ct
JOIN Archer a ON a.ArcherID = ct.ArcherID
JOIN Club   c ON c.ClubID   = a.ClubID
WHERE (ct.ChampionshipID, ct.TotalScore) IN (
    SELECT ChampionshipID, MAX(TotalScore)
    FROM ChampionshipTotals
    GROUP BY ChampionshipID
)
ORDER BY ct.Year DESC, ct.ChampionshipName;
