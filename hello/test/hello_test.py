#!/usr/bin/python
"""This is a sample docstring for the Hello unit testing."""

import unittest
from hello import Hello


class TestHello(unittest.TestCase):
    """This is a sample docstring for the Hello testing class."""

    def test_hello(self):
        """Test the Hello.hello() method."""
        hello = Hello()
        self.assertEqual(hello.hello(), 'Hello!')

if __name__ == '__main__':
    unittest.main()
