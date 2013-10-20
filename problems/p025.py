"""
Project Eurler Problem 25
http://projecteuler.net/problem=25
"""

def fib(n):
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a + b
    return a

def solve():
    i = 1
    while True:
        result = fib(i)
        l = len(str(result))
        if l == 1000:
            return i
            break
        i += 1


if __name__ == '__main__':
    print solve()