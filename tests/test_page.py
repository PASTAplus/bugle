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

from bugle.config import Config
from bugle.crawl.page import Page


logger = daiquiri.getLogger(__name__)


@pytest.fixture
def page():
    return Page(Config.URL)


def test_page_html(page):
    assert page.html is not None and isinstance(page.html, str)


def test_page_links(page):
    assert isinstance(page.links, list)
