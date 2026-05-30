#pragma once

#include "jdbc/cppconn/connection.h"
#include "jdbc/cppconn/prepared_statement.h"
#include "jdbc/cppconn/resultset.h"
#include "raylib.h"
#include <functional>
#include <string>

namespace app {

struct Application;

class Interface
{
    static constexpr unsigned MaxSectionTitleLength = 100;

public:
    using Pfn_PrepareStatement = std::function<void(sql::PreparedStatement* prepStatement)>;
    using Pfn_ReadResult       = std::function<void(sql::ResultSet* result)>;

    Interface(std::string_view name, unsigned selectionCount, Application* app);
    virtual ~Interface() = default;

    virtual void OnBegin();
    virtual void OnGUI() = 0;
    void HandleSelectionIndex();
    void ResetOffsetY();

    const std::string& GetName() { return m_Name; }
    Application* GetApp() { return m_App; }

protected:
    void BeginSection(std::string_view title);
    void EndSection(bool toMargin = false);
    void GuiText(std::string_view text, Color color = WHITE);

    float GetCenter() const;
    float GetMargin() const;

    bool IsSelected(unsigned index) const;
    void IncrementSelection();
    void SetSelection(unsigned index);

    Rectangle GetButtonBounds(bool centered = true, int index = 0, int rowCount = 1);

    sql::Connection* GetConnection() const;
    bool QuerySQL(std::string_view query, Pfn_PrepareStatement bindFunc,
                  Pfn_ReadResult readFunc) const;
    bool InsertSQL(std::string_view statement, Pfn_PrepareStatement stmtFunc) const;

    float m_ButtonHeight = 40.0f;
    float m_yOffset      = 0.0f;
    float m_Padding      = 15.0f;
    float m_Margin       = 40.0f;

private:
    std::string m_Name;
    Application* m_App;

    int m_SelectedIndex = 0;
    int m_MaxSelectionCount;
    char m_SectionTitle[MaxSectionTitleLength];
    Rectangle m_SectionBounds;
};

} // namespace app
