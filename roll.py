import argparse
import sys

from src.dice.dicefactory import DiceFactory
from src.dice.diceutils import parse_dice_request


def roll_advantage(dice, score, sep_values, kwargs=None):
    """Support method to handle -a (advantage) option

    :param dice: Dice object that needs to be rolled once again
    :type: Dice
    :param score: score obtained on first roll
    :param sep_values: each dice value obtained on first roll
    :param kwargs:
    :return: highest results (score, sep_values) of both rolls
    """

    second_roll, second_separated_values = dice.throw(kwargs=kwargs)

    if kwargs.get("verbose"):
        print("Second roll with advantage scored:", second_roll)

    if second_roll > score:
        score = second_roll
        sep_values = second_separated_values

    return score, sep_values


def roll_disadvantage(dice, score, sep_values, kwargs=None):
    """Support method to handle -d (disadvantage) option

    :param dice: Dice object that needs to be rolled once again
    :type: Dice
    :param score: score obtained on first roll
    :param sep_values: each dice value obtained on first roll
    :param kwargs:
    :return: highest results (score, sep_values) of both rolls
    """

    second_roll, second_separated_values = dice.throw(kwargs=kwargs)

    if kwargs["verbose"]:
        print("Second roll with advantage scored:", second_roll)

    if second_roll < score:
        score = second_roll
        sep_values = second_separated_values

    return score, sep_values


def sum_decorator(roll_func, dice_list, kwargs=None):
    def sum_wrapper():
        hand_total = 0
        for dice in dice_list:
            hand_total += roll_func(dice, kwargs=kwargs)

        return hand_total

    dice_sum = sum_wrapper()

    if kwargs["verbose"]:
        print("Sum of all dices is: ")
    print(dice_sum)


def roll(dice=None, kwargs=None):
    dice_factory = DiceFactory()

    if dice is None:
        dice = dice_factory.pick_custom(1, 6)
    if kwargs is None:
        kwargs = {}

    if kwargs["verbose"]:
        print("Roll as been requested : " + dice.__str__())

    total, separated_values  = dice.throw(kwargs=kwargs)

    if kwargs["advantage"]:
        total, separated_values = roll_advantage(dice, total, separated_values, kwargs)

    if kwargs["disadvantage"]:
        total, separated_values = roll_disadvantage(dice, total, separated_values, kwargs)

    if kwargs["separated_values"]:
        if kwargs["verbose"]:
            print("Each dice score is:")
        print(separated_values)

    else:
        print(total)

    return total


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-s", "--sum", help="return the sum of all thrown dices", action="store_true")
    parser.add_argument("-S", "--separated-values", help="each result is displayed", action="store_true")
    parser.add_argument("-o", "--open", help="reroll open dices (a dice is open when it scores max value)",
                        action="store_true")
    parser.add_argument("-a", "--advantage",  help="dices will be rolled twice, picking highest", action="store_true")
    parser.add_argument("-d", "--disadvantage",  help="dice will be rolled twice, picking lowest", action="store_true")

    dice_requested = None

    print(sys.argv)

    if len(sys.argv) > 1:
        # get roll command argument
        dice_requested = [entry for entry in sys.argv[1:] if entry[0] != '-']

        for argument in sys.argv[:]:
            if argument in dice_requested:
                sys.argv.remove(argument)

    raw_args = parser.parse_args()
    args = vars(raw_args)

    if args["advantage"] and args["disadvantage"]:
        parser.error("You cant't have both options advantage and disadvantage for the same roll")

    dice_requested = parse_dice_request(dice_requested)

    if args["sum"]:
        sum_decorator(roll, dice_requested, kwargs=args)

    else:
        for dice in dice_requested:
            roll(dice, kwargs=args)

