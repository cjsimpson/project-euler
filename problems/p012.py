'''
Project Eurler Problem 12
http://projecteuler.net/problem=12
'''

from p003 import find_factors

def triangle_number(n):
    triangle_num = 0
    for x in xrange(n+1):
        triangle_num += x
    return triangle_num

if __name__ == '__main__':
    factors = 0
    x = 0
    while factors < 250:    #250 pairs of factors = 500 factors
        x += 1
        factors = len(find_factors(triangle_number(x)))
    print triangle_number(x)