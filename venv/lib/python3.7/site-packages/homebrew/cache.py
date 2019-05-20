import json
import os
from functools import wraps

CACHE_DIR = os.path.join(
    os.path.expanduser("~/Library/Caches"), __loader__.name.split(".")[0]
)
INSTALLED_PATH = os.path.join(CACHE_DIR, "installed.json")
USES_PATH = os.path.join(CACHE_DIR, "uses.json")


def read(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        pass


def write(installed, path):
    with open(path, "w") as file:
        json.dump(installed, file)


def uses_cache(method):
    @wraps(method)
    def _wrapper(self):
        installed = read(INSTALLED_PATH)
        uses = read(USES_PATH)

        if installed and uses and sorted(self._installed) == sorted(installed):
            return uses

        uses = method(self)

        write(self._installed, INSTALLED_PATH)
        write(uses, USES_PATH)

        return uses

    return _wrapper
