from random import randint

class Dice:

    def __init__(self, dice_nbr, dice_faces, modifier):
        self.dice_nbr = dice_nbr
        self.dice_faces = dice_faces
        self.modifier = modifier

    def throw(self, kwargs=None):
        total = 0
        separated_values = []
        dice_result= 0

        for roll in range (0, self.dice_nbr):
            dice_result = randint(1, self.dice_faces)

            if kwargs["reroll"] and dice_result == self.dice_faces:
                dice_result = self.reroll(dice_result)

            separated_values.append(dice_result)
            total += dice_result

        total+=self.modifier

        return total, separated_values

    def reroll(self, dice_score):
        if dice_score == self.dice_faces:
            return dice_score + self.reroll(randint(1, self.dice_faces))
        else :
            return dice_score

