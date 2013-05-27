import unittest
from problems import p021

class TestProblem021(unittest.TestCase):
    def test_proper_divisors_220(self):
        self.assertEqual(p021.proper_divisors(220), [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])

    def test_proper_divisors_284(self):
        self.assertEqual(p021.proper_divisors(284), [1, 2, 4, 71, 142])

    def test_sum_proper_divisors_220(self):
        self.assertEqual(p021.sum_proper_divisors(220), 284)

    def test_sum_proper_divisors_284(self):
        self.assertEqual(p021.sum_proper_divisors(284), 220)

if __name__ == '__main__':
    unittest.main()
