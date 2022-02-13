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

import daiquiri

from bugle.config import Config
from bugle.index.index import Index
from bugle.index.webpage import WebPage


logger = daiquiri.getLogger(__name__)


def load_content(path: str) -> Index:
    with open(path, "r") as f:
        content = json.loads(f.read())

    index = Index()
    for i, page_url in enumerate(content):
        webpage = WebPage(ID=i, content=content[page_url], url=page_url)
        index.index_document(webpage)

    return index
