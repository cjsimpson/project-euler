'''
Project Eurler Problem 1
http://projecteuler.net/problem=1
'''

def solve():
     multiples_of_3_and_5 = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
    print sum(multiples_of_3_and_5)
       
if __name__ == '__main__':
    solve()
