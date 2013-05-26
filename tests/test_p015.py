import unittest
from problems import p015

class TestProblem015(unittest.TestCase):
    def test_solve_2x2(self):
        self.assertEqual(p015.solve(2), 6)


    def test_solve_3x3(self):
        self.assertEqual(p015.solve(3), 20)

if __name__ == '__main__':
    unittest.main()
