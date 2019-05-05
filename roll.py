import sys
import argparse

from dice.dicefactory import DiceFactory
from diceutils import parse_dice_request


def advantage_decorator(roll_func, dice_list, kwargs=None):
    def advantage_wrapper():
        roll_func(dice_list, kwargs=kwargs)

def roll(dice, kwargs=None):
    dice_factory = DiceFactory()
    separated_values = []
    separated_values_bis= []
    hand_total = 0

    if dice is None:
        dice = dice_factory.pick_custom(1,6)

    if  kwargs["verbose"]:
        print("Roll as been requested : " + dice.__str__())

    total, separated_values  = dice.throw(kwargs=kwargs)

    if kwargs["advantage"]:
        total_bis, separated_values_bis = dice.throw(kwargs=kwargs)
        if kwargs["verbose"]:
            print("Second roll with advantage scored:", total_bis)

        if total_bis > total:
            total = total_bis
            separated_values = separated_values_bis

    print(total)
    #hand_total+=total

    if kwargs["separated_values"]:
        if kwargs["verbose"]:
            print("Each dice score is:")
        print(separated_values)

    #if kwargs["sum"]:
        #print(hand_total)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    #parser.add_argument("-s", "--sum", help="return the sum of all thrown dices", action="store_true")
    parser.add_argument("-S", "--separated-values", help="each result is displayed", action="store_true")
    parser.add_argument("-r", "--reroll", help="reroll open dices (a dice is open when it rolls max value)", action="store_true")
    parser.add_argument("-a", "--advantage",  help="dices will be rolled twice, picking highest", action="store_true")
    parser.add_argument("-d", "--disadvantage",  help="dice will be rolled twice, picking lowest", action="store_true")


    dice_requested = None

    if len(sys.argv) > 1:
        #get roll command argument
        dice_requested = [entry for entry in sys.argv[1:] if entry[0] != '-']

        for argument in sys.argv[:]:
            if argument in dice_requested:
                sys.argv.remove(argument)

    raw_args = parser.parse_args()
    args = vars(raw_args)

    dice_requested = parse_dice_request(dice_requested)

    print(dice_requested)


    for dice in dice_requested:
        roll(dice, kwargs=args)

#TODO Add disadvantage rolls
#TODO Refactor --sum arg