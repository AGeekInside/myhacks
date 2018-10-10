__version__ = "15.0.0"

from .hacks import compile_repo_info
from .hacks import find_repos
from .hacks import get_hostname_ip
from .hacks import make_executable
from .hacks import HacksInfo

HACKS_INFO = HacksInfo()
MYHACKS_DIR = "/home/mbrooks/projs/myhacks/"
MYHACKSBIN_DIR = f"{MYHACKS_DIR}myhacks/scripts/"
PROJS_DIR = "/home/mbrooks/projs/"
OUTPUTS = ["fancy_grid", "grid", "psql", "presto", "simple"]


__all__ = [
    "compile_repo_info",
    "find_repos",
    "get_hostname_ip",
    "HacksInfo",
    "make_executable",
]
