#pragma once

#include "app/interface/Interface.h"

namespace app {

class SuccessInterface : public Interface
{
public:
    SuccessInterface(Application* app);

    void OnGUI() override;
};

} // namespace app
