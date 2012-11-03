'''
Project Eurler Problem 4
http://projecteuler.net/problem=4
'''

def is_number_a_palidrome(number):
    return str(number) == str(number)[::-1]

def all_products(low_number, high_number):
    all_products = set()
    for x in xrange(low_number, high_number + 1):
        for y in xrange(low_number, high_number + 1):
            if x*y not in all_products:
                all_products.add(x*y)
    return all_products

all_palindromes = [x for x in all_products(100,1000) if is_number_a_palidrome(x)]
print max(all_palindromes)