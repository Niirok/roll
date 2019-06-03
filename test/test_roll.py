import unittest

from roll import roll
from src.dice.dicefactory import DiceFactory

class TestRoll(unittest.TestCase):
    test_dice_factory = DiceFactory()
    test_dice = test_dice_factory.pick_custom(1, 20)

    def test_default_case(self):
        default_result = roll()
        self.assertTrue(1 <= default_result <= 6)

if __name__ == '__main__':
    unittest.main()