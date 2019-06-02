from random import randint


class Dice:
    """Dice class is here to handle dice information

    There is three attributes :
        dice_nbr (int) represents number of dices
        dice_faces (int), the number of faces of the dice
        modifier (int) that will be added to dice(s) score
    """

    def __init__(self, dice_nbr, dice_faces, modifier=0):
        self.dice_nbr = dice_nbr
        self.dice_faces = dice_faces
        self.modifier = modifier

    def throw(self, kwargs=None):
        """Main method to compute score obtain by a dice.

        It handles following options : open dices (-o)

        :param kwargs: list of command arguments (default is None)
        :return: total with modifier added and separated_values that saves each dice score
        :rtype: int, list
        """
        if kwargs is None:
            kwargs = {}

        total = 0
        separated_values = []

        for roll in range(0, self.dice_nbr):
            dice_result = randint(1, self.dice_faces)

            if kwargs.get("open") and dice_result == self.dice_faces:
                dice_result = self.reroll(dice_result)

            separated_values.append(dice_result)
            total += dice_result

        total += self.modifier

        return total, separated_values

    def reroll(self, dice_score):
        """
        This method recursively handles open dice

        :param dice_score: Current dice result to be evaluated before rerolling
        :type: int
        :return: final result for this open dice as
        :rtype: int
        """

        if dice_score == self.dice_faces:
            return dice_score + self.reroll(randint(1, self.dice_faces))
        else:
            return dice_score

    def __str__(self):
        return str(self.dice_nbr)+"d"+str(self.dice_faces)+str(self.modifier)
