#!/usr/bin/env python

from setuptools import setup, find_packages

name = "indicdictionary"

setup(
    name = name,
    version = "0.1.0",
    license = "LGPL-3.0",
    description = "A bilingual dictionary for indic languages",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description = """A bilingual dictionary supporting multiple indic languages and English""",
    packages = find_packages(),
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools', 'BeautifulSoup', 'render'],
    test_suite="tests",
    zip_safe = False,
    )


