"""
Project Eurler Problem 20 Solution
http://projecteuler.net/problem=20
"""

from math import factorial

def solve(n):
    return sum( [int(x) for x in str(factorial(n))] )

if __name__ == '__main__':
    print solve(100)