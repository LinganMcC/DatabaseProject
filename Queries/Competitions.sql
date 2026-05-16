-- ------------------------------------------------------------------------------------------------
-- View club competition results (placings, arrow totals, scores).
-- ------------------------------------------------------------------------------------------------
-- RANK() -> Orders and provides a ranking based on the ORDER BY. PARTITION BY divides the reuslt
--           into groups and ranks rows independently within each group
--           More Info: https://www.geeksforgeeks.org/sql/rank-function-in-sql-server/
-- WITH   -> (Common Table Expression (CTE)) Basically defines a function/macro that you can reuse
--           within other queries. It kinda creates a new tempory table result set where its
--           lifetime exists only for the duration of the entire collection of queries.
--           More Info: https://www.geeksforgeeks.org/sql/sql-with-clause/
--
--           Another Note when implementing WIDTH, don't put ORDER BY, leave that to the queries
--           using this, also don't add a semi-colon as its a syntax error.
--           When providing parameters `WIDTH Name (param1...) AS (...);`  then you add semi-colon
--           as its more generic.
--
-- HOW TO USE:
--  | 1. Copy CTE (Entire WITH query) and paste at the top within phpmyadmin SQL
--  | 2. Select Either one of the following queries and paste under CTE query (see below)
--  |    - OPT 1: See all results query
--  |    - OPT 2: See top 3 ranks only query
WITH CompetitionRankedResult AS (
    SELECT
        cl.Name AS ClubName,                    -- Club and Competition details
        cmp.CompetitionName,
        cmp.CompetitionDate,
        cmp.CompetitionID,
        RANK() OVER (                           -- Plancing Rank
            PARTITION BY cmp.CompetitionID
            ORDER BY SUM(ar.Score) DESC
        ) AS RankPlacing,
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
            ) AS TotalPossibleArrows,           -- Total possible arrows to shoot
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
)

-- OPT 2: See top 3 ranks only query
SELECT
    cte.ClubName,
    cte.CompetitionName,
    cte.CompetitionDate,
    cte.RankPlacing,
    cte.FirstName,
    cte.LastName,
    cte.HighestScoreResult,
    cte.TotalArrowsShot
FROM CompetitionRankedResult cte
WHERE
    cte.RankPlacing <= 3
ORDER BY
    cte.CompetitionID   DESC,
    cte.CompetitionDate DESC,
    cte.RankPlacing     ASC;

-- OPT 1: See all results query
SELECT
    cte.ClubName,
    cte.CompetitionName,
    cte.CompetitionDate,
    cte.RankPlacing,
    cte.FirstName,
    cte.LastName,
    cte.HighestScoreResult,
    cte.TotalArrowsShot
FROM CompetitionRankedResult cte
ORDER BY
    cte.CompetitionID   DESC,
    cte.CompetitionDate DESC,
    cte.RankPlacing     ASC;


-- ------------------------------------------------------------------------------------------------
-- View yearly club championship results and identify winners.
-- ------------------------------------------------------------------------------------------------
-- Description...
-- Technical description...
