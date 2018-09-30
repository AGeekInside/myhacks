#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import os

import myhacks as myh


@click.command()
@click.argument("inputfile", required=False)
def run_gnvim(inputfile):
    """Runs nvim in a gnome-terminal"""

    cmd = f"nvim {inputfile}"
    myh.term_run(cmd)


if __name__ == "__main__":
    run_gnvim()
