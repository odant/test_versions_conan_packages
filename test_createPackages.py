#!/usr/bin/env python


import unittest
from removeAll import removeAll
from pathlib import Path
from conans import tools

from createPackages import conanInit, conanCreate, createFakeOpenSSL


currentDir = Path.cwd()
conanHome = currentDir / "FAKE_CONAN_HOME"


class Test_createPackages(unittest.TestCase):

    def setUp(self):
        removeAll(conanHome)
        conanHome.mkdir()

    def test_1_conanInit(self):
        with tools.environment_append({"CONAN_USER_HOME": str(conanHome)}):
            conanInit()
        self.assertTrue((conanHome / ".conan").is_dir())
        self.assertTrue((conanHome / ".conan" / "conan.conf").is_file())
        self.assertTrue((conanHome / ".conan" / "registry.json").is_file())

    def test_2_conanCreate(self):
        recipeDir = currentDir / "fake_openssl"
        with tools.environment_append({"CONAN_USER_HOME": str(conanHome)}):
            conanInit()
            packageHash = conanCreate(folder=currentDir, name="fake_openssl", version="1.1.0", user_channel="odant/testing")
            conaninfoPath = conanHome / ".conan" / "data" / "fake_openssl" / "1.1.0" / "odant" / "testing" / "package" / packageHash / "conaninfo.txt"
            self.assertTrue(conaninfoPath.is_file())

    def test_3_createFakeOpenSSL(self):
        recipeDir = currentDir / "fake_openssl"
        with tools.environment_append({"CONAN_USER_HOME": str(conanHome)}):
            conanInit()
            createFakeOpenSSL(folder=currentDir, user_channel="odant/testing")


if __name__ == "__main__":
    unittest.main()
