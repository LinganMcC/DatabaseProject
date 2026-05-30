#include "app/App.h"

#include <cassert>

#include "raygui.h"
#include "raylib.h"

namespace app {

Application::Application()
{
    SetupWindow();
}

Application::~Application()
{
    CloseWindow();
}

void Application::Run()
{
    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(BLACK);

        DrawText("This is a test", GetScreenWidth() / 2, GetScreenHeight() / 2, 16, WHITE);

        EndDrawing();
    }
}

void Application::Initialize()
{
    SetTraceLogLevel(LOG_WARNING);
}

void Application::SetupWindow()
{
    InitWindow(0, 0, "Archery Entry App");
    assert(IsWindowReady() && "Failed to initialize Raylib's window for some reason");

    int monitor = GetCurrentMonitor();
    int width   = GetMonitorWidth(monitor) / 2;
    int height  = GetMonitorHeight(monitor) / 2;

    SetWindowSize(width, height);
    SetWindowPosition(width / 2, height / 2); // Center window

    SetExitKey(NULL);
    SetTargetFPS(60);
}

} // namespace app
