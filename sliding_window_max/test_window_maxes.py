import unittest
from window_maxes import window_maxes

class Test_window_maxes(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(window_maxes([1, 2, 3], 2), [2,3])

    def test_tiny(self):
        self.assertEqual(window_maxes([1], 1), [1])

    def test_description(self):
        self.assertEqual(window_maxes([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])

    def test_empty_list(self):
        self.assertEqual(window_maxes([], 2), [])
