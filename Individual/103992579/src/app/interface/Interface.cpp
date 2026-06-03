#include "app/interface/Interface.h"

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

void Interface::Reset()
{
    m_SelectedIndex = 0;
}

bool Interface::LoadTransitionData(void* transitionData)
{
    return true;
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
    m_yOffset += m_Padding;

    if (!toMargin)
        m_SectionBounds.height = m_yOffset - m_SectionBounds.y;
    GuiGroupBox(m_SectionBounds, m_SectionTitle);

    m_yOffset += 2 * m_Padding;
}

void Interface::GuiText(std::string_view text, int column, int columnCount, float centered,
                        Color color, bool applyOffset)
{
    if (color.r == 255 && color.g == 255 && color.b == 255)
        color = GetColor(GuiGetStyle(DEFAULT, TEXT_COLOR_NORMAL));

    Font font    = GuiGetFont();
    int fontSize = GuiGetStyle(DEFAULT, TEXT_SIZE);

    Rectangle bounds = GetBounds(column, columnCount, 0.0f, centered, false);
    Vector2 size     = MeasureTextEx(font, text.data(), fontSize, 0);
    Vector2 pos{
        .x = (bounds.x + bounds.width * 0.5f) - size.x * 0.5f,
        .y = bounds.y,
    };

    DrawTextEx(GuiGetFont(), text.data(), pos, fontSize, 0, color);
    if (applyOffset && column == columnCount - 1)
        m_yOffset += size.y + m_Padding;
}

void Interface::GuiDropdownView(DropdownView& view, int column, int columnCount, float height,
                                bool centered)
{
    Rectangle bounds = GetBounds(column, columnCount, height, centered);
    int focus        = -1;
    GuiListViewEx(bounds,
                  const_cast<const char**>(view.Names.data()),
                  (int)view.Names.size(),
                  &view.ScrollIndex,
                  &view.ActiveIndex,
                  &focus);
}

Rectangle Interface::GetBounds(int column, int columnCount, float height, bool centered,
                               bool applyOffset)
{
    height = height == 0.0f ? m_ButtonHeight : height;
    float width =
        GetScreenWidth() - 2 * (GetMargin() + m_Padding) - ((columnCount - 1) * m_Padding);

    Rectangle bounds{
        .x      = 0,
        .y      = m_yOffset + m_Padding,
        .width  = width / columnCount,
        .height = height,
    };

    float offset = column * (bounds.width + m_Padding);
    if (centered)
    {
        float totalColumnWidth = (columnCount * bounds.width) + ((columnCount - 1) * m_Padding);
        float centerOffset     = totalColumnWidth * 0.5f;
        bounds.x               = GetCenter() - centerOffset + offset;
    }
    else
        bounds.x = GetMargin() + m_Padding + offset;

    if (applyOffset && column == columnCount - 1)
        m_yOffset += height + m_Padding;

    return bounds;
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
    m_SelectedIndex = index;
}

} // namespace app
