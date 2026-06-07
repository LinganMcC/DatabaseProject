
from db_config import get_connection

def get_archer_history(archer_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT
        a.FirstName,
        a.LastName,
        COALESCE(SUM(ar.Score), 0) AS TotalScore,
        rs.Date,
        rs.Time,
        br.RoundName
    FROM RoundScore rs
    JOIN Archer a
        ON rs.ArcherID = a.ArcherID
    JOIN BaseRound br
        ON rs.BaseRoundID = br.BaseRoundID
    LEFT JOIN `End` e
        ON e.ScoreID = rs.ScoreID
    LEFT JOIN Arrow ar
        ON ar.EndID = e.EndID
    WHERE rs.ArcherID = %s
    GROUP BY
        a.ArcherID,
        a.FirstName,
        a.LastName,
        rs.Date,
        rs.Time,
        br.RoundName
    ORDER BY
        rs.Date ASC,
        rs.Time ASC
    """

    # PREPARED STATEMENT
    cursor.execute(query, (archer_id,))

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


def get_personal_bests(archer_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    WITH ArcherPBRanked AS (
        SELECT
            a.ArcherID,
            a.FirstName,
            a.LastName,
            br.RoundName,
            rs.Date AS ScoreDate,
            COALESCE(SUM(ar.Score), 0) AS TotalScore,

            RANK() OVER (
                PARTITION BY a.ArcherID, br.BaseRoundID
                ORDER BY COALESCE(SUM(ar.Score), 0) DESC
            ) AS ScoreRank

        FROM RoundScore rs
        JOIN Archer a
            ON a.ArcherID = rs.ArcherID
        JOIN BaseRound br
            ON br.BaseRoundID = rs.BaseRoundID
        LEFT JOIN `End` e
            ON e.ScoreID = rs.ScoreID
        LEFT JOIN Arrow ar
            ON ar.EndID = e.EndID

        WHERE
            rs.IsApproved = TRUE
            AND a.ArcherID = %s

        GROUP BY
            rs.ScoreID,
            a.ArcherID,
            a.FirstName,
            a.LastName,
            br.RoundName,
            rs.Date
    )

    SELECT
        FirstName,
        LastName,
        RoundName,
        TotalScore,
        ScoreDate
    FROM ArcherPBRanked
    WHERE ScoreRank = 1
    ORDER BY RoundName ASC;
    """

    cursor.execute(query, (archer_id,))

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results

