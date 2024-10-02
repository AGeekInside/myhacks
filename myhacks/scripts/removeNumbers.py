
#!/usr/bin/env python
'''No docstring has been added yet.'''

import click
import os

import myhacks as myh

def rename_directories(root_dir):
    """
    Rename directories before processing files.
    
    :param root_dir: Root directory to start the search
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            if '-' in dirname:
                new_dirname = dirname.split('-')[1].strip() + ' - ' + dirname.split('-')[0].strip().split('.')[1].strip()
            else:
                if '.' in dirname:
                    new_dirname = dirname.split('.')[1].strip()
                else:
                    new_dirname = dirname
            print(f"Renamed {dirname} to {new_dirname}")
            os.rename(os.path.join(dirpath, dirname), os.path.join(dirpath, new_dirname))

@click.command()
@click.argument('root_dir', required=True)
def run_removeNumbers(root_dir):
    '''test docstring'''

    # Rename directories before processing files
    rename_directories(root_dir)


if __name__ == '__main__':
    run_removeNumbers()