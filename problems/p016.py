"""
Project Eurler Problem 16
http://projecteuler.net/problem=16
"""


def solve(number):
    digits = [int(digit) for digit in str(number)]
    result = sum(digits)
    print result


if __name__ == '__main__':
    solve(2 ** 1000)