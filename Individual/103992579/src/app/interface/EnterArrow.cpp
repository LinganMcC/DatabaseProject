#include "app/interface/EnterArrow.h"
#include "app/Application.h"
#include "app/Error.h"
#include "app/InterfaceShared.h"

#include "app/SQL.h"
#include "fmt/core.h"
#include "jdbc/cppconn/resultset.h"
#include "raygui.h"
#include "raylib.h"

namespace app {

static constexpr std::string_view QueryRoundRangeInfo =
    R"(
SELECT
    jrr.RangeID,            -- Positional info
    jrr.BaseRoundID,
    jrr.RangePosition,
    r.DistanceToTargetM,    -- Target Face Info
    r.TargetFaceCm,
    r.NumberOfEnds
FROM JunctionRoundRange jrr
JOIN RangeType r            ON r.RangeID = jrr.RangeID
JOIN BaseRound br           ON br.BaseRoundID = jrr.BaseRoundID
WHERE
    br.RoundName = ?
ORDER BY
    jrr.RangePosition;
    )";

static constexpr int ScoreX = 10;
static constexpr int ScoreM = 0;

EnterArrowInterface::EnterArrowInterface(Application* app)
    : Interface("Enter Arrow", 0, app)
{
}

void EnterArrowInterface::OnGUI()
{
    BeginSection("Score Entry");
    {
        Header();
        ScoreSlots();
        Keypad();
        ActionButtons();
    }
    EndSection();
}

bool EnterArrowInterface::LoadTransitionData(void* transitionData)
{
    ASSERT(transitionData, "Must provide transition data to EnterArrowInterface");

    auto* package = (TransitionToEnterArrowDataPackage*)transitionData;
    m_FirstName   = std::move(package->firstName);
    m_LastName    = std::move(package->lastName);
    m_RoundName   = std::move(package->roundName);
    m_EquipmentID = package->equipmentID;

    SelectSQL select(QueryRoundRangeInfo);
    select.Bind(m_RoundName);

    if (!select.Execute())
        return false;

    sql::ResultSet* results = select.GetResults();
    while (results->next())
    {
        m_RoundID = results->getUInt(2);

        Range range{.rangeID           = results->getUInt(1),
                    .distanceToTargetM = results->getUInt(4),
                    .targetFaceCm      = results->getUInt(5),
                    .numberOfEnds      = results->getUInt(6)};
        m_Ranges.emplace_back(std::move(range));
    }
    return true;
}

void EnterArrowInterface::Header()
{
    GuiText(fmt::format("{} {}, {}", m_FirstName, m_LastName, EquipmentNames[m_EquipmentID]),
            0,
            1,
            true);

    Range& range = m_Ranges[m_CurrentRangeIndex];

    GuiText(fmt::format("{}m {}cm", range.distanceToTargetM, range.targetFaceCm), 0, 1, true);
    GuiText(fmt::format("End {}", range.ends.size()), 0, 1, true);
}

void EnterArrowInterface::ScoreSlots()
{
    Range& currentRange = m_Ranges[m_CurrentRangeIndex];
    if (currentRange.ends.empty())
        currentRange.ends.push_back(End{});

    End& currentEnd = currentRange.ends.back();

    int totalColumns = End::MaxArrowCount + 1; // +1 for the Total box

    for (size_t i = 0; i < End::MaxArrowCount; ++i)
    {
        std::string scoreText =
            (i < currentEnd.arrowScores.size()) ? GetScoreString(currentEnd.arrowScores[i]) : "";

        GuiButton(GetBounds(i, totalColumns), scoreText.c_str());
    }

    int total = 0;
    for (int s : currentEnd.arrowScores)
        total += (s == ScoreX) ? 10 : s;

    std::string totalTxt = fmt::format("Tot: {}", total);
    GuiButton(GetBounds(End::MaxArrowCount, totalColumns), totalTxt.c_str());
}

void EnterArrowInterface::Keypad()
{
    // Row 1
    if (GuiButton(GetBounds(0, 4), "X"))
        AddSCore(ScoreX);
    if (GuiButton(GetBounds(1, 4), "10"))
        AddSCore(10);
    if (GuiButton(GetBounds(2, 4), "9"))
        AddSCore(9);
    if (GuiButton(GetBounds(3, 4), "8"))
        AddSCore(8);

    // Row 2
    if (GuiButton(GetBounds(0, 4), "7"))
        AddSCore(7);
    if (GuiButton(GetBounds(1, 4), "6"))
        AddSCore(6);
    if (GuiButton(GetBounds(2, 4), "5"))
        AddSCore(5);
    if (GuiButton(GetBounds(3, 4), "4"))
        AddSCore(4);

    // Row 3
    if (GuiButton(GetBounds(0, 4), "3"))
        AddSCore(3);
    if (GuiButton(GetBounds(1, 4), "2"))
        AddSCore(2);
    if (GuiButton(GetBounds(2, 4), "1"))
        AddSCore(1);
    if (GuiButton(GetBounds(3, 4), "M"))
        AddSCore(ScoreM);
}

void EnterArrowInterface::ActionButtons()
{
    Range& currentRange = m_Ranges[m_CurrentRangeIndex];
    End& currentEnd     = currentRange.ends.back();

    if (IsKeyPressed(KEY_ESCAPE))
    {
        // Auto fill
        while (currentEnd.arrowScores.size() < End::MaxArrowCount)
            currentEnd.arrowScores.push_back(5);
    }

    if (GuiButton(GetBounds(0, 2), "Cancel"))
        GetApp()->SetCurrentInterface("Setup", nullptr);

    if (GuiButton(GetBounds(1, 2), "Backspace"))
        currentEnd.arrowScores.pop_back();

    if (currentEnd.arrowScores.size() == End::MaxArrowCount)
    {
        if (GuiButton(GetBounds(), "Save"))
        {
            if (currentRange.ends.size() == currentRange.numberOfEnds)
            {
                // Are there more ranges in this round?
                if (m_CurrentRangeIndex + 1 < m_Ranges.size())
                {
                    m_CurrentRangeIndex++;
                    m_Ranges[m_CurrentRangeIndex].ends.push_back(End{}); // First end of next range
                }
                else
                {
                    if (PushToDatabase())
                    {
                        GetApp()->SetCurrentInterface("Success", nullptr);
                    }
                    else
                    {
                        // Optional: Set an error state to display to the user
                        FATAL("Failed to push scores to database.");
                    }
                }
            }
            else
                currentRange.ends.push_back(End{}); // Next end in range
        }
    }
}

bool EnterArrowInterface::PushToDatabase()
{
    // 1. Get the ArcherID
    SelectSQL archerSelect("SELECT ArcherID FROM Archer WHERE FirstName = ? AND LastName = ?");
    archerSelect.Bind(m_FirstName);
    archerSelect.Bind(m_LastName);

    if (!archerSelect.Execute() || !archerSelect.GetResults()->next())
        return false;

    int archerID = archerSelect.GetResults()->getInt(1);

    // 2. Create the RoundScore Entry
    std::string_view queryScore =
        "INSERT INTO RoundScore (ArcherID, BaseRoundID, EquipmentID, `Date`, `Time`) "
        "VALUES (?, ?, ?, CURDATE(), CURTIME())";

    UpdateSQL scoreInsert(queryScore); // Using your UpdateSQL wrapper
    scoreInsert.Bind(archerID);
    scoreInsert.Bind(m_RoundID);
    scoreInsert.Bind(m_EquipmentID + 1);

    if (!scoreInsert.Execute())
        return false;

    // FIX 1: Fetch the ScoreID by looking up the most recent entry for this Archer
    SelectSQL scoreIdSelect(
        "SELECT ScoreID FROM RoundScore WHERE ArcherID = ? ORDER BY ScoreID DESC LIMIT 1");
    scoreIdSelect.Bind(archerID);

    if (!scoreIdSelect.Execute() || !scoreIdSelect.GetResults()->next())
        return false;

    int scoreID = scoreIdSelect.GetResults()->getInt(1);

    // 3. Iterate through Ranges and Ends
    int absoluteEndPosition = 1;

    for (const Range& range : m_Ranges)
    {
        for (const End& end : range.ends)
        {
            // Insert End
            UpdateSQL endInsert("INSERT INTO `End` (ScoreID, Position) VALUES (?, ?)");
            endInsert.Bind(scoreID);

            // We store the current position in a variable so we can query it easily right after
            int currentPosition = absoluteEndPosition++;
            endInsert.Bind(currentPosition);

            if (!endInsert.Execute())
                return false;

            // FIX 2: Fetch the EndID using the unique combination of ScoreID and Position
            SelectSQL endIdSelect("SELECT EndID FROM `End` WHERE ScoreID = ? AND Position = ?");
            endIdSelect.Bind(scoreID);
            endIdSelect.Bind(currentPosition);

            if (!endIdSelect.Execute() || !endIdSelect.GetResults()->next())
                return false;

            int endID = endIdSelect.GetResults()->getInt(1);

            // 4. Insert Arrows
            for (int score : end.arrowScores)
            {
                UpdateSQL arrowInsert("INSERT INTO Arrow (EndID, Score) VALUES (?, ?)");
                arrowInsert.Bind(endID);
                arrowInsert.Bind(score);

                if (!arrowInsert.Execute())
                    return false;
            }
        }
    }

    return true;
}

void EnterArrowInterface::AddSCore(int scoreValue)
{
    End& currentEnd = m_Ranges[m_CurrentRangeIndex].ends.back();

    if (currentEnd.arrowScores.size() >= End::MaxArrowCount)
        return;

    // Enforce magnitude order (Large scores first)
    if (!currentEnd.arrowScores.empty())
    {
        // Ignore input if it breaks the order rule
        int lastScore = currentEnd.arrowScores.back();
        if (scoreValue > lastScore)
            return;
    }

    currentEnd.arrowScores.push_back(scoreValue);
}

std::string EnterArrowInterface::GetScoreString(int scoreValue) const
{
    if (scoreValue == ScoreX)
        return "X";
    if (scoreValue == ScoreM)
        return "M";
    return std::to_string(scoreValue);
}

} // namespace app
