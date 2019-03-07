from conans import ConanFile


class FakeOpenSSLConan(ConanFile):
    name = "fake_openssl"
    version = "1.1.0"
    build_policy = "missing"
