import click
import os
from tabulate import tabulate

import myhacks as myh

projs_dir = '/home/mbrooks/projs'

@click.command()
@click.argument('rootdir', required=False)
@click.option('--all/--changes', default=False)
def run_checkGit(rootdir, all):
    '''Output the status of git repos in the projs directory.'''
    if not rootdir:
        rootdir = projs_dir

    repos = myh.find_repos(rootdir)
    print(f'Found {len(repos)} repos in {rootdir}.')

    repo_info = myh.compile_repo_info(repos, all=all)
    print(tabulate(repo_info, headers="keys"))


if __name__ == '__main__':
    run_checkGit()
