#
# Copyright 2008,2009 Free Software Foundation, Inc.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

# The presence of this file turns this directory into a Python package

'''
This is the GNU Radio PYAIS_PARSER module. Place your Python package
description here (python/__init__.py).
'''
import os

# import pybind11 generated symbols into the pyais_parser namespace
try:
    # this might fail if the module is python-only
    from .pyais_parser_python import *
except ModuleNotFoundError:
    pass

# import any pure python here
from .pyais_json import pyais_json
#
