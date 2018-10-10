__version__ = "14.0.0"

from .hacks import compile_repo_info
from .hacks import find_repos
from .hacks import make_executable
from .hacks import HacksInfo

HACKS_INFO = HacksInfo()
MYHACKS_DIR = "/home/mbrooks/projs/myhacks/"
MYHACKSBIN_DIR = f"{MYHACKS_DIR}myhacks/scripts/"
PROJS_DIR = "/home/mbrooks/projs/"
OUTPUTS = ["fancy_grid", "grid", "psql", "presto", "simple"]


__all__ = ["compile_repo_info", "find_repos", "HacksInfo", "make_executable"]
