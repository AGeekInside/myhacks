#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import os
import pytest

import myhacks as myh

@click.command()
@click.argument('parameter', required=False)
def run_timeTests(parameter):
    '''Runs all found tests and times them.'''
    cwd = os.getcwd()
    print(f'cwd: {cwd}')

    pytest_cmd = "python -m cProfile -o profile $(pytest)"
    myh.run(pytest_cmd)

if __name__ == '__main__':
    run_timeTests()
