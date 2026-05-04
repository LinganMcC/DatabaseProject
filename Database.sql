CREATE TABLE Archer (
    ArcherID int PRIMARY KEY,
    FirstName varChar,
    LastName varChar,
    Gender varChar,
    DOB date,
    DefaultEquipmentID int,
    ClubID int
);

CREATE TABLE EquipmentType (
    EquipmentID int PRIMARY KEY,
    Name varChar,
    DivisionCode varChar
);

CREATE TABLE Club (
    ClubID int PRIMARY KEY,
    Name varChar
);

CREATE TABLE BaseRound (
    BaseRoundID int PRIMARY KEY,
    RoundName varChar
);

CREATE TABLE JunctionRoundRange (
    BaseRoundID int,
    RangeID int,
    RangePosition int
);

CREATE TABLE Range (
    RangeID int PRIMARY KEY,
    DistanceToTargetM int,
    TargetFaceCm int,
    NumberOfEnds int
);

CREATE TABLE Class (
    ClassID int PRIMARY KEY,
    Gender varChar,
    MinAge int,
    MaxAge int
);

CREATE TABLE EquivalentRound (
    EquivalentRoundID int PRIMARY KEY,
    BaseRoundID int,
    ActualRoundID int,
    ClassID int,
    EquipmentID varChar,
    ValidFrom date,
    ValidTo date
);

CREATE TABLE Competition (
    CompetitionID int PRIMARY KEY,
    BaseRoundID int,
    ClubID int,
    ChampionshipID int,
    CompetitionDate date,
    CompetitionName varChar
);

CREATE TABLE Championship (
    ChampionshipID int PRIMARY KEY,
    ChampionshipName varChar,
    Year int
);

CREATE TABLE RoundScore (
    ScoreID int PRIMARY KEY,
    CompetitionID int,
    ArcherID int,
    BaseRoundID int,
    IsApproved bool,
    Date date,
    Time time
);

CREATE TABLE End (
    EndID int PRIMARY KEY,
    ScoreID int,
    Position int
);

CREATE TABLE Arrow (
    ArrowID int PRIMARY KEY,
    EndID int,
    Score int
);
