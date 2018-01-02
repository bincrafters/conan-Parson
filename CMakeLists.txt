cmake_minimum_required(VERSION 2.8)
project(parson C)

# Conan Setup ##################################################################
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Export all symbols when build DLL on MSVC ####################################
if (WIN32 AND MSVC AND BUILD_SHARED_LIBS)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif(MSVC AND BUILD_SHARED_LIBS)

# Build target #################################################################
add_library(${CMAKE_PROJECT_NAME} parson/parson.c parson/parson.h)

# Enable warnings when GCC or Clang ############################################
if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang" OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE -Wall -Wextra -std=c89 -pedantic-errors)
endif("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang" OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")

# Install target ###############################################################
install(TARGETS ${CMAKE_PROJECT_NAME}
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        RUNTIME DESTINATION bin
        PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ GROUP_WRITE WORLD_READ)
install(FILES parson/parson.h DESTINATION include)
