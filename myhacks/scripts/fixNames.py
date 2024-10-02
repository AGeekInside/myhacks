
#!/usr/bin/env python
'''No docstring has been added yet.'''

import click
import os
import shutil

import myhacks as myh

def is_all_digits(s):
    """
    Check if every character of the string is a digit.
    
    :param s: Input string
    :return: True if every character is a digit, False otherwise
    """
    return s.isdigit()


def has_spaces(s):
    """
    Check if the string has spaces.
    
    :param s: Input string
    :return: True if the string has spaces, False otherwise
    """
    return ' ' in s


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
    print(len(pdf_files), "PDF files found.")
    proposed_names = []
    for file in pdf_files:
        print(f"Old name: {file}")
        split = str.split(file, "_")
        if len(split) > 1:
            proposed_name = str.split(file, "_")[-1].strip()
            print(f"Old name: {file}")
            print(f"New name: {proposed_name}")
            proposed_names.append({
                "old": file,
                "new": proposed_name
            })
            shutil.move(file, proposed_name)
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


def rmText(pdf_files):
    proposed_names = []
    for file in pdf_files:
        proposed_name = str.split(file, ".")[0] + ".pdf"
        proposed_names.append({
            "old": file,
            "new": proposed_name
        })
        shutil.copy(file, proposed_name)
    return proposed_names


def ddProcess(pdf_files):
    print("Processing Daredevil files.")

    for file in pdf_files:
        name_parts = str.split(file, " ")

        # If the first part is a number, remove it
        if is_all_digits(name_parts[0]):
            name_parts = name_parts[1:] 
            proposed_name = ' '.join(name_parts)
            print(f"Old name: {file}")
            print(f"New name: {proposed_name}")
            shutil.move(file, proposed_name)


def dragonProcess(pdf_files):
    print("Processing Dragon Magazine files.")

    for file in pdf_files:
        proposed_name = file
        if not has_spaces(file):
            print(f"Old name: {file}")
            issue_number = file.split(".")[0][-3:]
            proposed_name = f"Dragon Magazine {issue_number}.pdf"  
            print(f"New name: {proposed_name}")
            shutil.move(file, proposed_name)
        else:
            print(f"Skipping {file}")



@click.command()
@click.argument('runmode', required=False)
def run_fixNames(runmode):
    '''hack tool to fixing names of files and directories for kavita'''

        # Get the list of files in the current directory
    files = os.listdir('.')
    pdf_files = [file for file in files if file.endswith('.pdf')]
    cbz_files = [file for file in files if file.endswith('.cbz')]

    print(len(pdf_files), "PDF files found.")
    print(len(cbz_files), "CBZ files found.")  

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
    elif runmode == "rmtext":
        print('Running in fix FR mode')
        proposed_names = rmText(pdf_files)
    elif runmode == "dd":
        print('Running in fix Daredevil mode')
        proposed_names = ddProcess(cbz_files)
        proposed_names = ddProcess(pdf_files)
    elif runmode == "dragon":
        print('Running in fix Dragon Magazine mode')
        proposed_names = dragonProcess(pdf_files)
    else:
        print('No mode specified')
        proposed_names = []
    
    # Print the list of PDF files
    # print(proposed_names)


if __name__ == '__main__':
    run_fixNames()