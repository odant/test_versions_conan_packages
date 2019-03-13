#!/usr/bin/env python


import unittest
from removeAll import removeAll
from pathlib import Path
from conans import tools
from configparser import ConfigParser

from createPackages import conanInit, conanCreate, createFakeOpenSSL
from conanInstall import conanInstall


currentDir = Path.cwd()
conanHome = currentDir / "FAKE_CONAN_HOME"


class Test_conanInstall(unittest.TestCase):

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
            conaninfo.read(str(conaninfoPath))
            requires = [i for i in conaninfo["full_requires"]]
            print("Full requires: ", requires)
            self.assertEqual(requires[0], "fake_openssl/1.1.0g+13@odant/testing")

    def test_2_conanInstall_project_with_fake_jscript(self):
        with tools.environment_append({"CONAN_USER_HOME": str(conanHome)}):
            conanInit()
            createFakeOpenSSL(folder=currentDir, user_channel="odant/testing")
            conanCreate(folder=currentDir, name="fake_jscript", version="11.11.0.1", user_channel="odant/testing")
            project = "project_with_fake_jscript"
            installDir = currentDir / project;
            removeAll(installDir)
            installDir.mkdir();
            conanInstall(conanfile=(currentDir / (project + ".py")), installFolder=installDir)
            conaninfoPath = installDir / "conaninfo.txt"
            self.assertTrue(conaninfoPath.is_file())
            conaninfo = ConfigParser(allow_no_value=True)
            conaninfo.read(str(conaninfoPath))
            requires = [i for i in conaninfo["full_requires"]]
            requires.sort()
            print("Full requires: ", requires)
            normalRequires = ["fake_jscript/11.11.0.1@odant/testing", "fake_openssl/1.1.1b+5@odant/testing"]
            normalRequires.sort()
            self.assertEqual(requires, normalRequires)

    def test_3_conanInstall_with_override_channel(self):
        with tools.environment_append({"CONAN_USER_HOME": str(conanHome)}):
            conanInit()
            createFakeOpenSSL(folder=currentDir, user_channel="odant/testing")
            conanCreate(folder=currentDir, name="fake_openssl", version="1.1.1a", user_channel="odant/stable")
            conanCreate(folder=currentDir, name="fake_jscript", version="11.11.0.2", user_channel="odant/stable")
            project = "project_with_override_channel"
            installDir = currentDir / project;
            removeAll(installDir)
            installDir.mkdir();
            conanInstall(conanfile=(currentDir / (project + ".py")), installFolder=installDir)
            conaninfoPath = installDir / "conaninfo.txt"
            self.assertTrue(conaninfoPath.is_file())
            conaninfo = ConfigParser(allow_no_value=True)
            conaninfo.read(str(conaninfoPath))
            requires = [i for i in conaninfo["full_requires"]]
            requires.sort()
            print("Full requires: ", requires)
            normalRequires = ["fake_jscript/11.11.0.2@odant/stable", "fake_openssl/1.1.1b+5@odant/testing"]
            normalRequires.sort()
            self.assertEqual(requires, normalRequires)


if __name__ == "__main__":
    unittest.main()
