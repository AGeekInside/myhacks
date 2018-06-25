#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import os

import myhacks as myh

@click.command()
@click.argument('parameter', required=False)
def run_newDevSession(parameter):
    '''Opens three terminals with the standard dev setup in i3.'''

    workspaces
 
    numbered_workspaces = filter(lambda w: w.name[0].isdigit(), workspaces)
    numbers = list(map(lambda w: int(re.search(r'^([0-9]+)', w.name).group(0)), numbered_workspaces))

    new = 0

    for i in range(1, max(numbers) + 2):
        if i not in numbers:
            new = i
            break

    print(f'new: {new}')

    print('No code added to this hack yet.')


if __name__ == '__main__':
    run_newDevSession()
