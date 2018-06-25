import click
import os

import myhacks as myh

@click.command()
@click.argument('parameter', required=False)
def run_branchHistory(parameter):
    '''test docstring'''
    cmd = "for branch in `git branch -r | " + \
          "grep -v HEAD`;do echo -e `git show --format=\"%ci %cr \" $branch | " + \
          "head -n 1` \\t$branch; done | sort -r"

    results = myh.run(cmd, False)

    print(results.stdout.decode('utf-8'))


if __name__ == '__main__':
    run_branchHistory()
