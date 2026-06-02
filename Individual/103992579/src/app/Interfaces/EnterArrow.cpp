#include "app/Interfaces/EnterArrow.h"
#include "app/Application.h"
#include "app/Database.h"
#include "app/Error.h"

#include "app/SQL.h"
#include "fmt/core.h"
#include "jdbc/cppconn/resultset.h"
#include "raygui.h"

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
        DrawHeader();
        //     DrawScoreSlots();
        //     DrawKeypad();
        //     DrawActionButtons();
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

void EnterArrowInterface::DrawHeader()
{
    GuiText(fmt::format("{} {}, {}", m_FirstName, m_LastName, EquipmentNames[m_EquipmentID]),
            0,
            1,
            true);

    Range& range = m_Ranges[m_CurrentRangeIndex];

    GuiText(fmt::format("{}m {}cm", range.distanceToTargetM, range.targetFaceCm), 0, 1, true);
    GuiText(fmt::format("End N"), 0, 1);
}

void EnterArrowInterface::DrawScoreSlots()
{
}

void EnterArrowInterface::DrawKeypad()
{
}

void EnterArrowInterface::DrawActionButtons()
{
}

void EnterArrowInterface::AddSCore(int scoreValue)
{
}

std::string EnterArrowInterface::GetScoreString(int scoreValue) const
{
    return "";
}

} // namespace app
