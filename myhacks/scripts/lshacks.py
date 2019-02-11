#!/usr/bin/env python
"""Hack to list the hacks in the system and their status."""

import click


@click.command()
def run_lshacks():
    """Runs the lshacks hack to show the hacks installed."""

    from pkg_resources import iter_entry_points

    for entry_point in iter_entry_points(group='console_scripts', name=None):
        if 'myhacks' in entry_point.module_name:
            print(f"{entry_point.name}")


if __name__ == "__main__":
    run_lshacks()
