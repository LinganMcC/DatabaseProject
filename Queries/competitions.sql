-- View club competition results (placings, arrow totals, scores).
-- ------------------------------------------------------------------------------------------------
-- Description...
-- Technical description...
select
    cmp.CompetitionName,
    cl.Name as ClubName,
    br.RoundName,
    arc.FirstName,
    arc.LastName,
    cmp.CompetitionDate,
    sum(a.Score) as TotalArrowScore,
    count(a.ArrowID) as TotalArrows
from Competition cmp
join RoundScore rs on cmp.CompetitionID = rs.CompetitionID
join Archer arc on rs.ArcherID = arc.ArcherID
join End e on rs.ScoreID = e.ScoreID
join Arrow a on e.EndID = a.EndID
join Club cl on cmp.ClubID = cl.ClubID
join BaseRound br on rs.BaseRoundID = br.BaseRoundID
where rs.IsApproved = 1
group by cmp.CompetitionID, arc.ArcherID, cl.ClubID, br.BaseRoundID, cmp.CompetitionDate

-- View yearly club championship results and identify winners.
-- ------------------------------------------------------------------------------------------------
-- Description...
-- Technical description...
