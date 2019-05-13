#!/usr/bin/env python
"""No docstring has been added yet."""

import click
import configparser
import os

import myhacks as myh


def setup(**kwargs):
    print(kwargs)


def parse_setup(text):
    """unmatched parenthesis, even inside string literals, will break this"""
    start = text.find("setup(")
    text = text[start:]  # cut off anything before
    stack = 0
    for idx, char in enumerate(text[6:], 7):
        if char == ")":
            if stack:
                stack -= 1
            else:
                break
        elif char == "(":
            stack += 1

    return text[:idx]  # cut off anything behind


@click.command()
@click.argument("parameter", required=False)
def run_checksetup(parameter):
    """test docstring"""

    pipfile_name = "Pipfile"

    print(f"Looking for Pipfile.")
    pipfile_config = configparser.ConfigParser()
    pipfile_config.read(pipfile_name)

    for package in pipfile_config["packages"]:
        print(f"Found {package} in Pipfile.")

    print("Attempting to reading setup from setup.py")

    setup_file = "setup.py"

    with open(setup_file) as f:
        print(f.read())


if __name__ == "__main__":
    run_checksetup()
