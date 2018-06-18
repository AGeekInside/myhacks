#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import i3ipc 
import os
import re

import myhacks as myh

@click.command()
def run_listWorkspaces():
    '''Lists the current workspaces in i3'''

    i3 = i3ipc.Connection()

    workspaces = i3.get_workspaces()
    for ws in workspaces:
        print(f'{ws["name"]}')


if __name__ == '__main__':
    run_listWorkspaces()
