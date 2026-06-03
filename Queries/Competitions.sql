-- ------------------------------------------------------------------------------------------------
-- View club competition results (placings, arrow totals, scores).
-- ------------------------------------------------------------------------------------------------
-- Authors: - Ewan Robson   103992579@student.swin.edu.au
--          - Eugene Tan    105334351@student.swin.edu.au
--
-- Shows the top ranking participants of every competition while ordering by date. There are two
-- options, showing all participants or only the top 3 performing archers (see HOW TO USE to
-- select between the two options).
--
-- HOW TO USE:
--  | 1. Copy CTE (Entire WITH query) and paste at the top within phpmyadmin SQL
--  | 2. Select Either one of the following queries and paste under CTE query (see below)
--  |    - OPT 1: See all results query
--  |    - OPT 2: See top 3 ranks only query
--
-- Technical Info:
-- RANK() -> Orders and provides a ranking based on the ORDER BY. PARTITION BY divides the reuslt
--           into groups and ranks rows independently within each group
--           More Info: https://www.geeksforgeeks.org/sql/rank-function-in-sql-server/
--
-- WITH   -> (Common Table Expression (CTE)) Basically defines a function/macro that you can reuse
--           within other queries. It kinda creates a new tempory table result set where its
--           lifetime exists only for the duration of the entire collection of queries.
--           More Info: https://www.geeksforgeeks.org/sql/sql-with-clause/
--
--           Another Note when implementing WIDTH, don't put ORDER BY, leave that to the queries
--           using this, also don't add a semi-colon as its a syntax error.
--           When providing parameters `WIDTH Name (param1...) AS (...);`  then you add semi-colon
--           as its more generic.
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

-- OPT 1: See all results query
SELECT
    ClubName,
    CompetitionName,
    CompetitionDate,
    RankPlacing,
    FirstName,
    LastName,
    HighestScoreResult,
    TotalArrowsShot
FROM CompetitionRankedResult
ORDER BY
    CompetitionDate DESC,
    RankPlacing     ASC;

-- OPT 2: See top 3 ranks only query
SELECT
    ClubName,
    CompetitionName,
    CompetitionDate,
    RankPlacing,
    FirstName,
    LastName,
    HighestScoreResult,
    TotalArrowsShot
FROM CompetitionRankedResult
WHERE
    RankPlacing <= 3
ORDER BY
    CompetitionDate DESC,
    RankPlacing     ASC;

-- ------------------------------------------------------------------------------------------------
-- View yearly club championship results and identify winners.
-- ------------------------------------------------------------------------------------------------
-- Author: - Viet Hoang Tran   studentid : 104688235
--
-- Shows the yearly club championship results by adding together each archer's approved scores
-- from all competitions that belong to a selected championship year. The query ranks archers by
-- their total championship score, allowing the club to identify the championship winner. If two
-- or more archers have the same total score, they will receive the same rank.

-- Important:
-- This query only includes approved scores:
--      rs.IsApproved = TRUE
--
-- This prevents unapproved or staged scores from being counted in the championship results.
-- ------------------------------------------------------------------------------------------------

WITH ChampionshipResult AS (
    SELECT
        chp.ChampionshipID,
        chp.ChampionshipName,
        chp.Year,

        cmp.CompetitionID,
        cmp.CompetitionName,
        cmp.CompetitionDate,

        a.ArcherID,
        a.FirstName,
        a.LastName,

        SUM(ar.Score) AS CompetitionScore
    FROM Championship chp
    JOIN Competition cmp
        ON cmp.ChampionshipID = chp.ChampionshipID
    JOIN RoundScore rs
        ON rs.CompetitionID = cmp.CompetitionID
    JOIN Archer a
        ON a.ArcherID = rs.ArcherID
    JOIN `End` e
        ON e.ScoreID = rs.ScoreID
    JOIN Arrow ar
        ON ar.EndID = e.EndID
    WHERE
        rs.IsApproved = TRUE
        AND chp.Year = 2010
    GROUP BY
        chp.ChampionshipID,
        chp.ChampionshipName,
        chp.Year,
        cmp.CompetitionID,
        cmp.CompetitionName,
        cmp.CompetitionDate,
        a.ArcherID,
        a.FirstName,
        a.LastName
),

ArcherChampionshipTotal AS (
    SELECT
        ChampionshipID,
        ChampionshipName,
        Year,
        ArcherID,
        FirstName,
        LastName,
        SUM(CompetitionScore) AS ChampionshipTotalScore
    FROM ChampionshipResult
    GROUP BY
        ChampionshipID,
        ChampionshipName,
        Year,
        ArcherID,
        FirstName,
        LastName
),

RankedChampionship AS (
    SELECT
        ChampionshipName,
        Year,
        ArcherID,
        FirstName,
        LastName,
        ChampionshipTotalScore,

        RANK() OVER (
            PARTITION BY ChampionshipID
            ORDER BY ChampionshipTotalScore DESC
        ) AS ChampionshipRank
    FROM ArcherChampionshipTotal
)

SELECT
    ChampionshipName,
    Year,
    ChampionshipRank,
    FirstName,
    LastName,
    ChampionshipTotalScore
FROM RankedChampionship
ORDER BY
    Year DESC,
    ChampionshipRank ASC;