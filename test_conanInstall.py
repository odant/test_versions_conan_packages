#!/usr/bin/env python


import unittest
from removeAll import removeAll
from pathlib import Path
from conans import tools
from configparser import ConfigParser

from createPackages import conanInit, createFakeOpenSSL
from conanInstall import conanInstall


currentDir = Path.cwd()
conanHome = currentDir / "FAKE_CONAN_HOME"


class Test_createPackages(unittest.TestCase):

    def setUp(self):
        removeAll(conanHome)
        conanHome.mkdir()

    def test_1_conanInstall_project_with_explicit_fake_openssl(self):
        with tools.environment_append({"CONAN_USER_HOME": str(conanHome)}):
            conanInit()
            createFakeOpenSSL(folder=currentDir, user_channel="odant/testing")
            project = "project_with_explicit_fake_openssl"
            installDir = currentDir / project;
            removeAll(installDir)
            installDir.mkdir();
            conanInstall(conanfile=(currentDir / (project + ".py")), installFolder=installDir)
            conaninfoPath = installDir / "conaninfo.txt"
            self.assertTrue(conaninfoPath.is_file())
            conaninfo = ConfigParser(allow_no_value=True)
            conaninfo.read(conaninfoPath)
            requires = [i for i in conaninfo["full_requires"]]
            print("Full requires: ", requires)
            self.assertEqual(requires[0], "fake_openssl/1.1.0g+13@odant/testing")


if __name__ == "__main__":
    unittest.main()
