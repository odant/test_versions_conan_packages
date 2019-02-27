#!/usr/bin/env python


import unittest
import pathlib
import conans.tools


class Fake(unittest.TestCase):

    def setUp(self):
        print("setUp()")

    def test_1(self):
        pass

    def test_2(self):
        pass


if __name__ == "__main__":
    unittest.main()

