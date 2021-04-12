cmake_minimum_required(VERSION 3.14)
set(CMAKE_CXX_STANDARD 14)

project(vectors_cpp)


if (UNIX)
    add_custom_target(
            preparation
            COMMAND echo "Removing old distribution files" && rm -Rf ${CMAKE_SOURCE_DIR}/dist/*
    )
else ()
    string(REPLACE / \\ WINDOWS_SOURCE_DIR ${CMAKE_SOURCE_DIR})
    add_custom_target(
            preparation
            COMMAND del /S /Q ${WINDOWS_SOURCE_DIR}\\dist\\*
    )
endif (UNIX)

add_library(
        foobar STATIC
        include/foobar.h src/foobar.cpp)

add_dependencies(foobar preparation)

set_target_properties(
        foobar PROPERTIES
        CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/dist"
        CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/dist"
        ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/dist"
)
