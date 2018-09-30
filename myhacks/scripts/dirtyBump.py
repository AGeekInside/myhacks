#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import os

import myhacks as myh


@click.command()
@click.argument("reltype", required=True)
@click.argument("dryrun", required=True)
def run_dirtyBump(reltype, dryrun):
    """Does a dirty bumpversion run."""

    if myh.isTrue(dryrun):
        dryrun_str = "--dry-run"
    else:
        dryrun_str = ""

    cmd = f"bumpversion --allow-dirty --verbose {dryrun_str} {reltype}"
    out = myh.run(cmd)

    print(out.stdout.decode("utf-8"))


if __name__ == "__main__":
    run_dirtyBump()
