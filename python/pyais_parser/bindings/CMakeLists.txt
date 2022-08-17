# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT pyais_parser_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT pyais_parser_sources)

########################################################################
# Check for pygccxml
########################################################################
GR_PYTHON_CHECK_MODULE_RAW(
    "pygccxml"
    "import pygccxml"
    PYGCCXML_FOUND
    )

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND pyais_parser_python_files
    python_bindings.cc)

GR_PYBIND_MAKE_OOT(pyais_parser
   ../../..
   gr::pyais_parser
   "${pyais_parser_python_files}")

# copy bindings extension for use in QA test module
add_custom_command(TARGET pyais_parser_python POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:pyais_parser_python>
    ${PROJECT_BINARY_DIR}/test_modules/gnuradio/pyais_parser/
)

install(TARGETS pyais_parser_python DESTINATION ${GR_PYTHON_DIR}/gnuradio/pyais_parser COMPONENT pythonapi)
