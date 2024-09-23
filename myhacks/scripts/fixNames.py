
#!/usr/bin/env python
'''No docstring has been added yet.'''

import click
import os
import shutil

import myhacks as myh

def removeLeadingNumbers(pdf_files):
    proposed_names = []
    for file in pdf_files:
        name_parts = str.split(file, " ")
        end_part = name_parts[-1].split(".")[0]
        proposed_name = ' '.join(name_parts[1:len(name_parts)-1]) + " " + end_part + " " + name_parts[0] + ".pdf"
        proposed_names.append({
            "old": file,
            "new": proposed_name
        })
        shutil.copy(file, proposed_name)
    return proposed_names 

def generateNames(pdf_files):
    proposed_names = []
    for file in pdf_files:
        split = str.split(file, "-")
        if len(split) > 1:
            proposed_name = str.split(file, "-")[-1].strip()
            proposed_names.append({
                "old": file,
                "new": proposed_name
            })
            shutil.copy(file, proposed_name)
    return proposed_names


def fixSpidey(pdf_files):
    proposed_names = []
    for file in pdf_files:
        proposed_name = "Amazing Spider-Man " + str.split(file," ")[-1].split(".")[0] + ".pdf"
        proposed_names.append({
            "old": file,
            "new": proposed_name
        })
        shutil.copy(file, proposed_name)
    return proposed_names


def fixFRNames(pdf_files):
    proposed_names = []
    for file in pdf_files:
        if "-" in file:
            proposed_name = str.split(file, "-")[-1].split(".")[0].strip() + ".pdf"
            proposed_names.append({
                "old": file,
                "new": proposed_name
            })
            shutil.copy(file, proposed_name)
    return proposed_names


@click.command()
@click.argument('runmode', required=False)
def run_fixNames(runmode):
    '''hack tool to fixing names of files and directories for kavita'''

        # Get the list of files in the current directory
    files = os.listdir('.')
    pdf_files = [file for file in files if file.endswith('.pdf')]

    if runmode == 'leading_nums':
        print('Running in remove numbers mode')
        proposed_names = removeLeadingNumbers(pdf_files)
    elif runmode == "fixSpidey":
        print('Running in fix spidey mode')
        proposed_names = fixSpidey(pdf_files)
    elif runmode == "generate_names":
        print('Running in generate names mode')
        proposed_names = generateNames(pdf_files)
    elif runmode == "fixFR":
        print('Running in fix FR mode')
        proposed_names = fixFRNames(pdf_files)
    else:
        print('No mode specified')
        proposed_names = []
    
    # Print the list of PDF files
    print(proposed_names)


if __name__ == '__main__':
    run_fixNames()