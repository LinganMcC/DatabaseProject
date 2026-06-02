#pragma once

#include "app/DropdownView.h"
#include "raylib.h"
#include <string>

namespace app {

struct Application;

class Interface
{
    static constexpr unsigned MaxSectionTitleLength = 100;

public:
    Interface(std::string_view name, unsigned selectionCount, Application* app);
    virtual ~Interface() = default;

    virtual void OnBegin(Interface* prevInterface);
    virtual void OnGUI() = 0;
    void HandleSelectionIndex();
    void ResetOffsetY();

    const std::string& GetName() { return m_Name; }
    Application* GetApp() { return m_App; }

protected:
    void BeginSection(std::string_view title);
    void EndSection(bool toMargin = false);

    void GuiText(std::string_view text, int column = 0, int columnCount = 1, float centered = true,
                 Color color = WHITE, bool applyOffset = true);
    void GuiDropdownView(DropdownView& view, float height = 0.0f, int column = 0,
                         int columnCount = 1, bool centered = true);
    Rectangle GetButtonBounds(float height = 0.0f, int column = 0, int columnCount = 1,
                              bool centered = true, bool applyOffset = true);

    float GetCenter() const;
    float GetMargin() const;

    bool IsSelected(unsigned index) const;
    void IncrementSelection();
    void SetSelection(unsigned index);

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
