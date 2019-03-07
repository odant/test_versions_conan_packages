import subprocess
from pathlib import Path


def conanInit():
    print("\n")
    cmd = ["conan", "user"]
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


def conanSearch(request):
    print("\n")
    cmd = ["conan", "search", request]
    print("Runing '%s' ..." % " ".join(cmd))
    out = subprocess.check_output(cmd, universal_newlines=True)
    print(out)
