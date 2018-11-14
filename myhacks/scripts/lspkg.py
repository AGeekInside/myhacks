#!/usr/bin/env python
import configparser

import click

from tabulate import tabulate

import myhacks as myh


@click.command()
@click.option("--outputformat", type=click.Choice(myh.OUTPUTS), default="simple")
def run_lspkg(outputformat):
    """Utility to list packages installed in a given pipfile."""

    pipfile = "Pipfile"

    config = configparser.ConfigParser()
    config.read(pipfile)

    package_info = []
    for package in config["packages"]:
        package_info.append((package, config.get("packages", package), "Std"))

    for package in config["dev-packages"]:
        package_info.append((package, config.get("dev-packages", package), "Dev"))

    print(
        tabulate(
            package_info,
            headers=["Package", "Info", "Install Type"],
            tablefmt=outputformat,
        )
    )


if __name__ == "__main__":
    run_lspkg()
