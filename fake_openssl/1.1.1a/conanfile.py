from conans import ConanFile


class FakeOpenSSLConan(ConanFile):
    name = "fake_openssl"
    version = "1.1.1a"
    license = "MIT"
    url = "https://github.com/odant/test_versions_conan_packages"
    discreption = "Select version Conan packages"
    build_policy = "missing"

