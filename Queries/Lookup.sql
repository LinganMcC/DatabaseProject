-- ================================================================================================
-- Personal Best (PB) for rounds.
-- ================================================================================================
-- Authors: Liam McCarthy     105336043@student.swin.edu.au
--          Shriyans Simhadri 105914805@student.swin.edu.au
--
-- Returns archers' PBs per round, with the date set.
--
-- HOW TO USE:
--  | 1. Copy CTE (Entire WITH query) and paste at the top within phpmyadmin SQL
--  | 2. Select either one of the following queries and paste under CTE query:
--  |    - OPT 1: See PBs for all archers across all rounds
--  |    - OPT 2: See PBs for one specific archer (edit ArcherID in WHERE clause)
--
-- Technical Info:
-- RANK() ties are preserved -- if an archer equals their own PB on a later date,
-- both attempts are returned rather than arbitrarily dropping one.
WITH ArcherPBRanked AS (
    SELECT
        a.ArcherID,
        a.FirstName,
        a.LastName,
        br.BaseRoundID,
        br.RoundName,
        rs.`Date` AS ScoreDate,
        COALESCE(SUM(ar.Score), 0) AS TotalScore,
        RANK() OVER (
            PARTITION BY a.ArcherID, br.BaseRoundID
            ORDER BY COALESCE(SUM(ar.Score), 0) DESC
        ) AS ScoreRank
    FROM RoundScore rs
    JOIN Archer    a   ON a.ArcherID     = rs.ArcherID
    JOIN BaseRound br  ON br.BaseRoundID = rs.BaseRoundID
    LEFT JOIN `End` e  ON e.ScoreID      = rs.ScoreID
    LEFT JOIN Arrow ar ON ar.EndID       = e.EndID
    WHERE
        rs.IsApproved = TRUE
    GROUP BY
        rs.ScoreID,
        a.ArcherID,
        a.FirstName,
        a.LastName,
        br.BaseRoundID,
        br.RoundName,
        rs.`Date`
)

-- OPT 1: See PBs for all archers
SELECT
    FirstName,
    LastName,
    RoundName,
    TotalScore AS PersonalBest,
    ScoreDate
FROM ArcherPBRanked
WHERE
    ScoreRank = 1
ORDER BY
    LastName    ASC,
    FirstName   ASC,
    RoundName   ASC;

-- OPT 2: See PBs for one specific archer
SELECT
    FirstName,
    LastName,
    RoundName,
    TotalScore AS PersonalBest,
    ScoreDate
FROM ArcherPBRanked
WHERE
    ScoreRank = 1
    AND ArcherID = 1    -- EDIT: change to the ArcherID you want
ORDER BY
    RoundName ASC;


-- ================================================================================================
-- Club record for rounds (best approved score and who holds it).
-- ================================================================================================
-- Authors: Liam McCarthy     105336043@student.swin.edu.au
--          Shriyans Simhadri 105914805@student.swin.edu.au
--
-- Returns each club's record per round, with the holder's name and the date it was set.
--
-- HOW TO USE:
--  | 1. Copy CTE (Entire WITH query) and paste at the top within phpmyadmin SQL
--  | 2. Select either one of the following queries and paste under CTE query:
--  |    - OPT 1: See records for all clubs across all rounds
--  |    - OPT 2: See records for one specific club (edit ClubID in WHERE clause)
--
-- Technical Info:
-- RANK() ties are preserved -- if two archers in the same club share the record,
-- both are returned rather than arbitrarily dropping one.
WITH ClubRecordRanked AS (
    SELECT
        cl.ClubID,
        cl.Name AS ClubName,
        br.BaseRoundID,
        br.RoundName,
        a.FirstName,
        a.LastName,
        rs.`Date` AS ScoreDate,
        COALESCE(SUM(ar.Score), 0) AS TotalScore,
        RANK() OVER (
            PARTITION BY cl.ClubID, br.BaseRoundID
            ORDER BY COALESCE(SUM(ar.Score), 0) DESC
        ) AS ScoreRank
    FROM RoundScore rs
    JOIN Archer    a   ON a.ArcherID     = rs.ArcherID
    JOIN Club      cl  ON cl.ClubID      = a.ClubID
    JOIN BaseRound br  ON br.BaseRoundID = rs.BaseRoundID
    LEFT JOIN `End` e  ON e.ScoreID      = rs.ScoreID
    LEFT JOIN Arrow ar ON ar.EndID       = e.EndID
    WHERE
        rs.IsApproved = TRUE
    GROUP BY
        rs.ScoreID,
        cl.ClubID,
        cl.Name,
        br.BaseRoundID,
        br.RoundName,
        a.FirstName,
        a.LastName,
        rs.`Date`
)

-- OPT 1: See records for all clubs
SELECT
    ClubName,
    RoundName,
    FirstName,
    LastName,
    TotalScore AS ClubRecord,
    ScoreDate
FROM ClubRecordRanked
WHERE
    ScoreRank = 1
ORDER BY
    ClubName  ASC,
    RoundName ASC;

-- OPT 2: See records for one specific club
SELECT
    ClubName,
    RoundName,
    FirstName,
    LastName,
    TotalScore AS ClubRecord,
    ScoreDate
FROM ClubRecordRanked
WHERE
    ScoreRank = 1
    AND ClubID = 4    -- EDIT: change to the ClubID you want
ORDER BY
    RoundName ASC; 
-- ------------------------------------------------------------------------------------------------
-- Round definitions (Distances, ends, target faces).
-- ------------------------------------------------------------------------------------------------
-- Authors: - Shriyans Simhadri: 105914805@student.swin.edu.au
--
-- Returns the full definition of a round: every range that makes it up,
-- in the order they are shot, with distance, target face size and number of ends.
--
-- JunctionRoundRange is the junction table that links BaseRound to its Ranges.
-- RangePosition orders the ranges as they are shot during the round.
-- The WHERE clause can be changed to look up by RoundName or BaseRoundID.
SELECT
    br.RoundName,
    jrr.RangePosition,
    r.DistanceToTargetM,
    r.TargetFaceCm,
    r.NumberOfEnds,
    (r.NumberOfEnds * 6) AS TotalArrows   -- each end always has 6 arrows
FROM BaseRound br
JOIN JunctionRoundRange jrr ON jrr.BaseRoundID = br.BaseRoundID
JOIN `Range` r              ON r.RangeID = jrr.RangeID
WHERE -- EDIT VARIABLE HERE
    br.RoundName = 'WA90/1440'
ORDER BY
    br.RoundName      ASC,
    jrr.RangePosition ASC;             -- show ranges in shooting order


-- ------------------------------------------------------------------------------------------------
-- Find equivalent rounds.
-- ------------------------------------------------------------------------------------------------
-- Authors: - Shriyans Simhadri: 105914805@student.swin.edu.au
--
-- For a given base round (the Male Open reference round), returns every equivalent
-- round that other classes and equipment types are permitted to shoot instead,
-- along with the class and equipment it applies to and the date range it was valid.
--
-- EquivalentRound links a BaseRound (the event's official round) to the ActualRound
-- an archer shoots based on their Class and EquipmentType. ValidFrom / ValidTo
-- capture the history of rule changes — a NULL ValidTo means the rule is current.
-- The WHERE clause filters to rules that are active today; remove the ValidTo check
-- to include historical equivalents as well.
SELECT
    base_br.RoundName                           AS BaseRound,
    actual_br.RoundName                         AS EquivalentRound,
    c.Gender,
    c.MinAge,
    COALESCE(CAST(c.MaxAge AS CHAR), 'Open')    AS MaxAge,   -- NULL MaxAge displayed as 'Open'
    et.Name                                     AS EquipmentType,
    er.ValidFrom,
    er.ValidTo
FROM EquivalentRound er
JOIN BaseRound base_br   ON base_br.BaseRoundID   = er.BaseRoundID
JOIN BaseRound actual_br ON actual_br.BaseRoundID = er.ActualRoundID
JOIN Class c             ON c.ClassID             = er.ClassID
JOIN EquipmentType et    ON et.EquipmentID        = er.EquipmentID
WHERE -- EDIT VARIABLE HERE
    base_br.RoundName = 'WA90/1440'
    AND (er.ValidTo IS NULL OR er.ValidTo >= CURDATE())  -- currently active rules only
ORDER BY
    c.Gender ASC,
    c.MinAge DESC,
    et.Name  ASC;

-- ------------------------------------------------------------------------------------------------
-- Stage scores by approved.
-- ------------------------------------------------------------------------------------------------
-- Authors: - Viet Hoang Tran - 104688235@student.swin.edu.au
--
--The recorder needs to look up all staged scores waiting for approval. The system retrieves all RoundScore
--records where IsApproved = FALSE, joins them with Archer, BaseRound, EquipmentType, optional
--Competition, End, and Arrow, and displays the archer name, round, equipment, date, time, competition
--details, total arrows recorded, and total score. This allows the recorder to verify the score before approving it.

SELECT
    rs.ScoreID,
    a.ArcherID,
    CONCAT(a.FirstName, ' ', a.LastName) AS ArcherName,
    c.Name AS ClubName,
    br.RoundName AS RoundShot,
    et.Name AS EquipmentUsed,
    rs.`Date`,
    rs.`Time`,
    cmp.CompetitionName,
    cmp.CompetitionDate,
    COUNT(ar.ArrowID) AS NumberOfArrowsRecorded,
    SUM(ar.Score) AS TotalScore,
    CASE
        WHEN rs.IsApproved = TRUE THEN 'Approved'
        ELSE 'Staged / Waiting for Approval'
    END AS ApprovalStatus
FROM RoundScore rs
JOIN Archer a
    ON a.ArcherID = rs.ArcherID
LEFT JOIN Club c
    ON c.ClubID = a.ClubID
JOIN BaseRound br
    ON br.BaseRoundID = rs.BaseRoundID
JOIN EquipmentType et
    ON et.EquipmentID = rs.EquipmentID
LEFT JOIN Competition cmp
    ON cmp.CompetitionID = rs.CompetitionID
LEFT JOIN `End` e
    ON e.ScoreID = rs.ScoreID
LEFT JOIN Arrow ar
    ON ar.EndID = e.EndID
WHERE rs.IsApproved = FALSE
GROUP BY
    rs.ScoreID,
    a.ArcherID,
    a.FirstName,
    a.LastName,
    c.Name,
    br.RoundName,
    et.Name,
    rs.`Date`,
    rs.`Time`,
    cmp.CompetitionName,
    cmp.CompetitionDate,
    rs.IsApproved
ORDER BY
    rs.`Date` ASC,
    rs.`Time` ASC;