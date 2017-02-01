import unittest
#from test import support
import dice


class TestDiceRoll(unittest.TestCase):

    def test_if_dice_roll_gives_int(self):
        self.assertIsInstance(dice.roll(), int)

    def test_if_roll_is_probably_random(self):
        rolls = set()
        for _ in range(10):
            roll = dice.roll()
            rolls.add(roll)

        self.assertNotEqual(len(rolls), 10)

    def test_is_not_random(self):
        rolls = set()
        for _ in range(10):
            roll = dice.roll()
            rolls.add(roll)

        self.assertEqual(len(rolls), 10)
        



if __name__ == '__main__':
    unittest.main()
