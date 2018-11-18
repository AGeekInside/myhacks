
#!/usr/bin/env python
'''No docstring has been added yet.'''

import click
import os

import myhacks as myh

@click.command()
@click.argument('parameter', required=False)
def run_roll(parameter):
    '''test docstring'''

    print('No code added to this hack yet.')


if __name__ == '__main__':
    run_roll()