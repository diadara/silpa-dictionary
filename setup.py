#!/usr/bin/env python

from setuptools import setup, find_packages

name = "dictionary"

setup(
    name = name,
    version = "0.2.1",
    url = "http://silpa.org.in/dictionary",
    license = "LGPL-3.0",
    description = "A bilingual dictionary for indic languages",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description = """A bilingual dictionary supporting multiple indic languages and english""",
    packages = find_packages(),
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools', 'BeautifulSoup''render'],
    zip_safe = False,
    )


