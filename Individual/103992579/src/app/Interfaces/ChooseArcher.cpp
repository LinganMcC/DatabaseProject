#include "app/Interfaces/ChooseArcher.h"
#include "app/Interfaces/Interface.h"

#include "fmt/format.h"
#include "jdbc/cppconn/prepared_statement.h"
#include "jdbc/cppconn/resultset.h"
#include "raygui.h"
#include "raylib.h"
#include <cstring>
#include <string_view>

namespace app {

static constexpr std::string_view QueryArcherExists = //
    "SELECT "
    "COUNT(*) "
    "FROM Archer a "
    "WHERE "
    "a.FirstName = ? "
    "    AND a.LastName = ?;";

ChooseArcherInterface::ChooseArcherInterface(Application* app)
    : Interface("Choose Arhcer", 2, app)
{
    m_FirstName[0] = '\0';
    m_LastName[0]  = '\0';
}

void ChooseArcherInterface::OnBegin()
{
    Interface::OnBegin();

    m_FirstName[0]       = '\0';
    m_LastName[0]        = '\0';
    m_ShowArcherNotFound = false;
    m_FoundArcher        = 0;
}

void ChooseArcherInterface::OnGUI()
{
    ChooseArcher();
    ChooseRound();
}

void ChooseArcherInterface::ChooseArcher()
{
    BeginSection("Choose Archer");
    {
        if (m_FoundArcher > 0)
        {
            int len = std::strlen(m_FirstName) + std::strlen(m_LastName);
            if (len != m_FoundArcher)
                m_FoundArcher = 0;
        }

        Rectangle bounds;
        bounds.width  = (float)GetScreenWidth() / 3;
        bounds.height = 40;
        bounds.x      = GetCenter() - (bounds.width + m_Padding);
        bounds.y      = m_yOffset;

        if (GuiTextBox(bounds, m_FirstName, MaxNameInput, IsSelected(0)))
            SetSelection(0);

        bounds.x = GetCenter() + m_Padding;
        if (GuiTextBox(bounds, m_LastName, MaxNameInput, IsSelected(1)))
            SetSelection(1);

        m_yOffset += bounds.height;

        if (GuiButton(GetButtonBounds(), "Find Archer") || IsKeyPressed(KEY_ENTER))
        {
            bool found    = false;
            auto bindFunc = [&](sql::PreparedStatement* stmt)
            {
                stmt->setString(1, m_FirstName);
                stmt->setString(2, m_LastName);
            };
            auto readFunc = [&](sql::ResultSet* res)
            {
                if (res->next())
                {
                    int count = res->getInt(1);
                    found     = count > 0;
                }
            };

            if (QuerySQL(QueryArcherExists, bindFunc, readFunc))
            {
                if (found)
                {
                    m_FoundArcher        = std::strlen(m_FirstName) + std::strlen(m_LastName);
                    m_ShowArcherNotFound = false;
                }
                else
                {
                    OnBegin();
                    m_ShowArcherNotFound = true;
                }
            }
        }

        if (m_ShowArcherNotFound)
        {
            GuiText("Archer doesn't exist", RED);
        }
    }
    EndSection();
}

void ChooseArcherInterface::ChooseRound()
{
    if (!m_FoundArcher)
        return;

    BeginSection("Choose Round");
    {
        m_yOffset += 20;
    }
    EndSection();
}

} // namespace app
