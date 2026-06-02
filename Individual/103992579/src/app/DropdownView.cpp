#include "app/DropdownView.h"

#include "raygui.h"

namespace app {

DropdownView::~DropdownView()
{
    Clear();
}

void DropdownView::AddEntry(std::string_view entry)
{
    char* buffer = (char*)std::malloc(sizeof(char) * entry.size() + 1);
    std::strncpy(buffer, entry.data(), entry.length());
    buffer[entry.length()] = '\0';

    Names.push_back(buffer);
}

void DropdownView::Clear()
{
    for (char* name : Names)
        std::free(name);

    Names.clear();
    ScrollIndex = 0;
    ActiveIndex = -1;
}

} // namespace app
