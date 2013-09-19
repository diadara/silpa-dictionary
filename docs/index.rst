.. indicdictionary documentation master file, created by
   sphinx-quickstart on Tue Sep 17 02:43:31 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

indicdictionary
===============

A bilingual dictionary for indic languages.

Usage
-----

 >>> from indicdictionary import getInstance
 >>> d = getInstance()
 >>> print d.getdef("cat","en-ml").encode('utf-8')
 'cat\n   \t1. \xe0\xb4\xaa\xe0\xb5\x82\xe0\xb4\x9a\xe0\xb5\x8d\xe0\xb4\x9a\n   \t2. \xe0\xb4\xae\xe0\xb4\xbe\xe0\xb4\xb0\xe0\xb5\x8d\xe2\x80\x8d\xe0\xb4\x9c\xe0\xb5\x8d\xe0\xb4\x9c\xe0\xb4\xbe\xe0\xb4\xb0\xe0\xb4\xa8\xe0\xb5\x8d\xe2\x80\x8d\n'

Dependancies
------------
Indicdictionary requires render module for creating images.This requires you
to have pango, cairo,and pangocairo installed in your system.

API reference
--------------

.. automodule:: indicdictionary.core
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
