-- ------------------------------------------------------------------------------------------------
-- View club competition results (placings, arrow totals, scores).
-- ------------------------------------------------------------------------------------------------
-- RANK() -> Orders and provides a ranking based on the ORDER BY. PARTITION BY divides the reuslt
--           into groups and ranks rows independently within each group
--           https://www.geeksforgeeks.org/sql/rank-function-in-sql-server/
SELECT
    cl.Name AS ClubName,                    -- Club and Competition details
    cmp.CompetitionName,
    cmp.CompetitionDate,
    RANK() OVER (                           -- Plancing Rank
        PARTITION BY cmp.CompetitionID
        ORDER BY SUM(ar.Score) DESC
    ) AS Rank,
    a.FirstName,                            -- Archer Name
    a.LastName,
    SUM(ar.Score) AS HighestScoreResult,    -- Total Score
    (
        SELECT
            SUM(r.NumberOfEnds * 6) AS TotalEndCount
        FROM JunctionRoundRange jrr
        JOIN RangeType r            ON r.RangeID = jrr.RangeID
        WHERE
            jrr.BaseRoundID = cmp.BaseRoundID

    ) AS TotalPossibleArrows,               -- Total possible arrows to shoot
    COUNT(ar.ArrowID) AS TotalArrowsShot    -- Actual arrows shot
FROM Competition cmp
JOIN BaseRound br       ON cmp.BaseRoundID = br.BaseRoundID
JOIN RoundScore rs      ON rs.CompetitionID = cmp.CompetitionID
JOIN Club cl            ON cl.ClubID = cmp.ClubID
JOIN Archer a           ON a.ArcherID = rs.ArcherID
JOIN `End` e            ON e.ScoreID = rs.ScoreID
JOIN Arrow ar           ON ar.EndID = e.EndID
WHERE
    rs.IsApproved = true
GROUP BY
    cl.Name,
    cmp.CompetitionName,
    cmp.CompetitionDate,
    cmp.CompetitionID, -- Distinguish between competitions with the same name
    a.ArcherID,        -- Distinguish between archers with the same name
    a.FirstName,
    a.LastName
ORDER BY
    cmp.CompetitionID   DESC,
    cmp.CompetitionDate DESC,
    Rank                ASC;

-- select
--     cmp.CompetitionName,
--     cl.Name as ClubName,
--     br.RoundName,
--     a.FirstName,
--     a.LastName,
--     cmp.CompetitionDate,
--     sum(ar.Score) as TotalArrowScore,
--     (SELECT SUM(r.NumberOfEnds * 6)
--      FROM junctionroundrange jrr
--      JOIN rangetype r ON jrr.RangeID = r.RangeID
--      WHERE jrr.BaseRoundID = br.BaseRoundID) AS ExpectedArrows
-- from Competition cmp
-- join RoundScore rs on cmp.CompetitionID = rs.CompetitionID
-- join Archer a on rs.ArcherID = a.ArcherID
-- join End e on rs.ScoreID = e.ScoreID
-- join Arrow ar on e.EndID = ar.EndID
-- join Club cl on cmp.ClubID = cl.ClubID
-- join BaseRound br on rs.BaseRoundID = br.BaseRoundID
-- where rs.IsApproved = 1
-- group by cmp.CompetitionID, a.ArcherID, cl.ClubID, br.BaseRoundID, cmp.CompetitionDate

-- ------------------------------------------------------------------------------------------------
-- View yearly club championship results and identify winners.
-- ------------------------------------------------------------------------------------------------
-- Description...
-- Technical description...
