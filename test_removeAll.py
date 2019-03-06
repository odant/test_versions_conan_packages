#!/usr/bin/env python


import unittest
from removeAll import removeAll
from pathlib import Path


currentDir = Path.cwd()
conanHome = currentDir / "FAKE_CONAN_HOME"


class Test_removeAll(unittest.TestCase):

    def test_1_remove_nonexists(self):
        removeAll(conanHome)
        self.assertFalse(conanHome.exists())

    def test_2_remove_empty_directory(self):
        conanHome.mkdir()
        self.assertTrue(conanHome.is_dir())
        removeAll(conanHome)
        self.assertFalse(conanHome.exists())

    def test_3_remove_file(self):
        conanHome.touch()
        self.assertTrue(conanHome.is_file())
        removeAll(conanHome)
        self.assertFalse(conanHome.exists())

    def test_4_remove_tree(self):
        conanHome.mkdir()
        file = conanHome / "file.txt"
        file.touch()
        self.assertTrue(file.is_file())
        dir = conanHome / "dir"
        dir.mkdir()
        self.assertTrue(dir.is_dir())
        nestedFile = dir / "nestedFile.txt"
        nestedFile.touch()
        self.assertTrue(nestedFile.is_file())
        removeAll(conanHome)
        self.assertFalse(conanHome.exists())


if __name__ == "__main__":
    unittest.main()
