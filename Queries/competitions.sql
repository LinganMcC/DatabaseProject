-- View club competition results (placings, arrow totals, scores).
-- ------------------------------------------------------------------------------------------------
-- Description...
-- Technical description...
select
    cmp.CompetitionName,
    cl.Name as ClubName,
    br.RoundName,
    a.FirstName,
    a.LastName,
    cmp.CompetitionDate,
    sum(ar.Score) as TotalArrowScore,
    count(ar.ArrowID) as TotalArrows
from Competition cmp
join RoundScore rs on cmp.CompetitionID = rs.CompetitionID
join Archer a on rs.ArcherID = a.ArcherID
join End e on rs.ScoreID = e.ScoreID
join Arrow ar on e.EndID = ar.EndID
join Club cl on cmp.ClubID = cl.ClubID
join BaseRound br on rs.BaseRoundID = br.BaseRoundID
where rs.IsApproved = 1
group by cmp.CompetitionID, a.ArcherID, cl.ClubID, br.BaseRoundID, cmp.CompetitionDate



-- View yearly club championship results and identify winners.
-- ------------------------------------------------------------------------------------------------
-- Description...
-- Technical description...
