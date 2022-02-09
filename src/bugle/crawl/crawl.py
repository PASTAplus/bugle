#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: crawl

:Synopsis:

:Author:
    servilla

:Created:
    2/9/22
"""
from bs4 import BeautifulSoup
import click
import daiquiri

from bugle.crawl.crawler import Crawler
from bugle.crawl.page import Page

logger = daiquiri.getLogger(__name__)


def indexer(**kwargs):
    page: Page = kwargs["page"]
    soup = BeautifulSoup(page.html, "lxml")
    main_tag = soup.main
    if main_tag is not None:
        index_text = " ".join([_.strip() for _ in main_tag.strings])
        print(f"{page.url}: {index_text}")


allow_help = "Filter HREFs using regular expression - default: '*' (allow all HREFs)"
follow_help = "Follow HREFs on page to next page(s)"
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("host", nargs=1, required=True)
@click.argument("paths", nargs=-1, required=True)
@click.option("-a", "--allow", default="*", help=allow_help)
@click.option("-f", "--follow", is_flag=True, default=False, help=follow_help)
def main(host: str, paths: tuple, allow: str, follow: bool):
    """
        Crawl a website

        \b
            HOST: Website host name (e.g., https://web.myweb.me).
            PATHS: One or more space separated page paths.
    """

    crawler = Crawler(host=host)

    for path in paths:
        crawler.crawl(path=path, allow=allow, follow=follow, callback=indexer)

    print(crawler.visited)

    return 0


if __name__ == '__main__':
    main()

