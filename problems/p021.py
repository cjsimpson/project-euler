"""
Project Eurler Problem 21 Solution
http://projecteuler.net/problem=21
"""

def proper_divisors(n):
    divisors = []
    if n > 1:
        divisors.append((1))
    for x in xrange(1, n-1 + 1):
        if n % x == 0 and x != 1:
            divisors.append(x)
    return divisors

def sum_proper_divisors(n):
    return sum(proper_divisors(n))

def sum_amicable_pairs_below(n):
    pairs = []
    for x in xrange(1, n):
        d1 = sum_proper_divisors(x)
        if d1 == x:
            continue
        if d1 in pairs:
            continue
        d2 = sum_proper_divisors(d1)
        if x == d2:
            pairs.append(d1)
            pairs.append(d2)

    print pairs
    return sum(pairs)

def solve(n):
    return sum_amicable_pairs_below(n)

if __name__ == '__main__':
    print solve(10000)