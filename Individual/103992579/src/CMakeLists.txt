# Dependencies
# =================================================================================================

include(FetchContent)
MACRO(fetch_content name repo tag)
    FetchContent_Declare(
        ${name}
        GIT_REPOSITORY ${repo}
        GIT_TAG ${tag}
        GIT_PROGRESS TRUE
    )
    FetchContent_MakeAvailable(${name})
ENDMACRO()

# Raylib
set(BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)

fetch_content(libfmt        https://github.com/fmtlib/fmt.git     "12.1.0")
fetch_content(raylib        https://github.com/raysan5/raylib.git "5.5")
fetch_content(raygui        https://github.com/raysan5/raygui.git "4.0")

# Setup Raygui library, because its a STB style library
set(RAYGUI_IMPL_FILE "${CMAKE_CURRENT_BINARY_DIR}/RayguiImpl.c")
file(WRITE ${RAYGUI_IMPL_FILE} "#define RAYGUI_IMPLEMENTATION\n#include \"raygui.h\"\n")
add_library(raygui STATIC ${RAYGUI_IMPL_FILE})
message("Raylib GUI path: ${raygui_SOURCE_DIR}")
target_include_directories(raygui
PUBLIC
    ${raygui_SOURCE_DIR}/src
)
target_compile_definitions(raygui
PRIVATE
    _CRT_SECURE_NO_WARNINGS
)
target_link_libraries(raygui
PUBLIC
    raylib
)

# Executable
# =================================================================================================

add_executable(${CMAKE_PROJECT_NAME})

add_subdirectory(app)

target_include_directories(${CMAKE_PROJECT_NAME}
PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/vender/include
)

target_compile_definitions(${CMAKE_PROJECT_NAME}
PRIVATE
    ASSET_DIRECTORY="${ASSET_DIRECTORY}"
    STATIC_CONCPP
    CPPCONN_PUBLIC_FUNC=
    $<$<CONFIG:RelWithDebInfo>:ENABLE_ASSERTS>
    $<$<CONFIG:Debug>:ENABLE_ASSERTS>
)

target_link_libraries(${CMAKE_PROJECT_NAME}
PRIVATE
    fmt::fmt
    raylib
    raygui
    ${CMAKE_CURRENT_SOURCE_DIR}/vender/lib64/vs14/mysqlcppconn-static.lib
)

if (MSVC)
    target_compile_options(${CMAKE_PROJECT_NAME}
    PUBLIC
        /Zc:preprocessor # Needed for __VA_OPT__() macro
    )
endif()
