"""
Project Eurler Problem 37
http://projecteuler.net/problem=37
"""

from p003 import is_prime


def solve():
    truncatable_primes = []

    i = 1
    while len(truncatable_primes) < 11:
        if is_prime(i):
            if i > 10:
                str_i = str(i)
                truncated_combinations = []
                if len(str_i) >= 2:

                    # Get all forward/backward combinations
                    for pos, n in enumerate(str_i, start=1):
                        if pos == len(str_i):
                            break
                        truncated_combinations.append(str_i[pos:])
                        truncated_combinations.append(str_i[:-pos])

                    # Check if these numbers are all primes
                    can_add = not (not truncated_combinations) # False when list is empty
                    for n in truncated_combinations:
                        if not is_prime(int(n)):
                            can_add = False
                            break
                    if can_add:
                        truncatable_primes.append(i)
        i += 1

    print sum(truncatable_primes)


if __name__ == '__main__':
    solve()
