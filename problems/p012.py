"""
Project Eurler Problem 12
http://projecteuler.net/problem=12
"""

from p003 import find_factors


def triangle_number(n):
    triangle_num = 0
    for x in xrange(n + 1):
        triangle_num += x
    return triangle_num


def solve():
    factors = 0
    z = 0
    while factors < 250:    # 250 pairs of factors = 500 factors
        z += 1
        factors = len(find_factors(triangle_number(z)))
    print triangle_number(z)


if __name__ == '__main__':
    solve()
