-- ================================================================================================
-- Clear Database if exists
-- ================================================================================================

-- Removing if exists
DROP DATABASE IF EXISTS archer_database;
CREATE DATABASE archer_database;
USE archer_database;

-- ================================================================================================
-- Core Foundational Tables (Every table below relys on these tables)
-- ================================================================================================

CREATE TABLE Club (
    ClubID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

CREATE TABLE EquipmentType (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    DivisionCode VARCHAR(50)
);

CREATE TABLE Championship (
    ChampionshipID INT AUTO_INCREMENT PRIMARY KEY,
    ChampionshipName VARCHAR(255) NOT NULL,
    Year INT NOT NULL
);

CREATE TABLE BaseRound (
    BaseRoundID INT AUTO_INCREMENT PRIMARY KEY,
    RoundName VARCHAR(255) NOT NULL
);

CREATE TABLE Class (
    ClassID INT AUTO_INCREMENT PRIMARY KEY,
    Gender VARCHAR(10),
    MinAge INT NOT NULL,
    MaxAge INT NOT NULL
);

-- ================================================================================================
-- Archer and Competitions Tables (Secondary, a lot of tables still rely on this)
-- ================================================================================================

CREATE TABLE Archer (
    ArcherID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Gender VARCHAR(10),
    DOB DATE,
    DefaultEquipmentID INT,
    ClubID INT,
    FOREIGN KEY (DefaultEquipmentID) REFERENCES EquipmentType(EquipmentID),
    FOREIGN KEY (ClubID) REFERENCES Club(ClubID)
);


CREATE TABLE Competition (
    CompetitionID INT AUTO_INCREMENT PRIMARY KEY,
    BaseRoundID INT NOT NULL,
    ClubID INT NOT NULL,
    ChampionshipID INT,
    CompetitionDate DATE NOT NULL,
    CompetitionName VARCHAR(255) NOT NULL,
    FOREIGN KEY (BaseRoundID) REFERENCES BaseRound(BaseRoundID),
    FOREIGN KEY (ClubID) REFERENCES Club(ClubID),
    FOREIGN KEY (ChampionshipID) REFERENCES Championship(ChampionshipID)
);

-- ================================================================================================
-- Round Tables
-- ================================================================================================

CREATE TABLE RangeType (
    RangeID INT AUTO_INCREMENT PRIMARY KEY,
    DistanceToTargetM INT NOT NULL,
    TargetFaceCm INT NOT NULL,
    NumberOfEnds INT NOT NULL
);

CREATE TABLE JunctionRoundRange (
    BaseRoundID INT NOT NULL,
    RangeID INT NOT NULL,
    RangePosition INT NOT NULL,
    PRIMARY KEY (BaseRoundID, RangePosition),
    FOREIGN KEY (BaseRoundID) REFERENCES BaseRound(BaseRoundID),
    FOREIGN KEY (RangeID) REFERENCES RangeType(RangeID)
);

CREATE TABLE RoundScore (
    ScoreID INT AUTO_INCREMENT PRIMARY KEY,
    CompetitionID INT,
    ArcherID INT NOT NULL,
    BaseRoundID INT NOT NULL,
    IsApproved BOOLEAN DEFAULT FALSE,
    EquipmentID INT NOT NULL,
    `Date` DATE NOT NULL,
    `Time` TIME NOT NULL,
    FOREIGN KEY (EquipmentID) REFERENCES EquipmentType(EquipmentID),
    FOREIGN KEY (CompetitionID) REFERENCES Competition(CompetitionID),
    FOREIGN KEY (ArcherID) REFERENCES Archer(ArcherID),
    FOREIGN KEY (BaseRoundID) REFERENCES BaseRound(BaseRoundID)
);

CREATE TABLE EquivalentRound (
    EquivalentRoundID INT AUTO_INCREMENT PRIMARY KEY,
    BaseRoundID INT NOT NULL,
    ActualRoundID INT NOT NULL,
    ClassID INT NOT NULL,
    EquipmentID INT NOT NULL,
    ValidFrom DATE NOT NULL,
    ValidTo DATE,
    FOREIGN KEY (BaseRoundID) REFERENCES BaseRound(BaseRoundID),
    FOREIGN KEY (ActualRoundID) REFERENCES BaseRound(BaseRoundID),
    FOREIGN KEY (ClassID) REFERENCES Class(ClassID),
    FOREIGN KEY (EquipmentID) REFERENCES EquipmentType(EquipmentID)
);

-- ================================================================================================
-- Round
-- ================================================================================================

-- No indexing required here, primary and foreign keys are already indexed

CREATE TABLE `End` (
    EndID INT AUTO_INCREMENT PRIMARY KEY,
    ScoreID INT NOT NULL,
    Position INT NOT NULL,
    FOREIGN KEY (ScoreID) REFERENCES RoundScore(ScoreID)
);

CREATE TABLE Arrow (
    ArrowID INT AUTO_INCREMENT PRIMARY KEY,
    EndID INT NOT NULL,
    Score INT NOT NULL,
    FOREIGN KEY (EndID) REFERENCES End(EndID)
);

-- ================================================================================================
-- Indexing
-- ================================================================================================

-- Sorting/filtering by Date and Time when Archer = ? - History (2)
CREATE INDEX Idx_RoundScoreArcherDateTime ON RoundScore(ArcherID, `Date`, `Time`);
-- Speeds up WHERE br.RoundName = "..." - History (2), Lookup (3, 4)
CREATE INDEX Idx_BaseRoundName ON BaseRound(RoundName)
--Speeds up WHERE Isapproved = True and Archer = ?, BaseRoundID = ? - PersonalBest, CLub record, Stage Score approval
CREATE INDEX Idx_RoundScore_IsApproved_Archer ON RoundScore(IsApproved, ArcherID, BaseRoundID);
--Every score-summing query needs to join End and Arrow
--So these 2 indexes will speed up all of those queries
CREATE INDEX Idx_End_ScoreID ON `End`(ScoreID);
CREATE INDEX Idx_Arrow_EndID ON Arrow(EndID);


