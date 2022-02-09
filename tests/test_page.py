#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: test_page

:Synopsis:

:Author:
    servilla

:Created:
    2/6/22
"""
import daiquiri
import pytest

from bugle.crawl.config import Config
from bugle.crawl.page import Page


logger = daiquiri.getLogger(__name__)


@pytest.fixture
def page():
    return Page(Config.HOST, Config.PATH)


def test_page_html(page):
    assert page.html is not None and isinstance(page.html, str)


def test_page_links(page):
    assert isinstance(page.links, list)


def test_page_text(page):
    text = page.text()
    logger.debug(text)
