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

from bugle.crawl.page import Page


logger = daiquiri.getLogger(__name__)


class Crawler:
    def __init__(self, host: str):
        self._host = host
        self._visited = set()

    @property
    def visited(self):
        return self._visited

    def crawl(self, path: str, allow: str = None, follow: bool = False, callback: object = None):
        self._visited = set.union(
            _crawl(self._host, path, allow=allow, follow=follow, callback=callback, visited=self._visited),
                   self._visited)


def _crawl(
        host: str,
        path: str,
        allow: str = "*",
        follow: bool = False,
        callback=None,
        visited: set = None
) -> set:

    url = path if path.startswith("http") else host + path

    try:
        page = Page(url)
        visited.add(path)

        if callback:
            callback(url=url, host=host, path=path, allow=allow, follow=follow, visited=visited, page=page)

        if follow:
            for link in page.links:
                if link not in visited:
                    if allow and re.search(allow, link):
                        visited = _crawl(host, link, allow, follow, callback, visited)

    except Exception as ex:
        logger.error(ex)

    return visited
