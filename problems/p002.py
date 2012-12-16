'''
Project Eurler Problem 2
http://projecteuler.net/problem=2
'''

LIMIT = 4000000
SEEDS = (1, 2)


def fib(limit):
    fib_sequence = list(SEEDS)
    while fib_sequence[-1] + fib_sequence[-2] < limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def solve():
    print sum(x for x in fib(LIMIT) if x % 2 == 0)
    
if __name__ == '__main__':
    solve()
