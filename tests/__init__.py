#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: __initi__

:Synopsis:

:Author:
    servilla

:Created:
    2/6/22
"""
import logging
import os
import sys

import daiquiri


cwd = os.path.dirname(os.path.realpath(__file__))
logfile = cwd + "/tests.log"
daiquiri.setup(level=logging.DEBUG,
               outputs=(daiquiri.output.File(logfile), "stdout",))
logger = daiquiri.getLogger(__name__)


sys.path.insert(0, os.path.abspath("../src"))
test_data_path = os.path.abspath(os.path.dirname(__file__)) + "/data"
