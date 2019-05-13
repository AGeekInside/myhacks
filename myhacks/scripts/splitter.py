#!/usr/bin/env python
"""Utiltiy class to split csv files."""

import click
import csv
import os


class Splitter:
    """Class to split csv files."""

    def __init__(
        self,
        input_file=None,
        line_limit=10000,
        output_prefix="output",
        output_suffix="csv",
        delimiter=",",
        output_dir=".",
        keep_headers=True,
    ):
        self.delimiter = delimiter
        self.input_file = input_file
        self.line_limit = line_limit
        self.output_dir = output_dir
        self.keep_headers = keep_headers
        self.output_prefix = output_prefix
        self.output_suffix = output_suffix

    def split(self):
        """Splits the input file into pieces."""

        if self.input_file:
            with open(self.input_file) as input_csv:
                reader = csv.reader(input_csv, delimiter=self.delimiter)

                current_piece = 1

                output_path = f"{self.output_dir}/{self.output_prefix}_{current_piece}.{self.output_suffix}"
                current_out_path = os.path.join(output_path)
                current_out_writer = csv.writer(open(current_out_path, "w"))
                current_limit = self.line_limit
                if self.keep_headers:
                    headers = next(reader)
                    current_out_writer.writerow(headers)
                for i, row in enumerate(reader):
                    if i + 1 > current_limit:
                        current_piece += 1
                        current_limit = self.line_limit * current_piece
                        output_path = f"{self.output_dir}/{self.output_prefix}_{current_piece}.{self.output_suffix}"
                        current_out_path = os.path.join(output_path)
                        current_out_writer = csv.writer(open(current_out_path, "w"))
                        if self.keep_headers:
                            current_out_writer.writerow(headers)
                    current_out_writer.writerow(row)

    def __repr__(self):
        """Outputs information about the Splitter object."""

        output_string = f"{self.__class__}: input_file: {self.input_file} output_dir: '{self.output_dir}'"
        return output_string


@click.command()
@click.argument("input_file", required=True)
@click.option("--line_limit", default=10000)
@click.option("--headers/--no-headers", default=False)
def run_splitter(input_file, line_limit, headers):
    """Runs split on the specified input file.  Default of 10000 entries per new file."""

    print(
        f"Preparing to split {input_file} into files with {line_limit} lines per files."
    )
    splitter = Splitter(input_file, line_limit=line_limit, keep_headers=headers)

    print(f"Spliter is {splitter}")
    splitter.split()


if __name__ == "__main__":
    run_splitter()
