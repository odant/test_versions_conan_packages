from pathlib import Path
from conans import tools


def removeAll(p):
    path = Path(p)
    if path.is_file():
        path.unlink()
    else:
        tools.rmdir(path)
