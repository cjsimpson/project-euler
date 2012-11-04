'''
Project Eurler Problem 5
http://projecteuler.net/problem=4
'''

from p003 import find_prime_factors, find_factors, is_prime

def find_prime_factorization(number):
    all_factors = find_factors(number)
    prime_factorization = []
    if len(all_factors) == 1:
        prime_factorization.extend([x for x in all_factors[0]])
    else:
        all_factors.remove((1,number))
        factor_pair = all_factors.pop()
    
        for f in factor_pair:
            if is_prime(f):
                prime_factorization.append(f)
            elif f not in (1, number):
                map(lambda x: prime_factorization.append(x), find_prime_factors(f))
    return prime_factorization
        
def find_lowest_common_multiple(list_of_numbers):
    if 1 in list_of_numbers:
        list_of_numbers.remove(1)
    prime_factors = {x:find_prime_factorization(x) for x in list_of_numbers}
    primes = prime_factors.values()
    prime_count = {}
    for x in primes:
        for y in x:
            count = x.count(y)
            if y in prime_count:
                if count > prime_count[y]:
                    prime_count[y] = count
            else:
                prime_count[y] = count
    
    result = reduce(lambda x,y: x*y, [k**v for k,v in prime_count.iteritems()])
    return result

if __name__ == '__main__':
    print find_lowest_common_multiple(range(1,21))
