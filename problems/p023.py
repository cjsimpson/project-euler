"""
Project Eurler Problem 23
http://projecteuler.net/problem=23
"""

from problems.p021 import proper_divisors


# TODO: Could be faster
def solve():
    abundant_numbers = []
    for num in xrange(28123 + 1):
        #print num
        divisors = proper_divisors(num)
        if sum(divisors) > num:
            abundant_numbers.append(num)

    answer = set(xrange(28123 + 1))
    for i, x in enumerate(abundant_numbers):
        for n in abundant_numbers[i:]:
            if n+x > 28123:
                break
            if n + x in answer:
                answer.remove(n+x)

    print sum(answer)

if __name__ == '__main__':
    solve()