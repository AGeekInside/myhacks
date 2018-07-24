import click
import importlib
import os

import myhacks as myh


@click.command()
@click.argument('module', required=True)
@click.option('--internal/--no-internal', default=False)
def run_pymodinfo(module, internal):
    '''Outputs information found about the specified module.'''

    try:
        work_module = importlib.import_module(module, package=None)
        mod_info = sorted(dir(work_module))

        for entry in mod_info:
            if internal:
                print(f'{entry}')
            elif not entry.startswith('__'):
                print(f'{entry}')
    except Exception:
        print(f'Error importing {module}')


if __name__ == '__main__':
    run_pymodinfo()
