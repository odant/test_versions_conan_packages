from conans import ConanFile


class FakeJScriptConan(ConanFile):
    name = "fake_jscript"
    version = "11.11.0.1"
    license = "MIT"
    url = "https://github.com/odant/test_versions_conan_packages"
    discreption = "Select version Conan packages"
    build_policy = "missing"
    requires = "fake_openssl/[>=1.1.1a]@odant/testing"
