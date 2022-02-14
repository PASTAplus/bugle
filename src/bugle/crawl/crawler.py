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
from urllib.parse import urlparse

import daiquiri
from bs4 import BeautifulSoup

from bugle.crawl.page import Page


logger = daiquiri.getLogger(__name__)


class Crawler:
    def __init__(self, url: str):
        self._url = url
        self._visited = set()
        self._url_parse = urlparse(self._url)
        self._url_prefix = f"{self._url_parse.scheme}://{self._url_parse.netloc}"
        self._index_content = {}

    @property
    def index_content(self):
        return self._index_content

    @property
    def visited(self):
        return self._visited

    def crawl(self, selectors: tuple, url: str = None, allow: str = None, follow: bool = False):

        url = self._url if url is None else url

        try:
            page = Page(url)
            self._visited.add(url)

            soup = BeautifulSoup(page.html, "lxml")

            index_text = ""
            for selector in selectors:
                elements = soup.find_all(selector)
                for element in elements:
                    index_text += " ".join([_.strip() for _ in element.strings])

            self._index_content[page.url] = index_text

            if follow:
                for link in page.links:
                    url = f"{self._url_prefix}{link}" if not link.startswith(self._url_prefix) else link
                    if url not in self._visited:
                        if allow and re.search(allow, link):
                            self.crawl(selectors, url, allow, follow)

        except Exception as ex:
            logger.error(ex)
