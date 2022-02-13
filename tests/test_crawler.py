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

from bs4 import BeautifulSoup
from bugle.crawl.crawler import Crawler
from bugle.crawl.page import Page


def test_crawl():
    print("\n")
    crawler = Crawler(url="http://localhost:8000/")
    crawler.crawl(selectors=("title",), allow="^/", follow=True)
    print(crawler.visited)
