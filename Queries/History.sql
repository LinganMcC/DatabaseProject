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
JOIN Archer a ON rs.ArcherID = a.ArcherID
JOIN BaseRound br ON rs.BaseRoundID = br.BaseRoundID
LEFT JOIN `End` e ON e.ScoreID = rs.ScoreID
LEFT JOIN Arrow ar ON ar.EndID = e.EndID
WHERE -- EDIT VARIABLE HERE
    rs.ArcherID = 1
GROUP BY
    br.RoundName,
    a.FirstName,
    a.LastName,
    rs.`Date`,
    rs.`Time`
ORDER BY
    rs.`Date` ASC,
    rs.`Time` ASC;

-- Filter scores by date, range and round type.
-- ------------------------------------------------------------------------------------------------
SELECT
    a.FirstName,
    a.LastName,
    COALESCE(SUM(ar.Score), 0) AS TotalScore,
    r.DistanceToTargetM,
    r.TargetFaceCm,
    r.NumberOfEnds,
    rs.`Date`
FROM RoundScore rs
JOIN Archer a ON a.ArcherID = rs.ArcherID
JOIN BaseRound br ON br.BaseRoundID= rs.BaseRoundID
JOIN JunctionRoundRange jrr ON jrr.BaseRoundID = br.BaseRoundID
JOIN RangeType r ON r.RangeID = jrr.RangeID
LEFT JOIN `End` e ON e.ScoreID = rs.ScoreID
LEFT JOIN Arrow ar ON ar.EndID = e.EndID
WHERE -- EDIT VARIABLES HERE
    a.ArcherID = 1,
    AND rs.`Date` BETWEEN '2023-01-01' AND '2023-12-31',
    AND r.DistanceToTargetM = 50,
    AND br.RoundName = 'WA 18m'
GROUP BY
    a.FirstName,
    a.LastName,
    r.DistanceToTargetM,
    r.TargetFaceCm,
    r.NumberOfEnds,
    rs.`Date`
ORDER BY
    r.DistanceToTargetM DESC,
    r.TargetFaceCm DESC,
    r.NumberOfEnds DESC,
    rs.`Date` DESC;

-- Sort listings by date and score.
-- ------------------------------------------------------------------------------------------------
-- Description...
-- Technical description...
