-- Create tables in correct dependency order

-- Club table
CREATE TABLE Club (
    ClubID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

-- EquipmentType table
CREATE TABLE EquipmentType (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    DivisionCode VARCHAR(50)
);

-- Championship table
CREATE TABLE Championship (
    ChampionshipID INT AUTO_INCREMENT PRIMARY KEY,
    ChampionshipName VARCHAR(255) NOT NULL,
    Year INT NOT NULL
);

-- BaseRound table
CREATE TABLE BaseRound (
    BaseRoundID INT AUTO_INCREMENT PRIMARY KEY,
    RoundName VARCHAR(255) NOT NULL
);

-- Range table
CREATE TABLE RangeType (
    RangeID INT AUTO_INCREMENT PRIMARY KEY,
    DistanceToTargetM INT NOT NULL,
    TargetFaceCm INT NOT NULL,
    NumberOfEnds INT NOT NULL
);

-- Class table
CREATE TABLE Class (
    ClassID INT AUTO_INCREMENT PRIMARY KEY,
    Gender VARCHAR(10),
    MinAge INT NOT NULL,
    MaxAge INT NOT NULL
);

-- Archer table
CREATE TABLE Archer (
    ArcherID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    Gender VARCHAR(10),
    DOB DATE,
    DefaultEquipmentID INT,
    ClubID INT,
    FOREIGN KEY (DefaultEquipmentID) REFERENCES EquipmentType(EquipmentID),
    FOREIGN KEY (ClubID) REFERENCES Club(ClubID)
);

-- Competition table
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

-- JunctionRoundRange table
CREATE TABLE JunctionRoundRange (
    BaseRoundID INT NOT NULL,
    RangeID INT NOT NULL,
    RangePosition INT NOT NULL,
    PRIMARY KEY (BaseRoundID, RangePosition),
    FOREIGN KEY (BaseRoundID) REFERENCES BaseRound(BaseRoundID),
    FOREIGN KEY (RangeID) REFERENCES RangeType(RangeID)
);

--  
CREATE TABLE RoundScore (
    ScoreID INT AUTO_INCREMENT PRIMARY KEY,
    CompetitionID INT,
    ArcherID INT NOT NULL,
    BaseRoundID INT NOT NULL,
    IsApproved BOOLEAN DEFAULT FALSE,
    `Date` DATE NOT NULL,
    `Time` TIME NOT NULL,
    FOREIGN KEY (CompetitionID) REFERENCES Competition(CompetitionID),
    FOREIGN KEY (ArcherID) REFERENCES Archer(ArcherID),
    FOREIGN KEY (BaseRoundID) REFERENCES BaseRound(BaseRoundID)
);

-- End table
CREATE TABLE End (
    EndID INT AUTO_INCREMENT PRIMARY KEY,
    ScoreID INT NOT NULL,
    Position INT NOT NULL,
    FOREIGN KEY (ScoreID) REFERENCES RoundScore(ScoreID)
);

-- Arrow table
CREATE TABLE Arrow (
    ArrowID INT AUTO_INCREMENT PRIMARY KEY,
    EndID INT NOT NULL,
    Score INT NOT NULL,
    FOREIGN KEY (EndID) REFERENCES End(EndID)
);

-- EquivalentRound table
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
