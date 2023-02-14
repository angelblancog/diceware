import unittest

from diceware.passwords import reseed, generate_password

class TestCore(unittest.TestCase):

    def test_reseed_seeds(self):

        reseed(1)
        pass_1 = generate_password()

        reseed(1)
        pass_2 = generate_password()

        self.assertEqual(pass_1, pass_2)

    def test_passwords_are_random(self):

        pass_1 = generate_password(50)
        pass_2 = generate_password(50)

        self.assertNotEqual(pass_1, pass_2)

    def test_password_length(self):

        for required_length in range(50):
            self.assertEqual(required_length, len(generate_password(required_length)))

if __name__ == "__main__":
    unittest.main()
