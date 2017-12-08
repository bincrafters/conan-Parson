cmake_minimum_required(VERSION 2.8)
project(parson)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if (WIN32 AND MSVC AND BUILD_SHARED_LIBS)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif(MSVC AND BUILD_SHARED_LIBS)

file(GLOB SOURCE_FILES parson/parson.c)
add_library(${CMAKE_PROJECT_NAME} ${SOURCE_FILES})

install(TARGETS ${CMAKE_PROJECT_NAME}
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        RUNTIME DESTINATION bin
        PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ GROUP_WRITE WORLD_READ)
install(FILES parson/parson.h DESTINATION include)
