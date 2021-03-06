#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Dictionary
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email: santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in


import os
from dictdlib import DictDB
from wiktionary import get_def
import render

# Have the render instance initiated only once
renderer = render.getInstance()

# One image for No image found
no_meaning_found = renderer.render_text("No meanings found",
                                        file_type="png",
                                        color="Red",
                                        font_size=10)


class Dictionary:
    """
    The dictionary class. Instantiate to get access to the methods.
    """
    def __init__(self):
        self.imageyn = None
        self.text = None
        self.dictionaryname = None
        self.fontsize = 16
        self.imagewidth = 300
        self.imageheight = 300

    def get_free_dict(self, src, dest):
        dict_dir = os.path.join(os.path.dirname(__file__), 'dictionaries')
        dictdata = dict_dir+ "/freedict-"+src+"-"+dest
        if os.path.isfile(dictdata+".index"):
            return dictdata
        return None

    def getdef(self, word, dictionary):
        """
        :param word: The word which has to be looked up.
        :param dictionary: The convertion needed, format src-dest
         >>>
        """
        src = dictionary.split("-")[0]
        dest = dictionary.split("-")[1]
        dictdata = self.get_free_dict(src, dest)
        if dictdata:
            meaningstring = ""
            dict = DictDB(dictdata)
            clean_word = word.lower()
            clean_word = clean_word.strip()
            meanings = dict.getdef(clean_word)
            for meaning in meanings:
                meaningstring += meaning
        if meaningstring == "None":
            meaningstring = "No definition found"
            return meaningstring
        return meaningstring.decode("utf-8")

    def getdef_image(self, word, dictionary, file_type='png',
                     width=0,  height=0, color="Black", fontsize=10):
        """
        Returns an image of the definition. Useful  for machine independant
        results.
        """
        meaning = self.getdef(word, dictionary)

        if meaning == "No definition found":
            return no_meaning_found
        else:
            return renderer.render_text(meaning, file_type=file_type,
                                        width=width, height=height,
                                        color=color, font_size=fontsize)

    def get_wiktionary_def_image(self, word, dictionary,
                                 file_type='png', width=0, height=0,
                                 color="Black", fontsize=10):
        """
        Returns an image of the definition. Useful  for machine independant
        results
        """
        tmp = dictionary.split("-")
        src_lang = tmp[0]
        dest_lang = tmp[1]

        meaning = get_def(word, src_lang, dest_lang)

        if meaning is None:
            return no_meaning_found
        else:
            return renderer.render_text(meaning, file_type=file_type,
                                        width=width, height=height,
                                        color=color, font_size=fontsize)

    def get_module_name(self):
        """
        Returns the modules name.
        """
        return "Dictionary"

    def get_info(self):
        """
        Returns more info on the module
        """
        return "Bilingual Dictionaries"


def getInstance():
    """
    :returns: an instance of the :class:`Dictionary`
    """
    return Dictionary()
