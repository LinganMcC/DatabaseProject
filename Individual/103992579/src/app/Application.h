#pragma once

#include "app/interface/Interface.h"

#include "raylib.h"
#include <memory>
#include <string_view>
#include <vector>

namespace app {

struct Application
{
    Application();
    ~Application();

    void Run();
    void SetCurrentInterface(std::string_view name, void* transitionData);

private:
    void SetupWindow();
    void SetupGUI();
    void LoadInterfaces();

    std::vector<std::unique_ptr<Interface>> m_Interfaces;
    unsigned m_CurrentInterface = 0;
    Font m_MainFont;
};

} // namespace app
