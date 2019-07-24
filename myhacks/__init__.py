__version__ = "20.0.0"

from .hacks import compile_repo_info
from .hacks import find_repos
from .hacks import get_hostname_ip
from .hacks import make_executable
from .hacks import HacksInfo
from .hacks import list_files

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
    "list_files",
    "make_executable",
    "file_template",
    "tabspace",
]

tabspace = '    '

file_template = """
#!/usr/bin/env python
'''{{top_docstring}}'''

import click
import os

@click.command()
@click.argument('parameter', required=False)
def run_{{ execname }}(parameter):
    \'\'\'{{ docstring }}\'\'\'

{{code_body}} 

if __name__ == '__main__':
    run_{{ execname }}()
"""