#!/usr/bin/env python
'''No docstring has been added yet.'''

import click
import os
import shutil

import myhacks as myh


def find_files_with_extension(root_dir, extension, exclude_dir):
    """
    Recursively find all files with a given extension in a specified root directory,
    excluding a specified directory.
    
    :param root_dir: Root directory to start the search
    :param extension: File extension to search for
    :param exclude_dir: Directory to exclude from the search
    """
    matching_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if exclude_dir in dirnames:
            dirnames.remove(exclude_dir)
        for filename in filenames:
            if filename.endswith(extension):
                matching_files.append(os.path.join(dirpath, filename))
    return matching_files


def move_file_to_directory(src_file, dest_dir):
    """
    Move a file to a specified directory.
    
    :param src_file: Source file path
    :param dest_dir: Destination directory path
    """
    dest_path = os.path.join(dest_dir, os.path.basename(src_file))
    shutil.move(src_file, dest_path)
    print(f"Moved {src_file} to {dest_path}")


@click.command()
@click.argument('root_dir', required=True)
@click.argument('extension', required=True)
@click.argument('exclude_dir', required=True)
def run_consolidateFiles(root_dir, extension, exclude_dir):
    '''Recursively find all files with a given extension in a specified root directory, excluding a specified directory.'''

    files = find_files_with_extension(root_dir, extension, exclude_dir)
    for file in files:
        move_file_to_directory(file, root_dir)


if __name__ == '__main__':
    run_consolidateFiles()