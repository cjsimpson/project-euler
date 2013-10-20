"""
Project Eurler Problem 48
http://projecteuler.net/problem=48
"""

def solve():
    result = 0
    for x in xrange(1, 1000 + 1):
        result += x**x
    return str(result)[-10:]

if __name__ == '__main__':
    print solve()