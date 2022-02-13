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

import click
import daiquiri

from bugle.crawl.crawler import Crawler

cwd = os.path.dirname(os.path.realpath(__file__))
logfile = cwd + "/crawl.log"
daiquiri.setup(level=logging.INFO,
               outputs=(daiquiri.output.File(logfile), "stdout",))
logger = daiquiri.getLogger(__name__)


allow_help = "Allow HREFs using regular expression - default: '*' (allow all HREFs)"
follow_help = "Follow HREFs on page to next page(s)"
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("url", nargs=1, required=True)
@click.argument("content", nargs=1, required=True)
@click.argument("selectors", nargs=-1, required=True)
@click.option("-a", "--allow", default="*", help=allow_help)
@click.option("-f", "--follow", is_flag=True, default=False, help=follow_help)
def main(url: str, content: str, selectors: tuple, allow: str, follow: bool):
    """
        Crawl a website

        \b
            URL: URL of website to crawl and index
            CONTENT: File location of content
            SELECTORS: One or more space separated tags to define index content.
    """
    crawler = Crawler(url=url)
    crawler.crawl(selectors=selectors, allow=allow, follow=follow)
    logger.info(crawler.visited)

    j = json.dumps(crawler.index_content, indent=2)
    with open(content, "w") as f:
        f.write(j)

    return 0


if __name__ == '__main__':
    main()

