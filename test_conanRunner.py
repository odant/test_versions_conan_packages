#!/usr/bin/env python


import unittest
from removeAll import removeAll
from pathlib import Path
from conans import tools

from conanRunner import conanRunner


currentDir = Path.cwd()
conanHome = currentDir / "FAKE_CONAN_HOME"


class Test_conanRunner(unittest.TestCase):

    def setUp(self):
        removeAll(conanHome)
        conanHome.mkdir()

    def test_1_conanRunner_normal(self):
        print("\n")
        with tools.environment_append({"CONAN_USER_HOME": str(conanHome)}):
            args = ["help"]
            result = conanRunner(args)
            self.assertFalse(not result)
            print("\nOutput 'conan help':")
            for s in result:
                print(s)

    def test_2_conanRunner_bad(self):
        print("\n")
        with tools.environment_append({"CONAN_USER_HOME": str(conanHome)}):
            args = ["bad_command"]
            self.assertRaises(Exception, conanRunner, args)


if __name__ == "__main__":
    unittest.main()
