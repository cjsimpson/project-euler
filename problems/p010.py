'''
Project Eurler Problem 10
http://projecteuler.net/problem=10
'''
#TODO: This still runs too slow


def is_prime(number):
    if number in (0, 1):
        return False
    for i in xrange(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def primes_in_range(low, high):

    def remove_multiples(source, n):
        multiple = n
        multiplier = 2
        max_value = max(source)
        while multiple < max_value:
            multiple = n * multiplier
            source.discard(multiple)
            multiplier += 1
        return source

    potential_primes = set(xrange(low, high + 1))
    potential_primes.discard(1)

    for k in xrange(2, int(high ** 0.5) + 1):
        if is_prime(k):
            remove_multiples(potential_primes, k)

    return potential_primes

if __name__ == '__main__':
    print sum(primes_in_range(1, 2000000))

