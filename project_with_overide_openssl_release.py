from conans import ConanFile


class Project(ConanFile):

    def requirements(self):
        self.requires("fake_openssl/1.1.1b+5@odant/stable")
        self.requires("fake_jscript/9.11.0.1@odant/testing")
