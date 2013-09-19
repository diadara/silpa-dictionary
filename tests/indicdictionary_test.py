#! /usr/bin/python
# -*- encoding:utf-8 -*-

import unittest
from indicdictionary import getInstance


class TestIndicDictionary(unittest.TestCase):

    def setUp(self):
        self.d = getInstance()

    def test_en_ml(self):
        meaning = self.d.getdef("cat", "en-ml")
        self.assertIn(u"പൂച്ച",meaning)

    def test_en_hi(self):
        meaning = self.d.getdef("cat","en-hi")
        self.assertIn(u"बिल्ली",meaning)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIndicDictionary)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
