import re

from dicefactory import DiceFactory


def convert_args_to_dice_object(dice_args_list):
    return list(map(lambda dice_request: re.split('(; |d|\+|-)', dice_request), dice_args_list))


def create_dice_object(parced_dices, dice_factory=None):
    if dice_factory is None:
        dice_factory = DiceFactory()
    return list(map(lambda dice_object: dice_factory.pick(dice_object), parced_dices))


def parse_dice_request(input_cmd):
    dice_list = []
    dice_factory = DiceFactory()

    if input_cmd is None or input_cmd == []:
        dice_list.append(dice_factory.pick_custom(1, 6))
    else:
        dice_list = create_dice_object(convert_args_to_dice_object(input_cmd), dice_factory)

    return dice_list
