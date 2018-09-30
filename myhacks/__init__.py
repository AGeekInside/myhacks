__version__ = "12.0.0"

from .hacks import make_executable
from .hacks import HacksInfo

MYHACKS_DIR = "/home/mbrooks/projs/myhacks/"
MYHACKSBIN_DIR = f"{MYHACKS_DIR}myhacks/scripts/"
PROJS_DIR = "/home/mbrooks/projs/"
OUTPUTS = ["fancy_grid", "grid", "psql", "presto", "simple"]

__all__ = ["HacksInfo", "make_executable"]
