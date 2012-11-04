'''
Project Eurler Problem 10
http://projecteuler.net/problem=10
'''
#TODO: This runs too slow

def is_prime(number):
    if number in (0,1):
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def primes_in_range(low, high):
    for x in xrange(low, high):
        if is_prime(x):
            yield x
 
if __name__ == '__main__':
    sum_of_primes = 0
    for x in primes_in_range(1,2000000):
        sum_of_primes += x
    print
    print sum_of_primes