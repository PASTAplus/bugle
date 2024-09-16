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
import json
import pathlib

import daiquiri
import pytest

from bugle.config import Config
import bugle.index.load as load
from bugle.index.index import Index


logger = daiquiri.getLogger(__name__)


@pytest.fixture
def cwd():
    cwd = pathlib.Path(".").absolute()
    if cwd.parts[-1] != "tests":
        cwd = cwd / "tests"
    return str(cwd)


def test_load_content(cwd):
    with open(f"{cwd}/data/content.json", "r") as f:
        content = json.loads(f.read())
    assert isinstance(content, dict)


def test_index_webpage(cwd):
    content = load.load_content(f"{cwd}/data/content.json")
    index: Index = load.build_index(content)
    assert isinstance(index, Index)


def test_search_index(cwd):
    content = load.load_content(f"{cwd}/data/content.json")
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
    assert len(hits) == 2
    hits = index.search("Etiquette Environmental", search_type="OR", rank=True)
    assert len(hits) == 14
    hits = index.search(".")
    assert len(hits) == 0
    hits = index.search("the")
    assert len(hits) == 0


def test_pkl_search_index():
    index: Index = load.from_pkl(f"{Config.CACHE}/index.pkl")
    hits = index.search("Environmental")
    assert len(hits) > 0
    hits = index.search("Etiquette")
    assert len(hits) == 1
    hits = index.search("Bullwinkle")
    assert len(hits) == 0
    hits = index.search("Etiquette", rank=True)
    assert len(hits) == 1
    hits = index.search("Etiquette Environmental", search_type="AND", rank=True)
    assert len(hits) == 1
    hits = index.search("Etiquette Environmental", search_type="OR", rank=True)
    assert len(hits) == 208
    hits = index.search(".")
    assert len(hits) == 0
    hits = index.search("the")
    assert len(hits) == 0
