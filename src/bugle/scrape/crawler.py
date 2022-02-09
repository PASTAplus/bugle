#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: crawler

:Synopsis:

:Author:
    servilla

:Created:
    2/6/22
"""
import re

import daiquiri

from bugle.scrape.page import Page


logger = daiquiri.getLogger(__name__)


class Crawler:
    def __init__(self, host: str, path: str = "/"):
        self._host = host
        self._path = path
        self._visited = None

    @property
    def visited(self):
        return self._visited

    def crawl(self, allow: str = None, callback: object = None):
        self._visited = _crawl(self._host, self._path, allow=allow, callback=callback)


def _crawl(
        host: str,
        path: str,
        allow: str = "*",
        visited: list = None,
        callback=None
) -> list:

    if visited is None:
        visited = []

    url = path if path.startswith("http") else host + path

    try:
        page = Page(url)
        visited.append(path)

        if callback:
            callback(url=url, host=host, path=path, allow=allow, visited=visited, page=page)

        for link in page.links:
            if link not in visited:
                if allow and re.search(allow, link):
                    visited = _crawl(host, link, allow, visited, callback)
    except Exception as ex:
        logger.error(ex)

    return visited
