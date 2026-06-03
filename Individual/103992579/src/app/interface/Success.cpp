#include "app/interface/Success.h"
#include "app/Application.h"
#include "raygui.h"

namespace app {

SuccessInterface::SuccessInterface(Application* app)
    : Interface("Success", 0, app)
{
}

void SuccessInterface::OnGUI()
{
    BeginSection("Submission Complete");
    {
        GuiText("Scores successfully recorded!", 0, 1, true, GREEN, true);

        if (GuiButton(GetBounds(0, 1, 40.0f, true, true), "Return to Setup"))
        {
            GetApp()->SetCurrentInterface("Setup", nullptr);
        }
    }
    EndSection();
}

} // namespace app
