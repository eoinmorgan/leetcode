import unittest
from generate_parens.generate_parens import generate_parens

class Test_generate_parens(unittest.TestCase):
    def test_none(self):
        self.assertEqual(generate_parens(0), [])

    def test_negative(self):
        self.assertEqual(generate_parens(-1), [])

    def test_one(self):
        self.assertEqual(generate_parens(1), ['()'])

    def test_two(self):
        self.assertEqual(generate_parens(2), ['(())', '()()'])

    def test_three(self):
        self.assertEqual(generate_parens(3), [
            '((()))',
            '(()())',
            '(())()',
            '()(())',
            '()()()',
        ])

if __name__ == '__main__':
    unittest.main()