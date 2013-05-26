import unittest
from problems import p020

class TestProblem020(unittest.TestCase):
    def test_solve_example(self):
        self.assertEqual(p020.solve(10), 27)

if __name__ == '__main__':
    unittest.main()
