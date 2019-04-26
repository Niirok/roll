from dice.dice import Dice


class DiceFactory:

    def __init__(self):
        pass

    def findDiceNbr(self, dice_tokens):
        try:
            central_index = dice_tokens.index("d")
        except Exception as e:
            print("Error parsing input command: ", e)
            sys.exit(4)

        return int(dice_tokens[central_index - 1])

    def findDiceFaces(self, dice_tokens):
        try:
            central_index = dice_tokens.index("d")
        except Exception as e:
            print("Error parsing input command: ", e)
            sys.exit(4)

        return int(dice_tokens[central_index + 1])

    def findRollModifier(self, dice_tokens):
        plus_modifier = 0
        minus_modifier = 0

        try:
            modifier_plus_index = dice_tokens.index("+")
            plus_modifier = dice_tokens[modifier_plus_index + 1]
        except ValueError:
            pass

        try:
            modifier_minus_index = dice_tokens.index("-")
            minus_modifier = dice_tokens[modifier_minus_index + 1]
        except ValueError:
            pass

        total = int(plus_modifier) - int(minus_modifier)

        return total

    def pick(self, dice_tokens):
        dice_nbr = self.findDiceNbr(dice_tokens)
        dice_faces = self.findDiceFaces(dice_tokens)
        roll_modifier = self.findRollModifier(dice_tokens)

        return Dice(dice_nbr, dice_faces, roll_modifier)