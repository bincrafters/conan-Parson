project(Parson)
cmake_minimum_required(VERSION 2.8)

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

file(GLOB SOURCE_FILES parson/parson.c)

add_library(${CMAKE_PROJECT_NAME} ${SOURCE_FILES})

install(TARGETS ${CMAKE_PROJECT_NAME}
        DESTINATION lib
        PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ GROUP_WRITE WORLD_READ)
