'''
Project Eurler Problem 9
http://projecteuler.net/problem=9
'''

def is_pythagorean(a, b, c):
    return a**2 + b**2 == c**2

def natural_nums_for_sum(summation):
    for a in xrange(1, int(summation/2)):
        for b in xrange(a+1, summation):
            for c in xrange(b+1, summation):
                if a + b + c == summation:
                    yield (a,b,c)

if __name__ == '__main__':
    for a,b,c in natural_nums_for_sum(1000):
        if is_pythagorean(a,b,c):
            print a*b*c
            return