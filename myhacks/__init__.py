__version__ = "13.0.0"

from .hacks import find_repos
from .hacks import make_executable
from .hacks import HacksInfo

HACKS_INFO = HacksInfo()
MYHACKS_DIR = "/home/mbrooks/projs/myhacks/"
MYHACKSBIN_DIR = f"{MYHACKS_DIR}myhacks/scripts/"
PROJS_DIR = "/home/mbrooks/projs/"
OUTPUTS = ["fancy_grid", "grid", "psql", "presto", "simple"]


__all__ = ["find_repos", "HacksInfo", "make_executable"]
