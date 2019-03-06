#!/usr/bin/env python


import unittest
from pathlib import Path
from conans import tools


currentDir = Path.cwd()
conanHome = currentDir / "FAKE_CONAN_HOME"

# Test for replace environment variable
class Test_tools_environment_append(unittest.TestCase):

    def test_1_current_environment(self):
        name = "CONAN_USER_HOME"
        value = tools.get_env(name)
        print("Current %s: %s" % (name, value))

    def test_2_replace_environment(self):
        name = "CONAN_USER_HOME"
        with tools.environment_append({name: str(conanHome)}):
            value = tools.get_env(name)
            print("Current %s: %s" % (name, value))
            self.assertEqual(conanHome, Path(value))


if __name__ == "__main__":
    unittest.main()
