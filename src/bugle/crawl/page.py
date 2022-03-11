#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: page

:Synopsis:
    Creates a scraped web page object
:Author:
    servilla

:Created:
    2/6/22
"""
from bs4 import BeautifulSoup
import daiquiri
import requests

logger = daiquiri.getLogger(__name__)


class Page:

    def __init__(self, url: str):
        self._url = url
        response = requests.get(self._url)
        response.raise_for_status()
        self._response = response
        self._html = response.text
        self._soup = BeautifulSoup(self._html, "lxml")

    @property
    def url(self) -> str:
        return self._url

    @property
    def html(self) -> str:
        return self._html

    @property
    def links(self) -> list:
        return self._get_links()

    def _get_links(self):
        links = []
        for link in self._soup.find_all("a"):
            l = link.get("href")
            if "#" not in l:  # Ignore links with page anchors
                links.append(l)
        return links
