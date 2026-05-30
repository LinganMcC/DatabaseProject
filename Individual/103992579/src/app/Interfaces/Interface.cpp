#include "app/Interfaces/Interface.h"
#include "app/Error.h"

#include "fmt/base.h"
#include "raygui.h"
#include "raylib.h"

namespace app {

Interface::Interface(std::string_view name, unsigned selectionCount, Application* app)
    : m_Name(name),
      m_App(app),
      m_MaxSelectionCount(selectionCount),
      m_SectionBounds()
{
}

void Interface::OnBegin()
{
    m_SelectedIndex = 0;
}

void Interface::HandleSelectionIndex()
{
    if (IsKeyPressed(KEY_TAB))
    {
        int inc = 1;
        if (IsKeyDown(KEY_LEFT_SHIFT) || IsKeyDown(KEY_RIGHT_SHIFT))
            inc = -1;
        m_SelectedIndex = std::abs((m_SelectedIndex + inc) % m_MaxSelectionCount);
    }
}

void Interface::ResetOffsetY()
{
    m_yOffset = GetMargin();
}

void Interface::BeginSection(std::string_view sectionTitle)
{
    m_SectionBounds = Rectangle{
        .x      = GetMargin(),
        .y      = m_yOffset,
        .width  = GetScreenWidth() - 2 * GetMargin(),
        .height = GetScreenHeight() - 2 * GetMargin(),
    };

    auto result = fmt::format_to_n(m_SectionTitle, MaxSectionTitleLength, "{}", sectionTitle);
    *result.out = '\0';

    m_yOffset += m_Padding;
}

void Interface::EndSection(bool toMargin)
{
    if (!toMargin)
        m_SectionBounds.height = m_yOffset - m_SectionBounds.y;
    GuiGroupBox(m_SectionBounds, m_SectionTitle);

    m_yOffset += 2 * m_Padding;
}

void Interface::GuiText(std::string_view text, Color color)
{

    if (color.r == 255 && color.g == 255 && color.b == 255)
        color = GetColor(GuiGetStyle(DEFAULT, TEXT_COLOR_NORMAL));

    Font font    = GuiGetFont();
    int fontSize = GuiGetStyle(DEFAULT, TEXT_SIZE);

    Vector2 size = MeasureTextEx(font, text.data(), fontSize, 0);
    Vector2 pos{
        .x = GetCenter() - size.x * 0.5f,
        .y = m_yOffset,
    };

    DrawTextEx(GuiGetFont(), text.data(), pos, fontSize, 0, color);
    m_yOffset += size.y + m_Padding;
}

float Interface::GetCenter() const
{
    return (float)GetScreenWidth() / 2;
}

float Interface::GetMargin() const
{
    return (float)GetScreenWidth() * 0.05f;
}

bool Interface::IsSelected(unsigned index) const
{
    return index == m_SelectedIndex;
}

void Interface::SetSelection(unsigned index)
{
    if (index < m_MaxSelectionCount)
    {
        m_SelectedIndex = index;
        return;
    }

    ERROR("Selection index ({}) must be less than selection max count ({})",
          index,
          m_MaxSelectionCount);
}

Rectangle Interface::GetButtonBounds(bool centered, int index, int rowCount)
{
    Rectangle bounds;
    bounds.width  = (float)GetScreenWidth() / 4;
    bounds.height = m_ButtonHeight;
    bounds.y      = m_yOffset + m_Padding;

    float offset = index * (bounds.width + m_Padding);
    if (centered)
    {
        float centerOffset = (rowCount * bounds.width) * 0.5f;
        bounds.x           = GetCenter() - centerOffset + offset;
    }
    else
        bounds.x = GetMargin() + offset;

    m_yOffset += m_ButtonHeight + 2 * m_Padding;

    return bounds;
}

} // namespace app
