#!/usr/bin/env python
"""A utility to roll dice of different sorts."""

import click
import pyparsing as pp
import os

import myhacks as myh


class DiceRoller:
    """Rolls dice for a given DiceRoll spec."""

    def __init__(self, roll_spec):
        """Initializes the roller with the given specification."""

        self.spec = roll_spec


class RollSpec:
    """Contains information needed to make a specific roll."""

    def __init__(self, sides, number, modifier):
        """Sets up information for roll specified."""

        self.sides = sides
        self.number = number
        self.modifier = modifier


class DiceStringParser:
    """Parser to parse a dice string."""

    def __setup_parser(self):
        """Sets up the grammar for the parser."""
        pass

    def __init__(self):
        self.__setup_parser()


def parse_dice_string(dice_string):
    """Parses dice string."""

    string_parts = dice_string.split("d")

    num_dice = string_parts[0]

    print(f"Rolling {num_dice} dice.")


def roll(dice_string):
    """Rolls a number of dice, as specified by the string."""

    dice_info = parse_dice_string(dice_string)


@click.command()
@click.argument("dice_string", default="1d20", required=False)
def run_roll(dice_string):
    """Rolls dice of various sorts using the ndm + x format."""

    print(f"Rolling {dice_string}.")

    roll(dice_string)


if __name__ == "__main__":
    run_roll()
