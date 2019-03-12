import subprocess
from pathlib import Path


def conanInstall(conanfile, installFolder):
    print("\n")
    conanfile = str(conanfile)
    installFolder = str(installFolder)
    cmd = ["conan", "install", conanfile, "--install-folder", installFolder]
    print("Runing '%s' ..." % " ".join(cmd))
    out = subprocess.check_output(cmd, universal_newlines=True)
    print(out)
