#!/usr/bin/env python


import unittest
from removeAll import removeAll
from pathlib import Path
from conans import tools

import createPackages


currentDir = Path.cwd()
conanHome = currentDir / "FAKE_CONAN_HOME"


class Test_conanInit(unittest.TestCase):

    def setUp(self):
        removeAll(conanHome)
        conanHome.mkdir()

    def test_conanInit(self):
        with tools.environment_append({"CONAN_USER_HOME": str(conanHome)}):
            createPackages.conanInit()
        self.assertTrue((conanHome / ".conan").is_dir())
        self.assertTrue((conanHome / ".conan" / "conan.conf").is_file())
        self.assertTrue((conanHome / ".conan" / "registry.json").is_file())


class Test_conanCreate(unittest.TestCase):
    def setUp(self):
        removeAll(conanHome)
        conanHome.mkdir()
        with tools.environment_append({"CONAN_USER_HOME": str(conanHome)}):
            createPackages.conanInit()

    def test_fake(self):
        pass


if __name__ == "__main__":
    unittest.main()
