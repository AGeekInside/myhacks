
#!/usr/bin/env python
'''Script to create donothing scripts'''

import os
import sys

import click
import jinja2

from prompt_toolkit import prompt

import myhacks as myh

def get_name():
    """Prompts for the name of the do-nothing script to create."""

    print("Creating a do-nothing script.")
    name = prompt("Do-Nothing name: ")
    return name


def get_filename(name=None):
    """Prompts for the filename to use for the do-nothin"""

    if name:
        default = name+'.py'
    else:
        default = ''

    filename = prompt("Enter the script filename: ", default=default)

    return filename

def get_steps():
    """Gets the steps for the process."""

    steps = []

    prev_step = None
    step_count = 0
    done = False
    while not done:
        if prev_step:
            print(f"Step {step_count}. {prev_step}")
        step_count += 1
        current_step = prompt("Enter next step:-> ")
        if current_step.strip() == '':
            break
        else:
            steps.append(current_step)
            prev_step = current_step
            current_step = None
    return steps

def write_script(script):
    """Outputs the do-nothing script."""

    if len(script['steps']) < 1:
        print("No steps found. Exiting.")
        sys.exit()

    print(f"Generating script for {script['name']}.")
    print(f"Outputting to {script['filename']}.")
    print("Script steps:")
    script['code_body'] = ''
    script['execname'] = script['name']

    for i, step in enumerate(script['steps']):
        print(f"{i+1}. {step}")
        script['code_body'] += f"{myh.tabspace}print(f' {i+1}. {step}')\n"

    # TODO add in render with parts from script dict
    template = jinja2.Template(myh.file_template)
    donothing_script = template.render(**script)
    print(donothing_script)

    with open(script["filename"], 'w') as f:
        f.write(donothing_script)

@click.command()
@click.argument('parameter', required=False)
def run_makedonothing(parameter):
    '''Creates a do-nothing script.'''

    script = {}

    script["name"] = get_name()

    script["filename"] = get_filename(script['name'])

    script["steps"] = get_steps()

    write_script(script)


if __name__ == '__main__':
    run_makedonothing()