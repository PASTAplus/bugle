#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: __init__

:Synopsis:

:Author:
    servilla

:Created:
    2/6/22
"""
import logging
import pathlib
import sys

import daiquiri

cwd = pathlib.Path(".").absolute()
if cwd.parts[-1] != "tests":
    cwd = cwd / "tests"
print(cwd)
print(cwd.parent)
logfile = f"{cwd}/tests.log"
daiquiri.setup(
    level=logging.INFO,
    outputs=(daiquiri.output.File(logfile), "stdout",)
)
logger = daiquiri.getLogger(__name__)
sys.path.insert(0, f"{cwd.parent}/src")
