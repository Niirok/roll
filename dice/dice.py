from random import randint

class Dice:

    def __init__(self, dice_nbr, dice_faces, modifier):
        self.dice_nbr = dice_nbr
        self.dice_faces = dice_faces
        self.modifier = modifier

    def throw(self):
        total = 0
        for roll in range (0, self.dice_nbr):
            total += randint(1, self.dice_faces)

        total+=self.modifier

        print(total)
