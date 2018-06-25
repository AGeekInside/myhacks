#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import os

import myhacks as myh

@click.command()
@click.argument('parameter', required=False)
def run_dockerUI(parameter):
    '''test docstring'''
    cmd = 'docker run -v /var/run/docker.sock:/run/docker.sock -ti -e TERM tomastomecek/sen'
    myh.run(cmd)

if __name__ == '__main__':
    run_dockerUI()
