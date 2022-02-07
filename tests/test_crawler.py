#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: test_crawler

:Synopsis:

:Author:
    servilla

:Created:
    2/6/22
"""
import pytest

from bugle.scrape.config import Config
from bugle.scrape.crawler import Crawler
from bugle.scrape.page import Page


def test_crawl():
    crawler = Crawler(host="https://web-x.edirepository.org", path=Config.PATH, callback=page_bugle)
    crawler.crawl()
    print(crawler.visited)


def page_bugle(**kwargs):
    page: Page = kwargs["page"]
    print(page.url)
    path: str = kwargs["path"]
    print(path)
