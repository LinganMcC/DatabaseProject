#pragma once

#include "app/Interfaces/Interface.h"

#include <vector>

namespace app {

class EnterArrowInterface : public Interface
{
    struct End
    {
        static constexpr unsigned MaxArrowCount = 6;

        std::vector<int> arrowScores;
    };

    struct Range
    {
        unsigned rangeID;
        unsigned distanceToTargetM;
        unsigned targetFaceCm;
        unsigned numberOfEnds;

        std::vector<End> ends;
    };

public:
    EnterArrowInterface(Application* app);

    void OnGUI() override;
    bool LoadTransitionData(void* transitionData) override;

private:
    void DrawHeader();
    void DrawScoreSlots();
    void DrawKeypad();
    void DrawActionButtons();

    void AddSCore(int scoreValue);
    std::string GetScoreString(int scoreValue) const;

    std::string m_FirstName;
    std::string m_LastName;

    std::string m_RoundName;
    int m_RoundID;
    int m_EquipmentID;

    unsigned m_CurrentRangeIndex = 0;
    std::vector<Range> m_Ranges;
};

} // namespace app
