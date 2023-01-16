import unittest

from diceware.core import roll_dice

class TestCore(unittest.TestCase):

    def test_roll_dice(self):

        self.assertEqual(len(roll_dice(1)), 1)
        self.assertEqual(len(roll_dice(2)), 2)
        self.assertEqual(len(roll_dice(3)), 3)
        
        self.assertIsInstance(roll_dice(1), str)

if __name__ == "__main__":
    unittest.main()
