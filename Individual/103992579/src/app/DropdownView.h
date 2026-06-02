#pragma once

#include <string_view>
#include <vector>

namespace app {

struct DropdownView
{
    ~DropdownView();

    std::vector<char*> Names;
    int ScrollIndex = 0;
    int ActiveIndex = -1;

    void AddEntry(std::string_view entry);
    void Clear();
};

} // namespace app
