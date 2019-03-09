import subprocess
from pathlib import Path
import re


def conanInit():
    print("\n")
    cmd = ["conan", "user"]
    print("Runing '%s' ..." % " ".join(cmd))
    out = subprocess.check_output(cmd, universal_newlines=True)
    print(out)
    cmd = ["conan", "profile", "new", "default", "--detect"]
    print("Runing '%s' ..." % " ".join(cmd))
    out = subprocess.check_output(cmd, universal_newlines=True)
    print(out)


def conanCreate(folder, name, version, user_channel):
    print("\n")
    recipeDir = str(Path(folder) / name / version)
    cmd = ["conan", "create", recipeDir, user_channel]
    print("Runing '%s' ..." % " ".join(cmd))
    out = subprocess.check_output(cmd, universal_newlines=True)
    print(out)
    lastString = out.split("\n")[-2]
    pattern = "^(%s/%s@%s:\sPackage)\s'([0-9a-f]+)'\screated" % (name, version, user_channel)
    res = re.match(pattern, lastString)
    packageHash = res.group(2)
    return packageHash


def conanSearch(request):
    print("\n")
    cmd = ["conan", "search", request]
    print("Runing '%s' ..." % " ".join(cmd))
    out = subprocess.check_output(cmd, universal_newlines=True)
    print(out)
