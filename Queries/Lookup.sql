USE archer_database;

-- ────────────────────────────────────────────────────────────────────────────
-- The archer's Personal Best (PB) for each round.
-- Example: PBs for ArcherID 1, ordered by round name.
-- ────────────────────────────────────────────────────────────────────────────
SELECT
    br.RoundName,
    MAX(ScoreTotals.TotalScore) AS PersonalBest
FROM (
    SELECT
        rs.ScoreID,
        rs.ArcherID,
        rs.BaseRoundID,
        SUM(ar.Score) AS TotalScore
    FROM RoundScore rs
    JOIN End   e  ON e.ScoreID = rs.ScoreID
    JOIN Arrow ar ON ar.EndID  = e.EndID
    WHERE rs.ArcherID = 1
    GROUP BY rs.ScoreID, rs.ArcherID, rs.BaseRoundID
) ScoreTotals
JOIN BaseRound br ON br.BaseRoundID = ScoreTotals.BaseRoundID
GROUP BY br.RoundName
ORDER BY br.RoundName;


-- ────────────────────────────────────────────────────────────────────────────
-- The club's overall best score for each round and the record holder.
-- Example: club records for ClubID 1.
-- ────────────────────────────────────────────────────────────────────────────
WITH ScoreTotals AS (
    SELECT
        rs.ScoreID,
        rs.ArcherID,
        rs.BaseRoundID,
        a.ClubID,
        SUM(ar.Score) AS TotalScore
    FROM RoundScore rs
    JOIN Archer a  ON a.ArcherID = rs.ArcherID
    JOIN End    e  ON e.ScoreID  = rs.ScoreID
    JOIN Arrow  ar ON ar.EndID   = e.EndID
    GROUP BY rs.ScoreID, rs.ArcherID, rs.BaseRoundID, a.ClubID
)
SELECT
    br.RoundName,
    CONCAT(a.FirstName, ' ', a.LastName) AS RecordHolder,
    st.TotalScore AS ClubBest
FROM ScoreTotals st
JOIN Archer    a  ON a.ArcherID    = st.ArcherID
JOIN BaseRound br ON br.BaseRoundID = st.BaseRoundID
WHERE st.ClubID = 1
  AND (st.BaseRoundID, st.TotalScore) IN (
      SELECT BaseRoundID, MAX(TotalScore)
      FROM ScoreTotals
      WHERE ClubID = 1
      GROUP BY BaseRoundID
  )
ORDER BY br.RoundName;


-- ────────────────────────────────────────────────────────────────────────────
-- Round definitions (distances, ends, target faces).
-- Lists every BaseRound with its ordered ranges and per-leg specs.
-- ────────────────────────────────────────────────────────────────────────────
SELECT
    br.BaseRoundID,
    br.RoundName,
    jrr.RangePosition,
    rt.DistanceToTargetM AS Distance_m,
    rt.TargetFaceCm      AS Face_cm,
    rt.NumberOfEnds      AS Ends
FROM BaseRound          br
JOIN JunctionRoundRange jrr ON jrr.BaseRoundID = br.BaseRoundID
JOIN RangeType          rt  ON rt.RangeID      = jrr.RangeID
ORDER BY br.RoundName, jrr.RangePosition;


-- ────────────────────────────────────────────────────────────────────────────
-- Find equivalent rounds — what does each base round map to for a given
-- class/equipment? Example: currently-valid mappings only.
-- ────────────────────────────────────────────────────────────────────────────
SELECT
    base.RoundName    AS BaseRound,
    actual.RoundName  AS EquivalentTo,
    cl.Gender,
    cl.MinAge,
    cl.MaxAge,
    et.Name           AS Equipment,
    er.ValidFrom,
    er.ValidTo
FROM EquivalentRound er
JOIN BaseRound     base   ON base.BaseRoundID   = er.BaseRoundID
JOIN BaseRound     actual ON actual.BaseRoundID = er.ActualRoundID
JOIN Class         cl     ON cl.ClassID         = er.ClassID
JOIN EquipmentType et     ON et.EquipmentID     = er.EquipmentID
WHERE er.ValidTo IS NULL
ORDER BY base.RoundName, cl.Gender, cl.MinAge;
