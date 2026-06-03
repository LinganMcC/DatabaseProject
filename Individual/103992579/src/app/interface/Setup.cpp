#include "app/interface/Setup.h"
#include "app/Application.h"
#include "app/DropdownView.h"
#include "app/Error.h"
#include "app/InterfaceShared.h"

#include "app/SQL.h"
#include "jdbc/cppconn/prepared_statement.h"
#include "jdbc/cppconn/resultset.h"
#include "jdbc/cppconn/sqlstring.h"
#include "raygui.h"
#include "raylib.h"
#include <string_view>

namespace app {

static constexpr std::string_view QueryArcherExists =
    R"(
SELECT
    DefaultEquipmentID
FROM Archer
WHERE
    FirstName = ?
    AND LastName = ?;
    )";

static constexpr std::string_view QueryRoundNames =
    R"(
SELECT
    br.RoundName
FROM BaseRound br
WHERE EXISTS (
    SELECT 1
    FROM EquivalentRound eqr
    WHERE eqr.BaseRoundID = br.BaseRoundID
      AND eqr.EquipmentID = ?
)
ORDER BY
    br.RoundName;
    )";

SetupInterface::SetupInterface(Application* app)
    : Interface("Setup", 3, app)
{
    m_FirstName[0] = '\0';
    m_LastName[0]  = '\0';

    for (const std::string_view& equipment : EquipmentNames)
        m_Equipment.AddEntry(equipment);
}

void SetupInterface::Reset()
{
    Interface::Reset();

    m_FirstName[0]          = '\0';
    m_LastName[0]           = '\0';
    m_ShowArcherNotFound    = false;
    m_FoundArcher           = 0;
    m_Equipment.ActiveIndex = -1;

    m_Rounds.Clear();
}

void SetupInterface::OnGUI()
{
    ChooseArcher();
    ChooseRound();

    if (GuiButton(GetBounds(), "Clear"))
        Reset();
}

void SetupInterface::ChooseArcher()
{
    BeginSection("Choose Archer");
    {
        if (m_FoundArcher > 0)
        {
            int len = std::strlen(m_FirstName) + std::strlen(m_LastName);
            if (len != m_FoundArcher)
                m_FoundArcher = 0;
        }

        if (GuiTextBox(GetBounds(0, 2), m_FirstName, MaxNameInput, IsSelected(0)))
            SetSelection(0);

        if (GuiTextBox(GetBounds(1, 2), m_LastName, MaxNameInput, IsSelected(1)))
            SetSelection(1);

        if (GuiButton(GetBounds(), "Find Archer"))
        {
            SelectSQL select(QueryArcherExists);
            select.Bind(m_FirstName);
            select.Bind(m_LastName);

            if (select.Execute())
            {
                m_Equipment.ActiveIndex = -1;
                if (select.GetResults()->next())
                {
                    m_Equipment.ActiveIndex = select.GetResults()->getInt(1) - 1;
                }

                if (m_Equipment.ActiveIndex != -1)
                {
                    m_FoundArcher        = std::strlen(m_FirstName) + std::strlen(m_LastName);
                    m_ShowArcherNotFound = false;
                    SetSelection(99);

                    LoadAvailableRounds();
                }
                else
                {
                    Reset();
                    m_ShowArcherNotFound = true;
                }
            }
        }

        if (m_ShowArcherNotFound)
            GuiText("Archer doesn't exist", 0, 1, true, RED);
    }
    EndSection();
}

void SetupInterface::ChooseRound()
{
    if (!m_FoundArcher)
        return;

    BeginSection("Choose Round");
    {
        GuiText("Select Equipment", 0, 2);
        GuiText("Select Round", 1, 2);

        int lastSelected = m_Equipment.ActiveIndex;
        GuiDropdownView(m_Equipment, 0, 2, 200.0f);
        if (lastSelected != m_Equipment.ActiveIndex)
            LoadAvailableRounds();

        GuiDropdownView(m_Rounds, 1, 2, 200.0f);

        if (m_Rounds.ActiveIndex != -1)
        {
            if (GuiButton(GetBounds(), "Enter Arrows"))
            {
                TransitionToEnterArrowDataPackage package{
                    .firstName   = m_FirstName,
                    .lastName    = m_LastName,
                    .roundName   = m_Rounds.Names[m_Rounds.ActiveIndex],
                    .equipmentID = m_Equipment.ActiveIndex,
                };
                GetApp()->SetCurrentInterface("Enter Arrow", &package);
            }
        }
    }
    EndSection();
}

void SetupInterface::LoadAvailableRounds()
{
    ASSERT(m_Equipment.ActiveIndex != -1,
           "Cannot call this function if the equipment ID has not been set");

    m_Rounds.Clear();

    SelectSQL select(QueryRoundNames);
    select.Bind(m_Equipment.ActiveIndex + 1);

    if (!select.Execute())
        FATAL("Failed to execute Query:\n{}\n", QueryRoundNames);

    sql::ResultSet* results = select.GetResults();
    if (!results)
        FATAL("Failed");

    while (results->next())
        m_Rounds.AddEntry(results->getString(1).c_str());
}

} // namespace app
