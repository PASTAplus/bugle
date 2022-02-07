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

from bugle.scrape.page import Page


class Crawler:
    def __init__(self, host: str, path: str = "/", callback: object = None):
        self._host = host
        self._path = path
        self._visited = None
        self._callback = callback

    @property
    def visited(self):
        return self._visited

    def crawl(self):
        self._visited = _crawl(self._host, self._path, allow="^/", callback=self._callback)


def _crawl(
        host: str,
        path: str,
        allow: str = "*",
        deny: str = None,
        visited: list = None,
        callback=None
) -> list:

    if visited is None:
        visited = []

    url = path if path.startswith("http") else host + path

    page = Page(url)

    if callback is not None:
        callback(url=url, host=host, path=path, allow=allow, deny=deny, visited=visited, page=page)

    visited.append(path)
    for link in page.links:
        if link not in visited:
            if allow and re.search(allow, link):
                visited = _crawl(host, link, allow, deny, visited, callback)
            elif deny and not re.search(deny, link):
                visited = _crawl(host, link, allow, deny, visited, callback)
    return visited
