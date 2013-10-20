"""
Project Eurler Problem 24
http://projecteuler.net/problem=24
"""

def solve():
    digits = map(lambda x: str(x), list(xrange(0, 9 + 1)))
    results = []
    for i, x in enumerate(digits):
        results.append('%s%s' % (x, ''.join(digits[i+1:] + digits[:i])))

    print results

if __name__ == '__main__':
    solve()