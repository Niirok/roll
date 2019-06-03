import unittest

from src.dice.dicefactory import DiceFactory


class TestDiceFactoryMethods(unittest.TestCase):


    def test_1_wrong_input_no_mod(self):
        facto = DiceFactory()

        with self.assertRaises(ValueError):
            facto.pick_custom( -4, 'sadsad')

    def test_1_wrong_input_with_mod(self):
        facto = DiceFactory()

        with self.assertRaises(ValueError):
            facto.pick_custom( 4, 'sadsad', -6)


    def test_2_wrong_input_no_mod(self):
        facto = DiceFactory()

        with self.assertRaises(ValueError):
            facto.pick_custom("sadsad", 'sadsad')

    def test_2_wrong_input_with_mod(self):
        facto = DiceFactory()

        with self.assertRaises(ValueError):
            facto.pick_custom("sadsad", 'sadsad', -6)

    def test_happy_case_mod(self):
        facto = DiceFactory()

        happy_dice = facto.pick_custom(4, 6, -6)

        print(happy_dice)

        self.assertEqual(happy_dice.dice_nbr, 4)
        self.assertEqual(happy_dice.dice_faces, 6)
        self.assertEqual(happy_dice.modifier, -6)

    def test_happy_case_no_mod(self):
        facto = DiceFactory()

        happy_dice = facto.pick_custom(4, 6)

        print(happy_dice)

        self.assertEqual(happy_dice.dice_nbr, 4)
        self.assertEqual(happy_dice.dice_faces, 6)
        self.assertEqual(happy_dice.modifier, 0)

if __name__ == '__main__':
    unittest.main()