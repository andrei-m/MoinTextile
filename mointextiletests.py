#!/usr/bin/python
"""
    Tests for the mointextile plugin.

    @copyright: 2011 by Andrei Mackenzie
    @license: GNU GPL
"""

import unittest
import mointextile

class TextileTester(unittest.TestCase):
    """Tests for mointextile.Textiler"""
    def test_http(self):
        """Test the default 'http' class"""
        result = mointextile.Parser.get_processed('"Andrei Mackenzie":http://www.andreimackenzie.com')
        self.assertEqual('\t<p><a href="http://www.andreimackenzie.com" class="http">Andrei Mackenzie</a></p>', result)

    def test_existing_class(self):
        """Test that existing classes are not overwritten"""
        result = mointextile.Parser.get_processed('"(testA,testB)title":http://www.google.com')
        self.assertEqual('\t<p><a href="http://www.google.com" class="testA,testB">title</a></p>', result)

    def test_mailto(self):
        """Test mailto links"""
        result = mointextile.Parser.get_processed('"address":mailto:someone@somedomain.com')
        self.assertEqual('\t<p><a href="mailto:someone@somedomain.com" class="mailto">address</a></p>', result)



if __name__ == '__main__':
    unittest.main()

