#!/usr/bin/env python
"""A utility to roll dice of different sorts."""

import click
import os

import myhacks as myh


def parse_dice_string(dice_string):
    '''Parses dice string.'''

    string_parts = dice_string.split('d')

    num_dice = string_parts[0]

    print(f'Rolling {num_dice} dice.')


def roll(dice_string):
    '''Rolls a number of dice, as specified by the string.'''

    dice_info = parse_dice_string(dice_string)

@click.command()
@click.argument("dice_string", default="1d20", required=False)
def run_roll(dice_string):
    """Rolls dice of various sorts using the ndm + x format."""

    print(f"Rolling {dice_string}.")

    roll(dice_string)

if __name__ == "__main__":
    run_roll()
