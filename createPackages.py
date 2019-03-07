import subprocess


def conanInit():
    print("\n")
    print("Runing 'conan user'...")
    out = subprocess.check_output(["conan", "user"], universal_newlines=True)
    print(out)

