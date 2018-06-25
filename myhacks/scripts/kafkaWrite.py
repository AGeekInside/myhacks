#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import os

import myhacks as myh

@click.command()
@click.argument('parameter', required=False)
def run_kafkaWrite(parameter):
    '''test docstring'''

    print('No code added to this hack yet.')


if __name__ == '__main__':
    run_kafkaWrite()