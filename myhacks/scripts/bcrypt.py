
#!/usr/bin/env python
'''No docstring has been added yet.'''

import bcrypt
import sys

import click
import os

import myhacks as myh

@click.command()
@click.argument('password', required=True)
def run_bcrypt(password):
    '''test docstring'''


    # Convert the password to bytes
    bytes = password.encode('utf-8')

    # Generate the salt
    salt = bcrypt.gensalt()

    # Compute the password hash and print
    hash = bcrypt.hashpw(bytes, salt)
    print(f"{hash=}")


if __name__ == '__main__':
    run_bcrypt()