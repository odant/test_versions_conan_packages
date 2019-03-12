from conans import ConanFile


class Project(ConanFile):

    def requirements(self):
        self.requires("fake_openssl/1.1.0g+13@odant/testing")
