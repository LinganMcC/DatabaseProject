# Database Project

The purpose of this submission is to provide evidence of your work during this semester. It includes both the process and the deliverables.

> **_Naming convention you must follow:_**
>
> - Object names are easily understood
> - Table names are not pluralized ("User" table not "Users")
> - Abbreviations are few, but allowed (i.e. Qty, Amt, etc.)
> - PascalCase used exclusively with the exception of certain column names (i.e. rowguid)
> - No underscores
> - Certain keywords are allowed (i.e. Name)
> - Stored procedures are prefaced with "usp"
> - Functions are prefaced with "ufn"
>
> **_Aliases:_**
>
> - Club = cl
> - EquipmentType = et
> - ChampionShip = chp
> - BaseRound = br
> - RangeType = r
> - Class = c
> - Archer = a
> - Competition = cmp
> - JunctionRoundRange = jrr
> - RoundScore = rs
> - End = e
> - Arrow = ar
> - EquivalentRound = er
>
> **_Variables in queries:_** Mark them using `-- EDIT VARIABLE HERE` to make it clear. Look in History, the first query for an example.

## Data Generation

1. Generate Database
    - Copy Database.sql into myphpadmin or alternative and execute. This creates a the database with archer_database as its name. Refresh if it doesn't show immediately.
2. Fill database with test data
    1. Open terminal and navigate to `Scripts` folder. Make sure its the current working directory using `pwd` in terminal.
    2. Execute all scripts `py execute_all.py` or `py execute_all.py 123` or any number, represents the number of archers to create. All other data scales based on archer count.
    3. This outputs insert statements into `output.sql` file, copy and paste into myphpadmin or alternative and execute.

## Unit Learning Outcomes

1. Acquire basic knowledge independently about the selection of suitable database technology as well as the design of databases according to relational and NoSQL principles.
2. Design and implement a project plan using industry standard project management and collaboration tools.
3. Apply ethical, professonal and technical considerations in the development of a database solution for a stakeholder.
4. Effectively discuss database storage solutions, alternative options and data storage and access requirements with stakeholders including issues such as data privacy and security.
5. Design and implement a database solution for a given purpose, including data access and manipulation as well as data privacy and security, according to project specifications in a team.
6. Contribute to the project development as a respectful and responsible team member.

## Submission Requirements

1. PDF of custom exported Confluence Space, containing
    - Initial ER diagram (Week 4)
    - Review of ER diagram to normalise/denormalise, revise relationships (Week 5), possible subsequent reviews (e.g. adjustments due to use cases)
    - Physical database (Week 6) - Create Table statements
    - Document on data creation and null values (Week 7)
    - Use cases and SQL statements, transactions (Week 8)
    - Performance (indexes) (Week 9)
    - Major-specific work (naming the contributor) (Week 10 + 11)
    - Team reflection (4L Retrospective Links to an external site.) (Week 12)
    - Task management (all weeks)
    - Meeting minutes (all weeks)

# Checklist

## Archer Requirements

- History
    - [x] View History score listing over time.
    - [x] Filter scores by date range and round type.
    - [x] Sort listings by date and score.
- Lookup
    - [x] The club's overall best score for a round and the record holder.
    - [x] Round definitions (Distances, ends, target faces).
    - [x] Find equivalent rounds.
    - [x] Stage scores by approved.
    - [x] Round and see all equivalent rounds
- Competitions
    - [x] View club competition results (placings, arrow totals, scores).
    - [x] View yearly club championship results and identify winners.

## Recorder Requirements

- Setup
    - [ ] Enter and configure new archers into the system.
    - [ ] Define new rounds and setup upcoming competitions.
    - [ ] Flag which specific scores qualify for standard competitions vs club championships.
- Score Management
    - [ ] Review and add new scores staged by archers.
    - [ ] Approve practice scores by verifying the staged equipment matches the recorded equipment.

## System and Data Requirement

- [x] Classifications: Store standard age, gender and bow division.
- [x] Range Configuration: Defines valid distances (excluding 80m) and target faces.
- [x] Arrow Scoring: Record individual and recorder arrow values.
- [x] End Tracking: Store sets of 6 arrows, ordered highest to lowest, mapped to a position within a round.
- [x] Round Definitions: Store historical and current valid date ranges. Round info: number of Ends and equivalent round mapping.
- [x] Archer Accounts: Store core identity (name, age, gender) and default equipment preferences.
- [x] Score Staging: Archers append their competition entry containing: date, time, round, and equipment, while the recorder adds their recorded score for comparison.
