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



def roll(input_dice="1d6"):
    dice_list = []


    print("Roll as been requested :" + input_dice)

    dice_tokens = re.split('(; |, |\+|d|\-)', input_dice)
    print(dice_tokens)

    dice_nbr = findDiceNbr(dice_tokens)
    dice_faces = findDiceFaces(dice_tokens)

    dice = Dice(dice_nbr, dice_faces)

    #dice_list.append(dice)

    dice.roll()

    #Modificator handling is not that simple
    #roll_modifier= findRollModifier(dice_tokens)

if __name__ == '__main__':
    # get args, then roll
    roll()