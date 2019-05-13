#!/usr/bin/env python
"""No docstring has been added yet."""

import click
import os

import myhacks as myh


@click.command()
@click.argument("recursive", required=False)
@click.argument("directory", required=False)
def run_finddups(recursive, directory):
    """Finds duplicate files in the directory."""

    print("No code added to this hack yet.")


if __name__ == "__main__":
    run_finddups()
