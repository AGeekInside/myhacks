#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import os

import myhacks as myh


@click.command()
@click.argument("filter", required=False)
def run_dimgFilter(filter):
    """Filters the list of images."""

    cmd = f"docker images | grep {filter}"

    result = myh.run(cmd)
    print(result.stdout.decode("utf-8"))


if __name__ == "__main__":
    run_dimgFilter()
