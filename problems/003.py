'''
Project Eurler Problem 3
http://projecteuler.net/problem=3
'''

def find_factors(number):
    factors = []
    for x in xrange(1, int(number**0.5) + 1):
        if number % x == 0 and x!= 1:
            factors.append(x)
    return factors

def is_prime(number):
    factors = find_factors(number)
    if len(factors) == 0:   
        return True
    else:
        return False

NUMBER = 600851475143    
factors = find_factors(NUMBER)
prime_factors = [x for x in factors if is_prime(x)]
print prime_factors[-1]