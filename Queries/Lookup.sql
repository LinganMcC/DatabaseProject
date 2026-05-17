-- ------------------------------------------------------------------------------------------------
-- The Archers Personal Best (PB) for specific rounds.
-- ------------------------------------------------------------------------------------------------
-- Finds the single highest total score an archer has ever shot for each round.
--
-- SUM(ar.Score) totals all arrow scores per round attempt. MAX() then picks the
-- highest of those totals across all attempts at that round, giving the PB.
-- COALESCE() handles rounds where no arrows were recorded, returning 0 instead of NULL.
-- Results are grouped per archer + round so each row represents one round's PB.
SELECT
    a.FirstName,
    a.LastName,
    br.RoundName,
    MAX(COALESCE(attempt_scores.TotalScore, 0)) AS PersonalBest
FROM Archer a
JOIN RoundScore rs ON rs.ArcherID = a.ArcherID
JOIN BaseRound br ON br.BaseRoundID = rs.BaseRoundID
JOIN (
    -- Sub-query: sum arrows per individual round attempt first,
    -- then the outer MAX() picks the best attempt per round.
    SELECT
        rs2.ScoreID,
        COALESCE(SUM(ar2.Score), 0) AS TotalScore
    FROM RoundScore rs2
    LEFT JOIN `End` e2 ON e2.ScoreID = rs2.ScoreID
    LEFT JOIN Arrow ar2 ON ar2.EndID = e2.EndID
    GROUP BY rs2.ScoreID
) AS attempt_scores ON attempt_scores.ScoreID = rs.ScoreID
WHERE -- EDIT VARIABLE HERE
    a.ArcherID = 1
    AND rs.IsApproved = 1
GROUP BY
    a.ArcherID,
    a.FirstName,
    a.LastName,
    br.BaseRoundID,
    br.RoundName
ORDER BY
    br.RoundName ASC;


-- ------------------------------------------------------------------------------------------------
-- The club's overall best score for a round and the record holder.
-- ------------------------------------------------------------------------------------------------
-- Finds the single highest approved score ever shot for each round across all archers,
-- and identifies which archer holds that club record.
--
-- The inner sub-query totals every approved score attempt, ranking them within each
-- round using RANK() OVER (PARTITION BY ...). The outer query then filters to
-- rank = 1 to return only the top score per round. RANK() is used instead of
-- ROW_NUMBER() so that tied record holders are both shown.
SELECT
    br.RoundName,
    a.FirstName,
    a.LastName,
    ranked.TotalScore AS ClubRecord
FROM (
    SELECT
        rs.ScoreID,
        rs.ArcherID,
        rs.BaseRoundID,
        COALESCE(SUM(ar.Score), 0) AS TotalScore,
        RANK() OVER (
            PARTITION BY rs.BaseRoundID          -- rank within each round independently
            ORDER BY COALESCE(SUM(ar.Score), 0) DESC  -- highest score = rank 1
        ) AS ScoreRank
    FROM RoundScore rs
    LEFT JOIN `End` e ON e.ScoreID = rs.ScoreID
    LEFT JOIN Arrow ar ON ar.EndID = e.EndID
    WHERE rs.IsApproved = 1
    GROUP BY
        rs.ScoreID,
        rs.ArcherID,
        rs.BaseRoundID
) AS ranked
JOIN Archer a ON a.ArcherID = ranked.ArcherID
JOIN BaseRound br ON br.BaseRoundID = ranked.BaseRoundID
WHERE ranked.ScoreRank = 1          -- only the top score(s) per round
ORDER BY
    br.RoundName ASC,
    ranked.TotalScore DESC;


-- ------------------------------------------------------------------------------------------------
-- Round definitions (Distances, ends, target faces).
-- ------------------------------------------------------------------------------------------------
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
JOIN `Range` r ON r.RangeID = jrr.RangeID
WHERE -- EDIT VARIABLE HERE
    br.RoundName = 'WA90/1440'
ORDER BY
    br.RoundName ASC,
    jrr.RangePosition ASC;             -- show ranges in shooting order


-- ------------------------------------------------------------------------------------------------
-- Find equivalent rounds.
-- ------------------------------------------------------------------------------------------------
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
    COALESCE(CAST(c.MaxAge AS CHAR), 'Open')   AS MaxAge,   -- NULL MaxAge displayed as 'Open'
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
    et.Name ASC;