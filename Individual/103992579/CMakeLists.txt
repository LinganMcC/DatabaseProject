cmake_minimum_required(VERSION 3.30)

# Libraries linked via full path != linker search path error
cmake_policy(SET CMP0003 NEW)
# Syntax problems are errors
cmake_policy(SET CMP0010 NEW)

# Removes unnecessary cmake files when generating MSVC project files
set(CMAKE_SUPPRESS_REGENERATION TRUE)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED 20)

set(BINARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/build/${CMAKE_BUILD_TYPE}")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${BINARY_OUTPUT_DIRECTORY}/Archive")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${BINARY_OUTPUT_DIRECTORY}")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${BINARY_OUTPUT_DIRECTORY}")

project("archery-frontend"
    VERSION 0.0.1
    LANGUAGES CXX C
)

add_subdirectory(src)
