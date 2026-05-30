#pragma once

#include "app/Interfaces/Interface.h"

namespace app {

class EnterArrowInterface : public Interface
{
public:
    EnterArrowInterface(Application* app);

    void OnGUI() override;

private:
};

} // namespace app
