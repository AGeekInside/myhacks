import click
import jinja2
import os
import stat

import myhacks as myh


file_template = '''

import click
import os

import myhacks as myh

@click.command()
@click.argument('parameter', required=False)
def run_{{ execname }}(parameter):
    \'\'\'{{ docstring }}\'\'\'

    print('No code added to this hack yet.')


if __name__ == '__main__':
    run_{{ execname }}()
'''


hack_bin_dir = myh.MYHACKS_DIR

@click.command()
@click.argument('execname')
def gen_bin(execname):
    '''Creates a stub for hack executables.'''

    template = jinja2.Template(file_template)
    new_hack_bin = template.render(execname=execname,
                                   docstring = 'test docstring')

    #print(f'new_hack_bin: \n{new_hack_bin}')

    outfile = hack_bin_dir + execname

    with open(outfile, 'w') as f:
        f.write(new_hack_bin)

    myh.make_executable(outfile)

    entry_point = f'{execname}=myhacks.scripts.{execname}:run_{execname}'

    print(f'entry_point: {entry_point}')


if __name__ == '__main__':
    gen_bin()
