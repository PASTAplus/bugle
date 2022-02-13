#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: document

:Synopsis:

:Author:
    servilla

:Created:
    2/9/22
"""
from collections import Counter
from dataclasses import dataclass

from bugle.index.analysis import analyze


@dataclass
class WebPage:
    ID: int
    content: str
    url: str

    @property
    def fulltext(self):
        return self.content

    def analyze(self):
        self.term_frequencies = Counter(analyze(self.fulltext))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)
