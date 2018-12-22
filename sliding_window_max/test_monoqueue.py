import unittest
from monoqueue import Monoqueue

class Test_Monoqueue(unittest.TestCase):
    def setUp(self):
        self.mq = Monoqueue()
        
    def test_increasing(self):
        self.mq.push(0)
        self.assertEqual(self.mq.front(), 0)
        self.mq.push(1)
        self.assertEqual(self.mq.front(), 1)
        self.mq.push(2)
        self.assertEqual(self.mq.front(), 2)

    def test_valley(self):
        self.mq.push(0)
        self.assertEqual(self.mq.front(), 0)
        self.mq.push(1)
        self.assertEqual(self.mq.front(), 1)
        self.mq.push(2)
        self.mq.push(0)
        self.mq.pop(2)
        self.assertEqual(self.mq.front(), 0)
        self.mq.push(1)
        self.assertEqual(self.mq.front(), 1)

    def test_front_empty(self):
        self.assertRaises(IndexError, lambda: self.mq.front())
        self.mq.push(1)
        self.mq.pop(1)
        self.assertRaises(IndexError, lambda: self.mq.front())

if __name__ == '__main__':
    unittest.main()