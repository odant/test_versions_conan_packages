#!/usr/bin/env python


import unittest
from removeAll import removeAll
from pathlib import Path
from conans import tools
import subprocess


currentDir = Path.cwd()
conanHome = currentDir / "FAKE_CONAN_HOME"


class Test_createFakePackages(unittest.TestCase):

    def setUp(self):
        removeAll(conanHome)
        conanHome.mkdir()

    def test_1_conan_user(self):
        print("\n")
        with tools.environment_append({"CONAN_USER_HOME": str(conanHome)}):
            print("Runing 'conan user'")
            out = subprocess.check_output(["conan", "user"], universal_newlines=True)
            print(out)
            p = currentDir / "fakeOpenSSLRecipes" / "1.1.0"
            out = subprocess.check_output(["conan", "create", str(p), "odant/testing"], universal_newlines=True)
            print(out)


if __name__ == "__main__":
    unittest.main()
