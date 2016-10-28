#!/usr/bin/python

import unittest
from hello import Hello

class HelloTest(unittest.TestCase):
    def test_hello(self):
        hello = Hello()
        self.assertEqual(hello.hello(), 'Hello!')

if __name__ == '__main__':
    unittest.main()
