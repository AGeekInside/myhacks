#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import os

import myhacks as myh


@click.command()
@click.argument("parameter", required=False)
def run_dosb(parameter):
    """test docstring"""

    cmd = f"ssh root@138.197.0.223"

    myh.run(cmd)


if __name__ == "__main__":
    run_dosb()
