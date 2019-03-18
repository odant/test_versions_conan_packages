from pathlib import Path
from conanRunner import conanRunner


def conanInstall(conanfile, installFolder):
    print("\n")
    conanfile = str(conanfile)
    installFolder = str(installFolder)
    args = ["install", conanfile, "--install-folder", installFolder]
    for s in conanRunner(args):
        print(s)
