import unittest
from letters_of_phone_number.letters_of_phone_number import letter_combinations

class Test_Letters_of_phone_number(unittest.TestCase):
    def test_small(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(letter_combinations(digits), expected)

    def test_empty_input(self):
        digits = ""
        expected = []
        self.assertEqual(letter_combinations(digits), expected)

if __name__ == '__main__':
    unittest.main()