-- View History score listing over time.
-- ------------------------------------------------------------------------------------------------
-- Collects the total score of each round linked to a specific archer ID.
--
-- Collects all arrows and sums up the total using SUM(), COALESCE() returns the first  non-null
-- value from the list.
-- LEFT JOIN -> Left side of the table (BaserRound) must exist, where End/Arrow don't have to
-- strictly exist as it will just skip it and move to the next. The RoundScore will still show
-- as an entry.
SELECT
    a.FirstName,
    a.LastName,
    COALESCE(SUM(ar.Score), 0) AS TotalScore,
    rs.`Date`,
    rs.`Time`,
    br.RoundName
FROM RoundScore rs
JOIN Archer a
    ON rs.ArcherID = a.ArcherID
JOIN BaseRound br
    ON rs.BaseRoundID = br.BaseRoundID
LEFT JOIN End e
    ON rs.ScoreID = e.ScoreID
LEFT JOIN Arrow ar
    ON ar.EndID = e.EndID
WHERE rs.ArcherID = 1 -- EDIT VARIABLE HERE
GROUP BY
    br.RoundName,
    a.FirstName,
    a.LastName,
    rs.`Date`,
    rs.`Time`
ORDER BY
    rs.`Date` ASC,
    rs.`Time` ASC;

-- Filter scores by date range and round type.
-- ------------------------------------------------------------------------------------------------
-- Description...
-- Technical description...

-- Sort listings by date and score.
-- ------------------------------------------------------------------------------------------------
-- Description...
-- Technical description...
