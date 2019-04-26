import sys
import argparse
import re

from dice.dice import Dice
from dice.dicefactory import DiceFactory


def roll(dice_list=None):
    dice_factory = DiceFactory()

    if dice_list is None:
        dice_list=["1d6"]

    for elem in dice_list:
        print("Roll as been requested :" + elem)

        dice_tokens = re.split('(; |d|\+|\-)', elem)

        dice = dice_factory.pick(dice_tokens)

        dice.throw()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

    dice_requested = None

    if len(sys.argv) > 1:
        #get roll command argument
        dice_requested = [entry for entry in sys.argv[1:] if entry[0] != '-']

        for argument in sys.argv[:]:
            if argument in dice_requested:
                sys.argv.remove(argument)

    args = parser.parse_args()
    print(args, dice_requested)


    roll(dice_requested)


#TODO Add option to get each dice value
#TODO Add option to get total sum with many arguments
#TODO Add option to reroll open dices
