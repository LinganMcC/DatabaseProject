#include "app/Application.h"

#include "app/Error.h"
#include "app/Interfaces/ChooseArcher.h"
#include "app/Interfaces/EnterArrow.h"
#include "app/Interfaces/Interface.h"

#include "raygui.h"
#include "raylib.h"
#include <memory>

namespace app {

Application::Application()
{
    SetupWindow();
    SetupGUI();

    LoadInterfaces();
}

Application::~Application()
{
    UnloadFont(m_MainFont);
    CloseWindow();
}

void Application::Run()
{
    Color clearColor = GetColor(GuiGetStyle(DEFAULT, BACKGROUND_COLOR));
    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(clearColor);

        m_Interfaces[m_CurrentInterface]->HandleSelectionIndex();
        m_Interfaces[m_CurrentInterface]->ResetOffsetY();
        m_Interfaces[m_CurrentInterface]->OnGUI();

        EndDrawing();
    }
}

void Application::SetupWindow()
{
    SetTraceLogLevel(LOG_WARNING);
    SetConfigFlags(FLAG_WINDOW_RESIZABLE);
    InitWindow(0, 0, "Archery Entry App");
    ASSERT(IsWindowReady(), "Failed to initialize Raylib's window for some reason");

    SetWindowMinSize(270, 600);

    int monitor = GetCurrentMonitor();
    int width   = GetMonitorWidth(monitor) / 2;
    int height  = GetMonitorHeight(monitor) / 2;

    SetWindowSize(width, height);
    SetWindowPosition(width / 2, height / 2); // Center window

    SetExitKey(NULL);
    SetTargetFPS(60);
}

void Application::SetupGUI()
{
    GuiLoadStyle(ASSET_DIRECTORY "/style/style_dark.rgs");

    int fontSize = 24;
    m_MainFont   = LoadFontEx(ASSET_DIRECTORY "/style/font/Roboto-Regular.ttf", fontSize, 0, 0);
    SetTextureFilter(m_MainFont.texture, TEXTURE_FILTER_BILINEAR);
    GuiSetFont(m_MainFont);

    GuiSetStyle(DEFAULT, TEXT_SIZE, fontSize);
}

void Application::LoadInterfaces()
{
    m_Interfaces.push_back(std::make_unique<ChooseArcherInterface>(this));
    m_Interfaces.push_back(std::make_unique<EnterArrowInterface>(this));
}

void Application::SetCurrentInterface(std::string_view name)
{
    for (unsigned i = 0; i < m_Interfaces.size(); i++)
    {
        if (m_Interfaces[i]->GetName() == name)
        {
            m_CurrentInterface = i;
            return;
        }
    }
    FATAL("Failed to load {} Interface, doesn't exist", name);
}

} // namespace app
