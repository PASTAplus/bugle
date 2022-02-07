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

from bugle.scrape.config import Config

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
            links.append(link.get("href"))
        return links

    def text(self, selector: str = None, raw: bool = False) -> str:
        page_text = ""
        raw_text = self._soup.get_text()
        if selector is None:
            if raw:
                page_text = raw_text
            else:
                page_text = " ".join(raw_text.split())
        return page_text
