#include "app/Interfaces/EnterArrow.h"
#include "app/Interfaces/Interface.h"

namespace app {

EnterArrowInterface::EnterArrowInterface(Application* app)
    : Interface("Enter Arrow", 0, app)
{
}

void EnterArrowInterface::OnGUI()
{
}

} // namespace app
