#pragma once

namespace app {

class Application
{
public:
    Application();
    ~Application();

    void Run();

private:
    void Initialize();
    void SetupWindow();
};

} // namespace app
