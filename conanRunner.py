from subprocess import PIPE, Popen, STDOUT
from conans.util.files import decode_text


def conanRunner(args = []):
    cmd = ["conan"]
    cmd.extend(args)
    print("Runing: ", " ".join(cmd))
    proc = Popen(cmd, stdout=PIPE, stderr=STDOUT)
    result = []
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        decoded_line = decode_text(line)
        striped_line = decoded_line.rstrip("\r\n")
        result.append(striped_line)
    proc.wait()
    if proc.returncode != 0:
        raise Exception("Failed run " + " ".join(cmd))
    return result
