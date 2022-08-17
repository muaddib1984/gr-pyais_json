find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_PYAIS_PARSER gnuradio-pyais_parser)

FIND_PATH(
    GR_PYAIS_PARSER_INCLUDE_DIRS
    NAMES gnuradio/pyais_parser/api.h
    HINTS $ENV{PYAIS_PARSER_DIR}/include
        ${PC_PYAIS_PARSER_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_PYAIS_PARSER_LIBRARIES
    NAMES gnuradio-pyais_parser
    HINTS $ENV{PYAIS_PARSER_DIR}/lib
        ${PC_PYAIS_PARSER_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-pyais_parserTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_PYAIS_PARSER DEFAULT_MSG GR_PYAIS_PARSER_LIBRARIES GR_PYAIS_PARSER_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_PYAIS_PARSER_LIBRARIES GR_PYAIS_PARSER_INCLUDE_DIRS)
