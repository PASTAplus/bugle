#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: test_index

:Synopsis:

:Author:
    servilla

:Created:
    2/12/22
"""
import datetime
import json

import daiquiri

from bugle.config import Config
import bugle.index.load as load
from bugle.index.index import Index


logger = daiquiri.getLogger(__name__)


def test_load_content():
    with open(f"{Config.CACHE}/content.json", "r") as f:
        content = json.loads(f.read())
    assert isinstance(content, dict)


def test_index_webpage():
    content = load.load_content(f"{Config.CACHE}/content.json")
    index: Index = load.build_index(content)
    assert isinstance(index, Index)


def test_search_index():
    content = load.load_content(f"{Config.CACHE}/content.json")
    index: Index = load.build_index(content)
    hits = index.search("Environmental")
    assert len(hits) > 0
    hits = index.search("Etiquette")
    assert len(hits) >= 2
    hits = index.search("Bullwinkle")
    assert len(hits) == 0
    hits = index.search("Etiquette", rank=True)
    assert len(hits) >= 2
    hits = index.search("Etiquette Environmental", search_type="AND", rank=True)
    assert len(hits) == 1
    hits = index.search("Etiquette Environmental", search_type="OR", rank=True)
    assert len(hits) == 4
    hits = index.search(".")
    assert len(hits) == 0
    hits = index.search("the")
    assert len(hits) == 0


def test_pkl_search_index():
    index: Index = load.from_pkl(f"{Config.CACHE}/index.pkl")
    hits = index.search("Environmental")
    assert len(hits) > 0
    hits = index.search("Etiquette")
    assert len(hits) >= 2
    hits = index.search("Bullwinkle")
    assert len(hits) == 0
    hits = index.search("Etiquette", rank=True)
    assert len(hits) >= 2
    hits = index.search("Etiquette Environmental", search_type="AND", rank=True)
    assert len(hits) == 1
    hits = index.search("Etiquette Environmental", search_type="OR", rank=True)
    assert len(hits) == 4
    hits = index.search(".")
    assert len(hits) == 0
    hits = index.search("the")
    assert len(hits) == 0
