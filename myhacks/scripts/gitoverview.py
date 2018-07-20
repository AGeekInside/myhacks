import click
import os
from tabulate import tabulate

import myhacks as myh


@click.command()
@click.argument('rootdir', required=False)
@click.option('--all/--changes', default=False)
@click.option('--fetch/--no-fetch', default=False)
@click.option('--outputformat',
              type=click.Choice(myh.OUTPUTS),
              default='simple')
def run_checkGit(rootdir, all, fetch, outputformat):
    '''Output the status of git repos in the projs directory.'''
    if not rootdir:
        rootdir = myh.PROJS_DIR 

    repos = myh.find_repos(rootdir)
    print(f'Found {len(repos)} repos in {rootdir}.')

    repo_info = myh.compile_repo_info(repos,
                                      all=all,
                                      fetch=fetch)

    print(tabulate(repo_info, headers="keys", tablefmt=outputformat))


if __name__ == '__main__':
    run_checkGit()
