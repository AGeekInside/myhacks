import click
import os
import sys

import myhacks as myh

@click.command()
@click.argument('parameter', required=False)
def run_currVersion(parameter):
    '''Prints out the current version from the .bumpversion.cfg
       in the current directory.'''

    cfg_files = ['.bumpversion.cfg', 'setup.cfg']
    cfg_file = None
    for wrk_file in cfg_files:
        if os.path.isfile(wrk_file):
            cfg_file = wrk_file

    if not cfg_file:
        print(f'No bumpversion config found.')
    else:
        try:
            with open(cfg_file, 'r') as f:
                for i, line in enumerate(f.readlines()):
                    version_line_start = 'current_version'
                    if line.startswith(version_line_start):
                        version = line.split('=')[1].strip()
                        print(f'Current version: {version}')
                        sys.exit(0)
            print('No version information found.')
        except FileNotFoundError as ex:
            print(f'No bumpversion config file "{cfg_file}" found.')


if __name__ == '__main__':
    run_currVersion()
