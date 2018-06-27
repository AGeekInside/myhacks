import click
import os
import sys

import myhacks as myh

def check_version_info(cfg_file):
    '''Checks for bumpversion version info.

       If found, prints it out and exits.

       Returns: None, if nothing found.  '''

    with open(cfg_file, 'r') as f:
        for i, line in enumerate(f.readlines()):
            version_line_start = 'current_version'
            if line.startswith(version_line_start):
                version = line.split('=')[1].strip()
                return version
    return None

def check_cfg_files(cfg_files = ['.bumpversion.cfg', 'setup.cfg']):
    '''Checks the given config files for bumpversion version.'''

    for wrk_file in cfg_files:
        if os.path.isfile(wrk_file):
            version = check_version_info(wrk_file)
            if version:
                return version

    return version



@click.command()
@click.argument('parameter', required=False)
def run_currVersion(parameter):
    '''Prints out the current version from the .bumpversion.cfg
       in the current directory.'''

    cfg_files = ['.bumpversion.cfg', 'setup.cfg']
    version = check_cfg_files(cfg_files)
    if version:
        print(f'Current version: {version}')
        sys.exit(0)

    print(f'No bumpversion config found.')


if __name__ == '__main__':
    run_currVersion()
