#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import os

import myhacks as myh

@click.command()
def run_cpMITREPipfile():
    '''test docstring'''

    pipfile_loc = '/home/mbrooks/projs/utils/py_stuff/Pipfile.mitre'
    cwd = os.getcwd()
    cmd = f'cp {pipfile_loc} {cwd}'
 
    myh.run(cmd)

if __name__ == '__main__':
    run_cpMITREPipfile()
