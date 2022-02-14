#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: setup.py

:Synopsis:

:Author:
    servilla

:Created:
    6/15/18
"""
from os import path
from setuptools import find_packages, setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "LICENSE"), encoding="utf-8") as f:
    full_license = f.read()

with open(path.join(here, "src/bugle/VERSION.txt"), encoding="utf-8") as f:
    version = f.read()


setup(
    name="bugle",
    version=version,
    description="Bugle: a light-weight web site crawler adn search indexer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Environmental Data Initiative",
    url="https://github.com/PASTAplus/bugle",
    license=full_license,
    packages=find_packages(where="src", include=["bugle", "bugle.crawl", "bugle.index"]),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=" >= 3.9.*",
    install_requires=["click==8.0.3", "daiquiri==3.0.0",  "beautifulsoup4==4.10.0", "lxml==4.7.1", "requests==2.27.1", "snowballstemmer==2.2.0"],
    classifiers=["License :: OSI Approved :: Apache Software License",],
)


def main():
    return 0


if __name__ == "__main__":
    main()
