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

from bs4 import BeautifulSoup
from bugle.scrape.config import Config
from bugle.scrape.crawler import Crawler
from bugle.scrape.page import Page


def test_crawl():
    print("\n")
    crawler = Crawler(host="http://localhost:8000", path=Config.PATH)
    crawler.crawl(allow="^/", callback=page_bugle)
    print(crawler.visited)


def page_bugle(**kwargs):
    page: Page = kwargs["page"]
    # print(page.url)
    visited: list = kwargs["visited"]
    # print(visited)
    soup = BeautifulSoup(page.html, "lxml")
    main_tag = soup.main
    if main_tag is not None:
        index_text = " ".join([_.strip() for _ in main_tag.strings])
        print(f"{page.url}: {index_text}")
