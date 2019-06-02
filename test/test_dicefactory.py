import os
import unittest

import sys

from src.dicefactory import DiceFactory

sys.path.append(os.getcwd())
print(sys.path)

#from src.roll import roll


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

class TestRoll(unittest.TestCase):
    test_dice_factory = DiceFactory()
    test_dice = test_dice_factory.pick_custom(1, 20)

    def test_default_case(self):
        pass
        #default_result = roll()
        #self.assertTrue(1 <= default_result <= 6)
