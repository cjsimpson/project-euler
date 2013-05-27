import unittest
from problems import p018

EXAMPLE_DATA = """ 3
                  7 4
                 2 4 6
                8 5 9 3 """

class TestProblem018(unittest.TestCase):
    def test_parse(self):
        new_data = p018.parse_input(EXAMPLE_DATA)
        expected = [(3,), (7, 4), (2, 4, 6), (8, 5, 9, 3)]
        self.assertEqual(new_data, expected)

    def test_solve_example(self):
        self.assertEqual(p018.solve(EXAMPLE_DATA), 23)

    def test_solve_simple_triangle(self):
        data = """ 3
                  7 4
                 1 4 6
                8 2 1 3 """
        self.assertEqual(p018.solve(data), 19)

if __name__ == '__main__':
    unittest.main()