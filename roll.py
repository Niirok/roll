import sys
import argparse
import re

from dice.dice import Dice
from dice.dicefactory import DiceFactory


def roll(dice_list=None, kwargs=None):
    dice_factory = DiceFactory()
    separated_values = []
    hand_total = 0

    if dice_list is None or dice_list==[]:
        dice_list=["1d6"]

    for elem in dice_list:
        if  kwargs["verbose"]:
            print("Roll as been requested :" + elem)

        dice_tokens = re.split('(; |d|\+|\-)', elem)
        dice = dice_factory.pick(dice_tokens)

        total, separated_values  = dice.throw()
        print(total)
        hand_total+=total

        if kwargs["separate_values"]:
            print(separated_values)

    if kwargs["sum"]:
        print(hand_total)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-s", "--sum", help="return the sum of all thrown dices", action="store_true")
    parser.add_argument("-S", "--separate_values", help="each result is displayed", action="store_true")

    dice_requested = None

    if len(sys.argv) > 1:
        #get roll command argument
        dice_requested = [entry for entry in sys.argv[1:] if entry[0] != '-']

        for argument in sys.argv[:]:
            if argument in dice_requested:
                sys.argv.remove(argument)

    raw_args = parser.parse_args()
    args = vars(raw_args)


    roll(dice_requested, kwargs=args)

#TODO Add option to reroll open dices
