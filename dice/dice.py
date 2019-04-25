from random import randint

class Dice:

    def __init__(self, dice_nbr, dice_faces, modifier):
        #check if inputs are str or int
        self.dice_nbr = int(dice_nbr)
        self.dice_faces = int(dice_faces)
        self.modifier = modifier

    def roll(self):
        total = 0
        for roll in range (0, self.dice_nbr):
            total += randint(1, self.dice_faces)

        print(total)

        total+=self.modifier

        print(total)
