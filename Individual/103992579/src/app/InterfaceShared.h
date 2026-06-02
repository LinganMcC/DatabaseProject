#pragma once

#include <array>
#include <string>
#include <string_view>

namespace app {

static constexpr std::array<std::string_view, 5> EquipmentNames = {
    "Recurve",
    "Compound",
    "Recurve Barebow",
    "Compound Barebow",
    "Longbow",
};

struct TransitionToEnterArrowDataPackage
{
    std::string firstName;
    std::string lastName;
    std::string roundName;
    int equipmentID;
};

} // namespace app
