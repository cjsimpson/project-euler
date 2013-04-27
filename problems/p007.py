"""
Project Eurler Problem 7
http://projecteuler.net/problem=7
"""

from p003 import is_prime


def find_nth_prime(n):
    prime_list = set()
    x = 1
    while len(prime_list) < n:
        if is_prime(x):
            prime_list.add(x)
        x += 1
    return max(prime_list)


def solve():
    print find_nth_prime(10001)


if __name__ == '__main__':
    solve()
