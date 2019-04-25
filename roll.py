import sys
import re

from dice.dice import Dice


def findDiceNbr(dice_tokens):
    central_index = dice_tokens.index("d")
    
    #print(dice_tokens[central_index-1])
    
    return dice_tokens[central_index-1]


def findDiceFaces(dice_tokens):
    central_index = dice_tokens.index("d")

    # print(dice_tokens[central_index-1])

    return dice_tokens[central_index + 1]


# def findRollModifier(dice_tokens):
    #first, check if there is any modifier
    #then, detect if this is a plus or minus modifier
    #then, save it

#     central_index = dice_tokens.index("d")
#
#     # print(dice_tokens[central_index-1])
#
#     return dice_tokens[central_index + 1]



def roll(dice_list=None):

    if dice_list is None:
        dice_list=["1d6"]

    for elem in dice_list:
        print("Roll as been requested :" + elem)

        dice_tokens = re.split('(; |, |\+|d|\-)', elem)
        print(dice_tokens)

        dice_nbr = findDiceNbr(dice_tokens)
        dice_faces = findDiceFaces(dice_tokens)

        dice = Dice(dice_nbr, dice_faces)

        #Modificator handling is not that simple
        #roll_modifier= findRollModifier(dice_tokens)

        #dice_list.append(dice)

        dice.roll()


if __name__ == '__main__':
    dice_requested = None
    if len(sys.argv) > 1:
        #get roll command argument
        dice_requested = sys.argv[1:]

    roll(dice_requested)


#TODO Add modifier parsing
#TODO Add error handlers for wrong inputs
#TODO Add option to get each dice value
#TODO Add option to get total sum with many arguments