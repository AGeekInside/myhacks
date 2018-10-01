#!/usr/bin/env python
"""Hack to list the hacks in the system and their status."""

import click
import os

import myhacks as myh


@click.command()
def run_lshacks():
    """Runs the lshacks hack to show the hacks installed."""

    hacks_info = myh.HacksInfo()
    hacks_dir = myh.__file__
    print(f"Hacks in found in {hacks_dir}.")


if __name__ == "__main__":
    run_lshacks()
