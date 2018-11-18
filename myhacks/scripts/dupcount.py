#!/usr/bin/env python
"""Utility to count duplicate files found in a given directory."""

import click
import operator
import os
from tabulate import tabulate

import myhacks as myh


def count_occurences(files_info, dup_method):
    """Counts the occurences of files, using the dup_method specified."""

    if dup_method in ["name"]:
        dup_method = lambda x,y: x
    elif dup_method in ["size"]:
        dup_method = lambda x,y: os.stat(y)
    else:
        print(f"Duplication method {dup_method} not defined.  Defaulting to filename.")
        dup_method = lambda x: x

    previous_files = {}

    file_count = 0

    for dirpath, dirname, filenames in files_info:
        for name in filenames:
            file_count += 1
            dup_name = dup_method(name, dirpath)
            if dup_name in previous_files:
                previous_files[dup_name] += 1
            else:
                previous_files[dup_name] = 1

    print(f"Found {file_count} file(s).")
    return previous_files


@click.command()
@click.option("--report-file", type=click.File("w"))
@click.option(
    "--dup-method", default="name", type=click.Choice(["name", "size", "size-name"])
)
@click.argument("directory", type=click.Path(exists=True), default=".", required=False)
def run_dupcount(directory, dup_method, report_file):
    """Recursively counts the duplicates found in a directory."""

    print(f"Counting duplicates in '{directory}'.")

    files_info = myh.list_files(directory)

    occurence_counts = count_occurences(files_info, dup_method)

    dup_filenames = [
        (name, occurence_counts[name])
        for name in occurence_counts
        if occurence_counts[name] > 1
    ]

    dup_filenames.sort(key=lambda tup: (tup[1], tup[0]))

    print(f"Found {len(dup_filenames)} duplicate(s).")

    if len(dup_filenames) < 21:
        print(tabulate(dup_filenames, headers=["Filename", "Count"]))


if __name__ == "__main__":
    run_dupcount()
