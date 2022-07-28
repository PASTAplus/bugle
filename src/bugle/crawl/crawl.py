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
import json
import logging
import os
import pickle
from xml.sax.saxutils import escape

import click
import daiquiri

from bugle.crawl.crawler import Crawler
from bugle.index import load
from bugle.index.index import Index

cwd = os.path.dirname(os.path.realpath(__file__))
logfile = cwd + "/crawl.log"
daiquiri.setup(level=logging.INFO,
               outputs=(daiquiri.output.File(logfile), "stdout",))
logger = daiquiri.getLogger(__name__)


def generate_sitemap(visited: set, cache: str):
    opentag = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
    )

    closetag = "</urlset>\n"

    sitemap = ""

    for url in visited:
        escaped_url = escape(url, {"'": "&apos;", "\"": "&quot;"})
        sitemap += f"  <url>\n    <loc>{escaped_url}</loc>\n  </url>\n"

    sitemap = opentag + sitemap + closetag

    with open(f"{cache}/sitemap.xml", "w") as f:
        f.write(sitemap)


allow_help = "Allow HREFs using regular expression - default: '*' (allow all HREFs)"
follow_help = "Follow HREFs on page to next page(s)"
sitemap_help = "Generate sitemap.org metadata and store in cache"
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("url", nargs=1, required=True)
@click.argument("cache", nargs=1, required=True)
@click.argument("selectors", nargs=-1, required=True)
@click.option("-a", "--allow", default="*", help=allow_help)
@click.option("-f", "--follow", is_flag=True, default=False, help=follow_help)
@click.option("-s", "--sitemap", is_flag=True, default=False, help=sitemap_help)
def main(url: str, cache: str, selectors: tuple, allow: str, follow: bool, sitemap: bool):
    """
        Crawl a website

        \b
            URL: URL of website to crawl and index
            CACHE: Cache location to write crawled content and index
            SELECTORS: One or more space separated tags to define index content.
    """
    crawler = Crawler(url=url)
    crawler.crawl(selectors=set(selectors), allow=allow, follow=follow)
    logger.info(crawler.visited)

    if sitemap:
        generate_sitemap(crawler.visited, cache)

    j = json.dumps(crawler.content, indent=2)
    with open(f"{cache}/content.json", "w") as f:
        f.write(j)

    index: Index = load.build_index(crawler.content)
    with open(f"{cache}/index.pkl", "wb") as f:
        pickle.dump(index, f)

    return 0


if __name__ == '__main__':
    main()

