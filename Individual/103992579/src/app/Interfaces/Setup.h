#pragma once

#include "app/DropdownView.h"
#include "app/Interfaces/Interface.h"

namespace app {

class SetupInterface : public Interface
{
    static constexpr unsigned MaxNameInput = 30;

public:
    SetupInterface(Application* app);

    void OnBegin(Interface* prevInterface) override;
    void OnGUI() override;

private:
    void ChooseArcher();
    void ChooseRound();

    void LoadAvailableRounds();

    char m_FirstName[MaxNameInput];
    char m_LastName[MaxNameInput];
    bool m_ShowArcherNotFound = false;
    int m_FoundArcher         = 0;

    DropdownView m_Rounds;
    DropdownView m_Equipment;
};

} // namespace app
