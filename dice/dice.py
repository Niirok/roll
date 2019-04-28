from random import randint

class Dice:

    def __init__(self, dice_nbr, dice_faces, modifier):
        self.dice_nbr = dice_nbr
        self.dice_faces = dice_faces
        self.modifier = modifier

    def throw(self):
        total = 0
        separated_values = []
        dice_result= 0

        for roll in range (0, self.dice_nbr):
            dice_result = randint(1, self.dice_faces)
            separated_values.append(dice_result)
            total += dice_result

        total+=self.modifier

        return total, separated_values
