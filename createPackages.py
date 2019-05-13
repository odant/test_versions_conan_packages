from pathlib import Path
from conanRunner import conanRunner
import re


def conanInit():
    print("\n")
    for s in conanRunner(["user"]):
        print(s)
    for s in conanRunner(["profile", "new", "default", "--detect"]):
        print(s)


def conanCreate(folder, name, version, user_channel):
    print("\n")
    recipeDir = str(Path(folder) / name / version)
    args = ["create", recipeDir, user_channel]
    res = conanRunner(args)
    for s in res:
        print(s)
    hashString = res[-2]
    version = version.replace("+", "\+")
    pattern = "^(%s/%s@%s:\sPackage)\s'([0-9a-f]+)'\screated" % (name, version, user_channel)
    res = re.match(pattern, hashString)
    packageHash = res.group(2)
    return packageHash


def conanSearch(request):
    print("\n")
    for s in conanRunner(["user"]):
        print(s)


def createFakeOpenSSL(folder, user_channel):
    path = Path(folder) / "fake_openssl"
    for p in path.iterdir():
        version = str(p.name)
        conanCreate(folder, "fake_openssl", version, user_channel)
