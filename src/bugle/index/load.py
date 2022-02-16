#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: load

:Synopsis:

:Author:
    servilla

:Created:
    2/12/22
"""
import json
import pickle

import daiquiri

from bugle.index.index import Index
from bugle.index.webpage import WebPage


logger = daiquiri.getLogger(__name__)


def load_content(content_path: str) -> dict:
    with open(content_path, "r") as f:
        return json.loads(f.read())


def build_index(content: dict) -> Index:
    index = Index()
    for i, page_url in enumerate(content):
        webpage = WebPage(ID=i, content=content[page_url], url=page_url)
        index.index_document(webpage)
    return index


def from_pkl(index_path: str) -> Index:
    with open(index_path, "rb") as f:
        index = pickle.load(f)
    return index

