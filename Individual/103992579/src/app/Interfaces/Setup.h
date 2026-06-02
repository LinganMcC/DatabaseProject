#pragma once

#include "app/Interfaces/Interface.h"

namespace app {

class SetupInterface : public Interface
{
    static constexpr unsigned MaxNameInput = 30;

public:
    SetupInterface(Application* app);

    void OnBegin() override;
    void OnGUI() override;

private:
    void ChooseArcher();
    void ChooseRound();

    char m_FirstName[MaxNameInput];
    char m_LastName[MaxNameInput];

    bool m_ShowArcherNotFound = false;
    int m_FoundArcher         = 0;
};

} // namespace app
