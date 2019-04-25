import sys
import re

from dice.dice import Dice


def findDiceNbr(dice_tokens):
    central_index = dice_tokens.index("d")
    return dice_tokens[central_index-1]


def findDiceFaces(dice_tokens):
    central_index = dice_tokens.index("d")

    return dice_tokens[central_index + 1]


def findRollModifier(dice_tokens):
    plus_modifier = 0
    minus_modifier = 0

    try :
        modifier_plus_index = dice_tokens.index("+")
        plus_modifier = dice_tokens[modifier_plus_index+1]
    except ValueError:
        pass

    try:
        modifier_minus_index = dice_tokens.index("-")
        minus_modifier = dice_tokens[modifier_minus_index + 1]
    except ValueError:
        pass

    total = int(plus_modifier) - int(minus_modifier)

    return total


def roll(dice_list=None):

    if dice_list is None:
        dice_list=["1d6"]

    for elem in dice_list:
        print("Roll as been requested :" + elem)

        dice_tokens = re.split('(; |d|\+|\-)', elem)
        print(dice_tokens)

        dice_nbr = findDiceNbr(dice_tokens)
        dice_faces = findDiceFaces(dice_tokens)
        roll_modifier = findRollModifier(dice_tokens)

        dice = Dice(dice_nbr, dice_faces, roll_modifier)

        #dice_list.append(dice)

        dice.roll()


if __name__ == '__main__':
    dice_requested = None
    if len(sys.argv) > 1:
        #get roll command argument
        dice_requested = sys.argv[1:]

    roll(dice_requested)


#TODO Add error handlers for wrong inputs
#TODO Add option to get each dice value
#TODO Add option to get total sum with many arguments
#TODO Add option to reroll open dices
